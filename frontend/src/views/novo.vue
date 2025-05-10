<template>
    <div class="invitation-manager">
      <div class="row">
        <!-- Sidebar -->
        <div class="col-md-4 sidebar">
          <div class="card">
            <div class="card-header">
              <h5>Enviar Convite</h5>
            </div>
            <div class="card-body">
              <div class="mb-3">
                <label class="form-label">Selecione um usuário</label>
                <select v-model="selectedUser" class="form-select">
                  <option value="" disabled>Selecione</option>
                  <option v-for="user in availableUsers" :key="user.id" :value="user">
                    {{ user.full_name || user.email }}
                  </option>
                </select>
              </div>
              <button @click="sendInvitation" class="btn btn-primary" :disabled="!selectedUser">
                Enviar Convite
              </button>
            </div>
          </div>
        </div>
  
        <!-- Main Content -->
        <div class="col-md-8">
          <div class="row">
            <!-- Received Invitations -->
            <div class="col-md-6">
              <div class="card">
                <div class="card-header d-flex justify-content-between align-items-center">
                  <h5>Convites Recebidos</h5>
                  <button @click="fetchInvitations" class="btn btn-sm btn-outline-secondary">
                    Atualizar
                  </button>
                </div>
                <div class="card-body">
                  <div v-if="loading" class="text-center py-4">
                    <div class="spinner-border text-primary" role="status">
                      <span class="visually-hidden">Carregando...</span>
                    </div>
                  </div>
                  <div v-else-if="receivedInvitations.length === 0" class="alert alert-info">
                    Nenhum convite recebido
                  </div>
                  <div v-else class="list-group">
                    <div v-for="inv in receivedInvitations" :key="inv.id" class="list-group-item">
                      <div class="d-flex justify-content-between align-items-center">
                        <div>
                          <strong>{{ inv.sender__full_name || inv.sender__email }}</strong>
                          <small class="text-muted d-block">{{ formatDate(inv.created_at) }}</small>
                        </div>
                        <div>
                          <button @click="handleInvitation(inv.id, 'accept')" class="btn btn-sm btn-success me-2">
                            Aceitar
                          </button>
                          <button @click="handleInvitation(inv.id, 'reject')" class="btn btn-sm btn-danger">
                            Rejeitar
                          </button>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
  
            <!-- Sent Invitations -->
            <div class="col-md-6">
              <div class="card">
                <div class="card-header">
                  <h5>Convites Enviados</h5>
                </div>
                <div class="card-body">
                  <div v-if="loading" class="text-center py-4">
                    <div class="spinner-border text-primary" role="status">
                      <span class="visually-hidden">Carregando...</span>
                    </div>
                  </div>
                  <div v-else-if="sentInvitations.length === 0" class="alert alert-info">
                    Nenhum convite enviado
                  </div>
                  <div v-else class="list-group">
                    <div v-for="inv in sentInvitations" :key="inv.id" class="list-group-item">
                      <div class="d-flex justify-content-between align-items-center">
                        <div>
                          <strong>{{ inv.recipient__full_name || inv.recipient__email }}</strong>
                          <small class="text-muted d-block">
                            {{ formatDate(inv.created_at) }} - 
                            <span :class="`badge bg-${getStatusColor(inv.status)}`">
                              {{ getStatusText(inv.status) }}
                            </span>
                          </small>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  const apiUrl = 'http://localhost:8000/account/api/';
  
  export default {
    name: 'InvitationManager',
    data() {
      return {
        loading: false,
        receivedInvitations: [],
        sentInvitations: [],
        availableUsers: [],
        selectedUser: null,
        currentUser: null
      }
    },
    created() {
      this.verifyAuthAndInitialize();
    },
    methods: {
      async verifyAuthAndInitialize() {
        const token = localStorage.getItem('authToken');
        if (!token) {
          this.redirectToLogin();
          return;
        }
        await this.fetchData();
      },
  
      redirectToLogin() {
        localStorage.removeItem('authToken');
        this.$router.push('/login').catch(() => {});
      },
  
      async handleApiCall(endpoint, method = 'GET', data = null) {
        const token = localStorage.getItem('authToken');
        if (!token) {
          this.redirectToLogin();
          throw new Error('Token de autenticação não encontrado');
        }
  
        try {
          const config = {
            method,
            url: `${apiUrl}${endpoint}`,
            headers: {
              'Authorization': `Token ${token}`,
              'Content-Type': 'application/json',
              'X-CSRFToken': this.getCookie('csrftoken')
            },
            withCredentials: true
          };
  
          if (data) {
            config.data = data;
          }
  
          const response = await axios(config);
          return response.data;
        } catch (error) {
          console.error('API Error:', error.response || error);
          
          if (error.response?.status === 401) {
            this.redirectToLogin();
            throw new Error('Sessão expirada. Por favor faça login novamente.');
          }
          
          const errorMessage = error.response?.data?.detail || 
                              error.response?.data?.message || 
                              error.response?.data?.error || 
                              'Erro na comunicação com o servidor';
          
          this.$toast.error(errorMessage);
          throw new Error(errorMessage);
        }
      },
  
      async fetchData() {
        this.loading = true;
        try {
          await Promise.all([
            this.fetchInvitations(),
            this.fetchAvailableUsers()
          ]);
        } catch (error) {
          console.error('Error in fetchData:', error);
        } finally {
          this.loading = false;
        }
      },
  
      async fetchInvitations() {
        try {
          const data = await this.handleApiCall('invitations/');
          this.receivedInvitations = data.received || [];
          this.sentInvitations = data.sent || [];
          this.currentUser = data.current_user || null;
        } catch (error) {
          this.receivedInvitations = [];
          this.sentInvitations = [];
        }
      },
  
      async fetchAvailableUsers() {
        try {
          const data = await this.handleApiCall('users/');
          this.availableUsers = Array.isArray(data.users) ? data.users : [];
        } catch (error) {
          this.availableUsers = [];
        }
      },
  
      async sendInvitation() {
        if (!this.selectedUser) return;
        
        try {
          await this.handleApiCall(
            'invitations/send/',
            'POST',
            { recipient_email: this.selectedUser.email }
          );
          
          this.$toast.success('Convite enviado com sucesso!');
          this.selectedUser = null;
          await this.fetchData();
        } catch (error) {
          console.error('Error sending invitation:', error);
        }
      },
  
      async handleInvitation(invitationId, action) {
        try {
          await this.handleApiCall(
            `invitations/${action}/`,
            'POST',
            { invitation_id: invitationId }
          );
          
          const actionText = action === 'accept' ? 'aceito' : 'rejeitado';
          this.$toast.success(`Convite ${actionText} com sucesso!`);
          await this.fetchInvitations();
        } catch (error) {
          console.error(`Error ${action} invitation:`, error);
        }
      },
  
      formatDate(dateString) {
        if (!dateString) return '';
        try {
          return new Date(dateString).toLocaleString('pt-BR');
        } catch {
          return dateString;
        }
      },
  
      getStatusColor(status) {
        const statusColors = {
          'pending': 'warning',
          'accepted': 'success',
          'rejected': 'danger'
        };
        return statusColors[status] || 'secondary';
      },
  
      getStatusText(status) {
        const statusTexts = {
          'pending': 'Pendente',
          'accepted': 'Aceito',
          'rejected': 'Rejeitado'
        };
        return statusTexts[status] || status;
      },
  
      getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(';').shift();
        return null;
      }
    }
  }
  </script>
  
  <style scoped>
  .invitation-manager {
    padding: 20px;
  }
  
  .sidebar {
    background-color: #f8f9fa;
    padding: 20px;
    height: 100vh;
    position: sticky;
    top: 0;
  }
  
  .list-group-item {
    margin-bottom: 10px;
    border-radius: 5px;
  }
  
  .badge {
    font-size: 0.8em;
  }
  </style>