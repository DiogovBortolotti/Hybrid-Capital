<template>
<div id="webcrumbs" class="w-full">
  <Header /> 
    <div class="bg-[#282641] min-h-screen text-[#eed4ed] font-sans">

      <div class="container mx-auto py-8 px-4">
        <section id="friends" class="rounded-xl shadow-lg border border-[#615c8e] overflow-hidden">
          <div class="flex flex-col md:flex-row">
            <div class="w-full md:w-1/4 lg:w-1/5 p-4 bg-[#1e1d32] border-r border-[#615c8e]">
              <h2 class="text-2xl font-bold mb-6 text-[#a79de9]">Meus Amigos</h2>
              <div class="mb-4">
                <div class="relative">
                  <input
                    type="text"
                    class="w-full bg-[#282641] border border-[#615c8e] rounded-md p-2 pl-10 focus:outline-none focus:ring-2 focus:ring-[#a79de9] transition-all duration-300"
                    placeholder="Buscar amigos..."
                  />
                  <span class="material-symbols-outlined absolute left-3 top-2.5 text-[#615c8e]">search</span>
                </div>
              </div>
              <div class="space-y-3 max-h-[calc(100vh-250px)] overflow-y-auto scrollbar-thin scrollbar-thumb-[#615c8e] pr-1">
                <h2 class="text-xl font-bold mb-2">Convites Recebidos</h2>
                <ul class="mb-4">
                  <li 
                    v-for="convite in convites" 
                    :key="convite.id" 
                    class="request-item flex justify-between items-center bg-[#615c8e] border-l-4 border-[#a79de9] p-2 rounded-md hover:bg-[#282641] transition-colors duration-200"
                  >
                    <div class="request-info">
                      <p class="font-semibold">{{ convite.from_user.full_name }}</p>
                      <p class="text-sm text-[#a79de9]">{{ convite.from_user.email }}</p>
                    </div>
                    <div class="request-actions flex items-center gap-2">
                      <button 
                        @click="aceitarConvite(convite.id)" 
                        class="bg-green-500 hover:bg-green-600 text-white px-3 py-1 rounded-md text-sm transition-colors duration-200"
                      >
                        Aceitar
                      </button>
                      <button 
                        @click="recusarConvite(convite.id)" 
                        class="text-red-300 hover:text-red-500 transition-colors duration-200"
                      >
                        <i class="fas fa-trash-alt"></i>
                      </button>
                    </div>
                  </li>
                  <li v-if="convites.length === 0" class="no-requests text-center text-gray-400 py-2">
                    Nenhum convite pendente.
                  </li>
                </ul>

                <h2 class="text-xl font-bold mb-2">Amigos</h2>
                <ul class="mb-4 space-y-2">
                  <li v-for="amigo in amigos" :key="amigo.id" 
                     class="flex justify-between items-center bg-[#282641] hover:bg-[#615c8e] p-2 rounded-md transition-colors duration-200 cursor-pointer border-l-4 border-[#a79de9]">
                    <div class="flex items-center">
                      <div class="w-10 h-10 rounded-full bg-[#a79de9] flex items-center justify-center text-white font-bold">
                        {{ amigo.initials }}
                      </div>
                      <div class="ml-3">
                        <p class="font-semibold">{{ amigo.full_name }}</p>
                        <div class="flex items-center">
                          <span class="w-2 h-2 bg-green-500 rounded-full"></span>
                          <p class="text-xs text-[#a79de9] ml-1.5">Online</p>
                        </div>
                      </div>
                    </div>
                    <button 
                      @click="removerAmizade(amigo.id)" 
                      class="text-red-300 hover:text-red-500 transition-colors duration-200"
                    >
                      <i class="fas fa-trash-alt"></i>
                    </button>
                  </li>
                  <li v-if="amigos.length === 0" class="text-center py-4 text-[#a79de9]">
                    Você ainda não tem amigos adicionados.
                  </li>
                </ul>
              </div>
              <button
                @click="abrirModalAdicionarAmigo"
                class="w-full mt-4 bg-[#615c8e] hover:bg-[#a79de9] text-white font-semibold py-2 px-4 rounded-md transition-colors duration-300 flex items-center justify-center"
              >
                <span class="material-symbols-outlined mr-2">group_add</span> Adicionar Amigos
              </button>

              <!-- Modal de convite por e-mail -->
              <div id="inviteByEmailModal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50" v-if="showInviteByEmailModal">
                <div class="bg-[#1e1d32] rounded-lg shadow-xl w-full max-w-md border border-[#615c8e]">
                  <div class="p-6">
                    <div class="flex justify-between items-center mb-4">
                      <h3 class="text-xl font-bold text-[#a79de9]">Convidar por E-mail</h3>
                      <button @click="fecharModais" class="text-[#a79de9] hover:text-white">
                        <span class="material-symbols-outlined">close</span>
                      </button>
                    </div>
                    <div class="mb-4">
                      <label class="block text-[#a79de9] mb-2">E-mail do amigo:</label>
                      <div class="relative">
<input
  v-model="emailParaAdicionar"
  type="email"
  class="w-full bg-[#282641] border border-[#615c8e] rounded-md p-2 pl-10 focus:outline-none focus:ring-2 focus:ring-[#a79de9] transition-all duration-300"
  placeholder="exemplo@email.com"
/>

                        <span class="material-symbols-outlined absolute left-3 top-2.5 text-[#615c8e]">mail</span>
                        <div v-if="isLoading" class="absolute right-3 top-2.5">
                          <div class="animate-spin rounded-full h-5 w-5 border-b-2 border-[#a79de9]"></div>
                        </div>
                        <div 
                          v-if="emailParaAdicionar.includes('@') && usuariosFiltradosPorEmail.length > 0"
                          class="absolute z-10 mt-1 w-full bg-[#1e1d32] border border-[#615c8e] rounded-md shadow-lg max-h-60 overflow-auto"
                        >
                          <div 
                            v-for="usuario in usuariosFiltradosPorEmail" 
                            :key="usuario.id"
                            class="p-2 hover:bg-[#615c8e] cursor-pointer flex justify-between items-center"
                            @click="selecionarUsuario(usuario)"
                          >
                            <span>{{ usuario.email }}</span>
                            <span class="text-sm text-[#a79de9]">{{ usuario.full_name }}</span>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="flex space-x-3">
                      <button
                        @click="fecharModais"
                        class="flex-1 bg-[#282641] hover:bg-[#615c8e] text-[#a79de9] font-semibold py-2 px-4 rounded-md transition-colors duration-300 flex items-center justify-center"
                      >
                        <span class="material-symbols-outlined mr-2">close</span> Cancelar
                      </button>
                      <button
                        @click="enviarConvitePorEmail"
                        :disabled="!emailParaAdicionar"
                        class="flex-1 bg-[#615c8e] hover:bg-[#a79de9] text-white font-semibold py-2 px-4 rounded-md transition-colors duration-300 flex items-center justify-center disabled:opacity-50"
                      >
                        <span class="material-symbols-outlined mr-2">send</span> Enviar
                      </button>
                    </div>
                    <div class="mt-4 text-center">
                    <div v-if="notificationMessage" 
                        :class="{
                        'bg-red-500': notificationType === 'error',
                        'bg-green-500': notificationType === 'success',
                        'bg-yellow-500': notificationType === 'warning'
                        }"
                        class="fixed bottom-4 left-1/2 transform -translate-x-1/2 text-white px-4 py-2 rounded-md shadow-lg transition-all duration-300">
                    {{ notificationMessage }}
                    </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="w-full md:w-3/4 lg:w-4/5 p-6 bg-[#282641]">
              <div class="flex items-center mb-6">
                <div class="w-12 h-12 rounded-full bg-[#a79de9] flex items-center justify-center text-white text-xl font-bold mr-4">
                  JR
                </div>
                <div>
                  <h3 class="text-xl font-bold text-[#a79de9]">João Ribeiro</h3>
                  <div class="flex items-center">
                    <span class="w-2 h-2 bg-green-500 rounded-full"></span>
                    <p class="text-sm text-[#a79de9] ml-1.5">Online agora</p>
                  </div>
                </div>
                <div class="ml-auto flex space-x-2">
                  <details class="relative">
                    <summary class="list-none cursor-pointer bg-[#615c8e] hover:bg-[#a79de9] text-white p-2 rounded-md transition-colors duration-300">
                      <span class="material-symbols-outlined">more_vert</span>
                    </summary>
                    <div class="absolute right-0 mt-2 w-48 bg-[#1e1d32] border border-[#615c8e] rounded-md shadow-lg z-10">
                      <div class="py-1">
                        <a href="#" class="flex items-center px-4 py-2 hover:bg-[#615c8e] transition-colors duration-200">
                          <span class="material-symbols-outlined mr-2">person_off</span>
                          Bloquear Amigo
                        </a>
                        <a href="#" class="flex items-center px-4 py-2 hover:bg-[#615c8e] transition-colors duration-200">
                          <span class="material-symbols-outlined mr-2">person_remove</span>
                          Remover Amigo
                        </a>
                        <a href="#" class="flex items-center px-4 py-2 hover:bg-red-700 text-red-400 transition-colors duration-200">
                          <span class="material-symbols-outlined mr-2">report</span>
                          Denunciar
                        </a>
                      </div>
                    </div>
                  </details>
                </div>
              </div>
              <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                <div class="bg-[#1e1d32] rounded-lg shadow-md hover:shadow-xl transition-all duration-300 p-5 transform hover:-translate-y-1">
                  <div class="flex justify-between items-center mb-4">
                    <h3 class="text-lg font-semibold text-[#a79de9]">Informações Pessoais</h3>
                    <span class="material-symbols-outlined text-[#615c8e]">person</span>
                  </div>
                  <ul class="space-y-3">
                    <li class="flex items-start">
                      <span class="material-symbols-outlined text-[#615c8e] mr-2 mt-0.5">mail</span>
                      <div>
                        <p class="text-sm text-[#a79de9]">Email</p>
                        <p>joao.ribeiro@email.com</p>
                      </div>
                    </li>
                    <li class="flex items-start">
                      <span class="material-symbols-outlined text-[#615c8e] mr-2 mt-0.5">today</span>
                      <div>
                        <p class="text-sm text-[#a79de9]">Membro desde</p>
                        <p>01/01/2023</p>
                      </div>
                    </li>
                    <li class="flex items-start">
                      <span class="material-symbols-outlined text-[#615c8e] mr-2 mt-0.5">today</span>
                      <div>
                        <p class="text-sm text-[#a79de9]">Ultimo Acesso</p>
                        <p>01/01/2024</p>
                      </div>
                    </li>
                  </ul>
                </div>
                <div class="bg-[#1e1d32] rounded-lg shadow-md hover:shadow-xl transition-all duration-300 p-5 transform hover:-translate-y-1">
                  <div class="flex justify-between items-center mb-4">
                    <h3 class="text-lg font-semibold text-[#a79de9]">Preferências de Investimento</h3>
                    <span class="material-symbols-outlined text-[#615c8e]">analytics</span>
                  </div>
                  <ul class="space-y-3">
                    <li class="flex items-center">
                      <div class="w-full">
                        <div class="flex justify-between mb-1">
                          <span class="text-sm text-[#a79de9]">Ações</span>
                          <span>65%</span>
                        </div>
                        <div class="w-full bg-[#282641] h-2 rounded-full">
                          <div class="bg-[#a79de9] h-2 rounded-full" style="width: 65%"></div>
                        </div>
                      </div>
                    </li>
                    <li class="flex items-center">
                      <div class="w-full">
                        <div class="flex justify-between mb-1">
                          <span class="text-sm text-[#a79de9]">FIIs</span>
                          <span>25%</span>
                        </div>
                        <div class="w-full bg-[#282641] h-2 rounded-full">
                          <div class="bg-[#a79de9] h-2 rounded-full" style="width: 25%"></div>
                        </div>
                      </div>
                    </li>
                    <li class="flex items-center">
                      <div class="w-full">
                        <div class="flex justify-between mb-1">
                          <span class="text-sm text-[#a79de9]">Crypto</span>
                          <span>10%</span>
                        </div>
                        <div class="w-full bg-[#282641] h-2 rounded-full">
                          <div class="bg-[#a79de9] h-2 rounded-full" style="width: 10%"></div>
                        </div>
                      </div>
                    </li>
                  </ul>
                </div>
                <div class="bg-[#1e1d32] rounded-lg shadow-md hover:shadow-xl transition-all duration-300 p-5 transform hover:-translate-y-1">
                  <div class="flex justify-between items-center mb-4">
                    <h3 class="text-lg font-semibold text-[#a79de9]">Últimas Atividades</h3>
                    <span class="material-symbols-outlined text-[#615c8e]">history</span>
                  </div>
                  <ul class="space-y-3">
                    <li class="flex items-start">
                      <div class="p-1.5 bg-[#615c8e] rounded-md mr-3">
                        <span class="material-symbols-outlined text-sm">add_circle</span>
                      </div>
                      <div>
                        <p class="text-sm">Comprou PETR4</p>
                        <p class="text-xs text-[#a79de9]">Hoje, 14:30</p>
                      </div>
                    </li>
                    <li class="flex items-start">
                      <div class="p-1.5 bg-[#615c8e] rounded-md mr-3">
                        <span class="material-symbols-outlined text-sm">trending_up</span>
                      </div>
                      <div>
                        <p class="text-sm">Atualizou portfólio</p>
                        <p class="text-xs text-[#a79de9]">Ontem, 19:15</p>
                      </div>
                    </li>
                    <li class="flex items-start">
                      <div class="p-1.5 bg-[#615c8e] rounded-md mr-3">
                        <span class="material-symbols-outlined text-sm">savings</span>
                      </div>
                      <div>
                        <p class="text-sm">Recebeu dividendos</p>
                        <p class="text-xs text-[#a79de9]">16/05, 08:45</p>
                      </div>
                    </li>
                  </ul>
                </div>
              </div>
              <div class="mt-8">
                <div class="flex items-center justify-between mb-4">
                  <h3 class="text-xl font-bold text-[#a79de9]">Portfólio</h3>
                </div>
                <div class="bg-[#1e1d32] rounded-lg shadow-md p-5">
                  <div class="mb-6">
                    <div class="flex justify-between mb-2">
                      <span class="text-[#a79de9]">Valor Total</span>
                      <span class="font-bold">R$ 87.325,48</span>
                    </div>
                    <div class="w-full bg-[#282641] h-2 rounded-full">
                      <div class="bg-gradient-to-r from-[#615c8e] to-[#a79de9] h-2 rounded-full w-full"></div>
                    </div>
                  </div>
                  <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
                    <div class="bg-[#282641] p-3 rounded-md">
                      <div class="flex items-center justify-between">
                        <span class="text-sm text-[#a79de9]">Rentabilidade</span>
                        <span class="text-green-400 font-semibold">+12.4%</span>
                      </div>
                    </div>
                    <div class="bg-[#282641] p-3 rounded-md">
                      <div class="flex items-center justify-between">
                        <span class="text-sm text-[#a79de9]">Dividendos</span>
                        <span class="font-semibold">R$ 452,78</span>
                      </div>
                    </div>
                    <div class="bg-[#282641] p-3 rounded-md">
                      <div class="flex items-center justify-between">
                        <span class="text-sm text-[#a79de9]">Ações</span>
                        <span class="font-semibold">14</span>
                      </div>
                    </div>
                  </div>
                  <h4 class="text-lg font-semibold text-[#a79de9] mb-3">Top 5 Ações</h4>
                  <div class="space-y-2">
                    <div class="flex items-center justify-between p-2 hover:bg-[#282641] rounded-md transition-colors duration-200">
                      <div class="flex items-center">
                        <div class="w-8 h-8 rounded bg-blue-600 flex items-center justify-center text-white font-bold text-xs mr-3">
                          VALE3
                        </div>
                        <span>Vale S.A.</span>
                      </div>
                      <div class="text-right">
                        <p class="font-semibold">R$ 14.823,45</p>
                        <p class="text-green-400 text-sm">+2.3%</p>
                      </div>
                    </div>
                    <div class="flex items-center justify-between p-2 hover:bg-[#282641] rounded-md transition-colors duration-200">
                      <div class="flex items-center">
                        <div class="w-8 h-8 rounded bg-red-600 flex items-center justify-center text-white font-bold text-xs mr-3">
                          PETR4
                        </div>
                        <span>Petrobras</span>
                      </div>
                      <div class="text-right">
                        <p class="font-semibold">R$ 11.547,32</p>
                        <p class="text-red-400 text-sm">-0.8%</p>
                      </div>
                    </div>
                    <div class="flex items-center justify-between p-2 hover:bg-[#282641] rounded-md transition-colors duration-200">
                      <div class="flex items-center">
                        <div class="w-8 h-8 rounded bg-green-600 flex items-center justify-center text-white font-bold text-xs mr-3">
                          WEGE3
                        </div>
                        <span>WEG S.A.</span>
                      </div>
                      <div class="text-right">
                        <p class="font-semibold">R$ 9.876,21</p>
                        <p class="text-green-400 text-sm">+1.5%</p>
                      </div>
                    </div>
                    <div class="flex items-center justify-between p-2 hover:bg-[#282641] rounded-md transition-colors duration-200">
                      <div class="flex items-center">
                        <div class="w-8 h-8 rounded bg-purple-600 flex items-center justify-center text-white font-bold text-xs mr-3">
                          ITUB4
                        </div>
                        <span>Itaú Unibanco</span>
                      </div>
                      <div class="text-right">
                        <p class="font-semibold">R$ 8.543,62</p>
                        <p class="text-green-400 text-sm">+0.7%</p>
                      </div>
                    </div>
                    <div class="flex items-center justify-between p-2 hover:bg-[#282641] rounded-md transition-colors duration-200">
                      <div class="flex items-center">
                        <div class="w-8 h-8 rounded bg-yellow-600 flex items-center justify-center text-white font-bold text-xs mr-3">
                          BBAS3
                        </div>
                        <span>Banco do Brasil</span>
                      </div>
                      <div class="text-right">
                        <p class="font-semibold">R$ 7.209,88</p>
                        <p class="text-green-400 text-sm">+3.1%</p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import debounce from 'lodash/debounce'
import { ref, computed, onMounted, watch } from 'vue'
import Header from '../components/Header.vue';

export default {
  name: 'FriendList',

  components: {
    Header,
  },

  setup() {
    const usuarios = ref([])
    const amigos = ref([])
    const convites = ref([])
    const emailParaAdicionar = ref('')
    const currentUserId = ref(null)
    const showInviteByEmailModal = ref(false)
    const selectedUser = ref(null)
    const notificationMessage = ref('')
    const notificationType = ref('error')
    const isLoading = ref(false)

    const api = axios.create({
      baseURL: 'http://localhost:8000/account/api',
      headers: { 'Content-Type': 'application/json' }
    })

    api.interceptors.request.use(config => {
      const token = localStorage.getItem('token')
      if (token) config.headers['Authorization'] = `Token ${token}`
      return config
    }, error => Promise.reject(error))

    const showNotification = (message, type = 'error') => {
      notificationMessage.value = message
      notificationType.value = type
      setTimeout(() => {
        notificationMessage.value = ''
      }, 5000)
    }

    const carregarUsuarioAtual = async () => {
      try {
        const response = await api.get('/users')
        currentUserId.value = response.data.id
      } catch (error) {
        showNotification('Erro ao carregar dados do usuário', 'error')
      }
    }

    const carregarDados = async () => {
      try {
        const [usuariosRes, amigosRes, convitesRes] = await Promise.all([
          api.get('/users/'),
          api.get('/users/me/friends/'),
          api.get('/friend-requests/')
        ])
        usuarios.value = usuariosRes.data
        amigos.value = amigosRes.data.map(amigo => ({
          ...amigo,
          initials: amigo.full_name.split(' ').map(n => n[0]).join('').toUpperCase()
        }))
        convites.value = convitesRes.data
      } catch (error) {
        showNotification('Erro ao carregar dados', 'error')
      }
    }

    const buscarUsuariosPorEmail = async () => {
      if (!emailParaAdicionar.value.includes('@')) return
      isLoading.value = true
      try {
        const response = await api.get('/users/', { 
          params: { email: emailParaAdicionar.value }
        })
        usuarios.value = response.data
      } catch (error) {
        showNotification('Erro ao buscar usuários', 'error')
      } finally {
        isLoading.value = false
      }
    }

    const buscarUsuariosDebounced = debounce(buscarUsuariosPorEmail, 500)

    watch(emailParaAdicionar, () => {
      buscarUsuariosDebounced()
    })

    const enviarConvite = async (id) => {
      try {
        const response = await api.post('/friend-requests/', { to_user: id })
        if (response.status === 201) {
          showNotification('Convite enviado com sucesso!', 'success')
          carregarDados()
          fecharModais()
        }
      } catch (error) {
        if (error.response) {
          if (error.response.status === 400) {
            const detail = error.response.data.detail
            showNotification(detail || 'Erro ao enviar convite', 'error')
          } else {
            showNotification('Erro no servidor', 'error')
          }
        } else {
          showNotification('Erro de conexão', 'error')
        }
      }
    }

    const enviarConvitePorEmail = async () => {
      try {
        if (!emailParaAdicionar.value.includes('@')) {
          showNotification('Por favor, informe um e-mail válido', 'error')
          return
        }

        if (selectedUser.value) {
          await enviarConvite(selectedUser.value.id)
          return
        }

        const res = await api.get('/users/', {
          params: { email: emailParaAdicionar.value }
        })

        if (res.data.length === 0) {
          showNotification('Nenhum usuário encontrado com este e-mail', 'error')
          return
        }

        await enviarConvite(res.data[0].id)
      } catch (error) {
        showNotification('Erro ao buscar usuário por e-mail', 'error')
      }
    }

    const aceitarConvite = async (id) => {
      try {
        await api.post(`/friend-requests/${id}/accept/`)
        showNotification('Convite aceito com sucesso!', 'success')
        carregarDados()
      } catch (error) {
        showNotification('Erro ao aceitar convite', 'error')
      }
    }

    const recusarConvite = async (id) => {
      try {
        await api.delete(`/friend-requests/${id}/`)
        showNotification('Convite recusado', 'success')
        carregarDados()
      } catch (error) {
        showNotification('Erro ao recusar convite', 'error')
      }
    }

    const removerAmizade = async (friendId) => {
      if (confirm('Tem certeza que deseja remover esta amizade?')) {
        try {
          await api.delete(`/friend-requests/remove-friend/${friendId}/`)
          showNotification('Amizade removida com sucesso!', 'success')
          carregarDados()
        } catch (error) {
          showNotification('Erro ao remover amizade', 'error')
        }
      }
    }

    const usuariosFiltradosPorEmail = computed(() => {
      if (!emailParaAdicionar.value || !currentUserId.value) return []
      return usuarios.value.filter(user => 
        user.email.toLowerCase().includes(emailParaAdicionar.value.toLowerCase()) &&
        user.id !== currentUserId.value &&
        !amigos.value.some(amigo => amigo.id === user.id)
      )
    })

    const jaEAmigo = (userId) => {
      return amigos.value.some(amigo => amigo.id === userId)
    }

    const convitePendente = (userId) => {
      return convites.value.some(convite => convite.from_user.id === userId)
    }

    onMounted(async () => {
      await carregarUsuarioAtual()
      await carregarDados()
    })

    const abrirModalAdicionarAmigo = () => {
      showInviteByEmailModal.value = true
    }

    const fecharModais = () => {
      showInviteByEmailModal.value = false
      selectedUser.value = null
      emailParaAdicionar.value = ''
    }

    const selecionarUsuario = (usuario) => {
      selectedUser.value = usuario
      emailParaAdicionar.value = usuario.email
    }

    return {
      usuarios,
      amigos,
      convites,
      emailParaAdicionar,
      currentUserId,
      showInviteByEmailModal,
      selectedUser,
      notificationMessage,
      notificationType,
      isLoading,
      usuariosFiltradosPorEmail,
      jaEAmigo,
      convitePendente,
      carregarDados,
      buscarUsuariosPorEmail,
      enviarConvite,
      enviarConvitePorEmail,
      aceitarConvite,
      recusarConvite,
      removerAmizade,
      abrirModalAdicionarAmigo,
      fecharModais,
      selecionarUsuario
    }
  }
}
</script>


<style scoped>
    @import url(https://fonts.googleapis.com/css2?family=Lato&display=swap);
    @import url(https://fonts.googleapis.com/css2?family=Open+Sans&display=swap);
    @import url(https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200);

    @keyframes spin {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }

    .animate-spin {
        animation: spin 1s linear infinite;
    }

    /*! tailwindcss v3.4.11 | MIT License | https://tailwindcss.com*/
    *,
    :after,
    :before {
        border: 0 solid #e5e7eb;
        box-sizing: border-box;
    }
    :after,
    :before {
        --tw-content: "";
    }
    :host,
    html {
        line-height: 1.5;
        -webkit-text-size-adjust: 100%;
        font-family:
            Open Sans,
            ui-sans-serif,
            system-ui,
            sans-serif,
            Apple Color Emoji,
            Segoe UI Emoji,
            Segoe UI Symbol,
            Noto Color Emoji;
        font-feature-settings: normal;
        font-variation-settings: normal;
        -moz-tab-size: 4;
        tab-size: 4;
        -webkit-tap-highlight-color: transparent;
    }
    body {
        line-height: inherit;
        margin: 0;
    }
    hr {
        border-top-width: 1px;
        color: inherit;
        height: 0;
    }
    abbr:where([title]) {
        text-decoration: underline dotted;
    }
    h1,
    h2,
    h3,
    h4,
    h5,
    h6 {
        font-size: inherit;
        font-weight: inherit;
    }
    a {
        color: inherit;
        text-decoration: inherit;
    }
    b,
    strong {
        font-weight: bolder;
    }
    code,
    kbd,
    pre,
    samp {
        font-family:
            ui-monospace,
            SFMono-Regular,
            Menlo,
            Monaco,
            Consolas,
            Liberation Mono,
            Courier New,
            monospace;
        font-feature-settings: normal;
        font-size: 1em;
        font-variation-settings: normal;
    }
    small {
        font-size: 80%;
    }
    sub,
    sup {
        font-size: 75%;
        line-height: 0;
        position: relative;
        vertical-align: baseline;
    }
    sub {
        bottom: -0.25em;
    }
    sup {
        top: -0.5em;
    }
    table {
        border-collapse: collapse;
        border-color: inherit;
        text-indent: 0;
    }
    button,
    input,
    optgroup,
    select,
    textarea {
        color: inherit;
        font-family: inherit;
        font-feature-settings: inherit;
        font-size: 100%;
        font-variation-settings: inherit;
        font-weight: inherit;
        letter-spacing: inherit;
        line-height: inherit;
        margin: 0;
        padding: 0;
    }
    button,
    select {
        text-transform: none;
    }
    button,
    input:where([type="button"]),
    input:where([type="reset"]),
    input:where([type="submit"]) {
        -webkit-appearance: button;
        background-color: transparent;
        background-image: none;
    }
    :-moz-focusring {
        outline: auto;
    }
    :-moz-ui-invalid {
        box-shadow: none;
    }
    progress {
        vertical-align: baseline;
    }
    ::-webkit-inner-spin-button,
    ::-webkit-outer-spin-button {
        height: auto;
    }
    [type="search"] {
        -webkit-appearance: textfield;
        outline-offset: -2px;
    }
    ::-webkit-search-decoration {
        -webkit-appearance: none;
    }
    ::-webkit-file-upload-button {
        -webkit-appearance: button;
        font: inherit;
    }
    summary {
        display: list-item;
    }
    blockquote,
    dd,
    dl,
    figure,
    h1,
    h2,
    h3,
    h4,
    h5,
    h6,
    hr,
    p,
    pre {
        margin: 0;
    }
    fieldset {
        margin: 0;
    }
    fieldset,
    legend {
        padding: 0;
    }
    menu,
    ol,
    ul {
        list-style: none;
        margin: 0;
        padding: 0;
    }
    dialog {
        padding: 0;
    }
    textarea {
        resize: vertical;
    }
    input::placeholder,
    textarea::placeholder {
        color: #9ca3af;
        opacity: 1;
    }
    [role="button"],
    button {
        cursor: pointer;
    }
    :disabled {
        cursor: default;
    }
    audio,
    canvas,
    embed,
    iframe,
    img,
    object,
    svg,
    video {
        display: block;
        vertical-align: middle;
    }
    img,
    video {
        height: auto;
        max-width: 100%;
    }
    [hidden] {
        display: none;
    }
    *,
    :after,
    :before {
        --tw-border-spacing-x: 0;
        --tw-border-spacing-y: 0;
        --tw-translate-x: 0;
        --tw-translate-y: 0;
        --tw-rotate: 0;
        --tw-skew-x: 0;
        --tw-skew-y: 0;
        --tw-scale-x: 1;
        --tw-scale-y: 1;
        --tw-pan-x: ;
        --tw-pan-y: ;
        --tw-pinch-zoom: ;
        --tw-scroll-snap-strictness: proximity;
        --tw-gradient-from-position: ;
        --tw-gradient-via-position: ;
        --tw-gradient-to-position: ;
        --tw-ordinal: ;
        --tw-slashed-zero: ;
        --tw-numeric-figure: ;
        --tw-numeric-spacing: ;
        --tw-numeric-fraction: ;
        --tw-ring-inset: ;
        --tw-ring-offset-width: 0px;
        --tw-ring-offset-color: #fff;
        --tw-ring-color: rgba(59, 130, 246, 0.5);
        --tw-ring-offset-shadow: 0 0 #0000;
        --tw-ring-shadow: 0 0 #0000;
        --tw-shadow: 0 0 #0000;
        --tw-shadow-colored: 0 0 #0000;
        --tw-blur: ;
        --tw-brightness: ;
        --tw-contrast: ;
        --tw-grayscale: ;
        --tw-hue-rotate: ;
        --tw-invert: ;
        --tw-saturate: ;
        --tw-sepia: ;
        --tw-drop-shadow: ;
        --tw-backdrop-blur: ;
        --tw-backdrop-brightness: ;
        --tw-backdrop-contrast: ;
        --tw-backdrop-grayscale: ;
        --tw-backdrop-hue-rotate: ;
        --tw-backdrop-invert: ;
        --tw-backdrop-opacity: ;
        --tw-backdrop-saturate: ;
        --tw-backdrop-sepia: ;
        --tw-contain-size: ;
        --tw-contain-layout: ;
        --tw-contain-paint: ;
        --tw-contain-style: ;
    }
    ::backdrop {
        --tw-border-spacing-x: 0;
        --tw-border-spacing-y: 0;
        --tw-translate-x: 0;
        --tw-translate-y: 0;
        --tw-rotate: 0;
        --tw-skew-x: 0;
        --tw-skew-y: 0;
        --tw-scale-x: 1;
        --tw-scale-y: 1;
        --tw-pan-x: ;
        --tw-pan-y: ;
        --tw-pinch-zoom: ;
        --tw-scroll-snap-strictness: proximity;
        --tw-gradient-from-position: ;
        --tw-gradient-via-position: ;
        --tw-gradient-to-position: ;
        --tw-ordinal: ;
        --tw-slashed-zero: ;
        --tw-numeric-figure: ;
        --tw-numeric-spacing: ;
        --tw-numeric-fraction: ;
        --tw-ring-inset: ;
        --tw-ring-offset-width: 0px;
        --tw-ring-offset-color: #fff;
        --tw-ring-color: rgba(59, 130, 246, 0.5);
        --tw-ring-offset-shadow: 0 0 #0000;
        --tw-ring-shadow: 0 0 #0000;
        --tw-shadow: 0 0 #0000;
        --tw-shadow-colored: 0 0 #0000;
        --tw-blur: ;
        --tw-brightness: ;
        --tw-contrast: ;
        --tw-grayscale: ;
        --tw-hue-rotate: ;
        --tw-invert: ;
        --tw-saturate: ;
        --tw-sepia: ;
        --tw-drop-shadow: ;
        --tw-backdrop-blur: ;
        --tw-backdrop-brightness: ;
        --tw-backdrop-contrast: ;
        --tw-backdrop-grayscale: ;
        --tw-backdrop-hue-rotate: ;
        --tw-backdrop-invert: ;
        --tw-backdrop-opacity: ;
        --tw-backdrop-saturate: ;
        --tw-backdrop-sepia: ;
        --tw-contain-size: ;
        --tw-contain-layout: ;
        --tw-contain-paint: ;
        --tw-contain-style: ;
    }
    .container {
        width: 100%;
    }
    @media (min-width: 640px) {
        .container {
            max-width: 640px;
        }
    }
    @media (min-width: 768px) {
        .container {
            max-width: 768px;
        }
    }
    @media (min-width: 1024px) {
        .container {
            max-width: 1024px;
        }
    }
    @media (min-width: 1280px) {
        .container {
            max-width: 1280px;
        }
    }
    @media (min-width: 1536px) {
        .container {
            max-width: 1536px;
        }
    }
    #webcrumbs .absolute {
        position: absolute;
    }
    #webcrumbs .relative {
        position: relative;
    }
    #webcrumbs .left-3 {
        left: 12px;
    }
    #webcrumbs .right-0 {
        right: 0;
    }
    #webcrumbs .top-2\.5 {
        top: 10px;
    }
    #webcrumbs .z-10 {
        z-index: 10;
    }
    #webcrumbs .mx-auto {
        margin-left: auto;
        margin-right: auto;
    }
    #webcrumbs .mb-1 {
        margin-bottom: 4px;
    }
    #webcrumbs .mb-2 {
        margin-bottom: 8px;
    }
    #webcrumbs .mb-3 {
        margin-bottom: 12px;
    }
    #webcrumbs .mb-4 {
        margin-bottom: 16px;
    }
    #webcrumbs .mb-6 {
        margin-bottom: 24px;
    }
    #webcrumbs .ml-1\.5 {
        margin-left: 6px;
    }
    #webcrumbs .ml-3 {
        margin-left: 12px;
    }
    #webcrumbs .ml-auto {
        margin-left: auto;
    }
    #webcrumbs .mr-1 {
        margin-right: 4px;
    }
    #webcrumbs .mr-2 {
        margin-right: 8px;
    }
    #webcrumbs .mr-3 {
        margin-right: 12px;
    }
    #webcrumbs .mr-4 {
        margin-right: 16px;
    }
    #webcrumbs .mt-0\.5 {
        margin-top: 2px;
    }
    #webcrumbs .mt-2 {
        margin-top: 8px;
    }
    #webcrumbs .mt-4 {
        margin-top: 16px;
    }
    #webcrumbs .mt-8 {
        margin-top: 32px;
    }
    #webcrumbs .flex {
        display: flex;
    }
    #webcrumbs .grid {
        display: grid;
    }
    #webcrumbs .hidden {
        display: none;
    }
    #webcrumbs .h-10 {
        height: 40px;
    }
    #webcrumbs .h-12 {
        height: 48px;
    }
    #webcrumbs .h-2 {
        height: 8px;
    }
    #webcrumbs .h-8 {
        height: 32px;
    }
    #webcrumbs .max-h-\[calc\(100vh-250px\)\] {
        max-height: calc(100vh - 250px);
    }
    #webcrumbs .min-h-screen {
        min-height: 100vh;
    }
    #webcrumbs .w-10 {
        width: 40px;
    }
    #webcrumbs .w-12 {
        width: 48px;
    }
    #webcrumbs .w-2 {
        width: 8px;
    }
    #webcrumbs .w-48 {
        width: 192px;
    }
    #webcrumbs .w-8 {
        width: 32px;
    }
    #webcrumbs .w-full {
        width: 100%;
    }
    #webcrumbs .transform {
        transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate))
            skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
    }
    #webcrumbs .cursor-pointer {
        cursor: pointer;
    }
    #webcrumbs .list-none {
        list-style-type: none;
    }
    #webcrumbs .grid-cols-1 {
        grid-template-columns: repeat(1, minmax(0, 1fr));
    }
    #webcrumbs .flex-row {
        flex-direction: row;
    }
    #webcrumbs .flex-col {
        flex-direction: column;
    }
    #webcrumbs .items-start {
        align-items: flex-start;
    }
    #webcrumbs .items-center {
        align-items: center;
    }
    #webcrumbs .justify-center {
        justify-content: center;
    }
    #webcrumbs .justify-between {
        justify-content: space-between;
    }
    #webcrumbs .gap-4 {
        gap: 16px;
    }
    #webcrumbs .gap-6 {
        gap: 24px;
    }
    #webcrumbs :is(.space-x-2 > :not([hidden]) ~ :not([hidden])) {
        --tw-space-x-reverse: 0;
        margin-left: calc(8px * (1 - var(--tw-space-x-reverse)));
        margin-right: calc(8px * var(--tw-space-x-reverse));
    }
    #webcrumbs :is(.space-x-6 > :not([hidden]) ~ :not([hidden])) {
        --tw-space-x-reverse: 0;
        margin-left: calc(24px * (1 - var(--tw-space-x-reverse)));
        margin-right: calc(24px * var(--tw-space-x-reverse));
    }
    #webcrumbs :is(.space-y-2 > :not([hidden]) ~ :not([hidden])) {
        --tw-space-y-reverse: 0;
        margin-bottom: calc(8px * var(--tw-space-y-reverse));
        margin-top: calc(8px * (1 - var(--tw-space-y-reverse)));
    }
    #webcrumbs :is(.space-y-3 > :not([hidden]) ~ :not([hidden])) {
        --tw-space-y-reverse: 0;
        margin-bottom: calc(12px * var(--tw-space-y-reverse));
        margin-top: calc(12px * (1 - var(--tw-space-y-reverse)));
    }
    #webcrumbs .overflow-hidden {
        overflow: hidden;
    }
    #webcrumbs .overflow-y-auto {
        overflow-y: auto;
    }
    #webcrumbs .rounded {
        border-radius: 12px;
    }
    #webcrumbs .rounded-full {
        border-radius: 9999px;
    }
    #webcrumbs .rounded-lg {
        border-radius: 24px;
    }
    #webcrumbs .rounded-md {
        border-radius: 18px;
    }
    #webcrumbs .rounded-xl {
        border-radius: 36px;
    }
    #webcrumbs .border {
        border-width: 1px;
    }
    #webcrumbs .border-b-2 {
        border-bottom-width: 2px;
    }
    #webcrumbs .border-l-4 {
        border-left-width: 4px;
    }
    #webcrumbs .border-r {
        border-right-width: 1px;
    }
    #webcrumbs .border-\[\#615c8e\] {
        --tw-border-opacity: 1;
        border-color: rgb(97 92 142 / var(--tw-border-opacity));
    }
    #webcrumbs .border-\[\#a79de9\] {
        --tw-border-opacity: 1;
        border-color: rgb(167 157 233 / var(--tw-border-opacity));
    }
    #webcrumbs .bg-\[\#120907\] {
        --tw-bg-opacity: 1;
        background-color: rgb(18 9 7 / var(--tw-bg-opacity));
    }
    #webcrumbs .bg-\[\#1e1d32\] {
        --tw-bg-opacity: 1;
        background-color: rgb(30 29 50 / var(--tw-bg-opacity));
    }
    #webcrumbs .bg-\[\#282641\] {
        --tw-bg-opacity: 1;
        background-color: rgb(40 38 65 / var(--tw-bg-opacity));
    }
    #webcrumbs .bg-\[\#615c8e\] {
        --tw-bg-opacity: 1;
        background-color: rgb(97 92 142 / var(--tw-bg-opacity));
    }
    #webcrumbs .bg-\[\#a79de9\] {
        --tw-bg-opacity: 1;
        background-color: rgb(167 157 233 / var(--tw-bg-opacity));
    }
    #webcrumbs .bg-blue-600 {
        --tw-bg-opacity: 1;
        background-color: rgb(37 99 235 / var(--tw-bg-opacity));
    }
    #webcrumbs .bg-gray-400 {
        --tw-bg-opacity: 1;
        background-color: rgb(156 163 175 / var(--tw-bg-opacity));
    }
    #webcrumbs .bg-green-500 {
        --tw-bg-opacity: 1;
        background-color: rgb(34 197 94 / var(--tw-bg-opacity));
    }
    #webcrumbs .bg-green-600 {
        --tw-bg-opacity: 1;
        background-color: rgb(22 163 74 / var(--tw-bg-opacity));
    }
    #webcrumbs .bg-purple-600 {
        --tw-bg-opacity: 1;
        background-color: rgb(147 51 234 / var(--tw-bg-opacity));
    }
    #webcrumbs .bg-red-600 {
        --tw-bg-opacity: 1;
        background-color: rgb(220 38 38 / var(--tw-bg-opacity));
    }
    #webcrumbs .bg-gradient-to-r {
        background-image: linear-gradient(to right, var(--tw-gradient-stops));
    }
    #webcrumbs .from-\[\#615c8e\] {
        --tw-gradient-from: #615c8e var(--tw-gradient-from-position);
        --tw-gradient-to: rgba(97, 92, 142, 0) var(--tw-gradient-to-position);
        --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to);
    }
    #webcrumbs .to-\[\#a79de9\] {
        --tw-gradient-to: #a79de9 var(--tw-gradient-to-position);
    }
    #webcrumbs .p-1\.5 {
        padding: 6px;
    }
    #webcrumbs .p-2 {
        padding: 8px;
    }
    #webcrumbs .p-3 {
        padding: 12px;
    }
    #webcrumbs .p-4 {
        padding: 16px;
    }
    #webcrumbs .p-5 {
        padding: 20px;
    }
    #webcrumbs .p-6 {
        padding: 24px;
    }
    #webcrumbs .px-3 {
        padding-left: 12px;
        padding-right: 12px;
    }
    #webcrumbs .px-4 {
        padding-left: 16px;
        padding-right: 16px;
    }
    #webcrumbs .px-6 {
        padding-left: 24px;
        padding-right: 24px;
    }
    #webcrumbs .py-1 {
        padding-bottom: 4px;
        padding-top: 4px;
    }
    #webcrumbs .py-1\.5 {
        padding-bottom: 6px;
        padding-top: 6px;
    }
    #webcrumbs .py-2 {
        padding-bottom: 8px;
        padding-top: 8px;
    }
    #webcrumbs .py-4 {
        padding-bottom: 16px;
        padding-top: 16px;
    }
    #webcrumbs .py-8 {
        padding-bottom: 32px;
        padding-top: 32px;
    }
    #webcrumbs .pl-10 {
        padding-left: 40px;
    }
    #webcrumbs .pr-1 {
        padding-right: 4px;
    }
    #webcrumbs .text-right {
        text-align: right;
    }
    #webcrumbs .font-sans {
        font-family:
            Open Sans,
            ui-sans-serif,
            system-ui,
            sans-serif,
            Apple Color Emoji,
            Segoe UI Emoji,
            Segoe UI Symbol,
            Noto Color Emoji;
    }
    #webcrumbs .text-2xl {
        font-size: 24px;
        line-height: 31.200000000000003px;
    }
    #webcrumbs .text-lg {
        font-size: 18px;
        line-height: 27px;
    }
    #webcrumbs .text-sm {
        font-size: 14px;
        line-height: 21px;
    }
    #webcrumbs .text-xl {
        font-size: 20px;
        line-height: 28px;
    }
    #webcrumbs .text-xs {
        font-size: 12px;
        line-height: 19.200000000000003px;
    }
    #webcrumbs .font-bold {
        font-weight: 700;
    }
    #webcrumbs .font-semibold {
        font-weight: 600;
    }
    #webcrumbs .text-\[\#615c8e\] {
        --tw-text-opacity: 1;
        color: rgb(97 92 142 / var(--tw-text-opacity));
    }
    #webcrumbs .text-\[\#a79de9\] {
        --tw-text-opacity: 1;
        color: rgb(167 157 233 / var(--tw-text-opacity));
    }
    #webcrumbs .text-\[\#eed4ed\] {
        --tw-text-opacity: 1;
        color: rgb(238 212 237 / var(--tw-text-opacity));
    }
    #webcrumbs .text-green-400 {
        --tw-text-opacity: 1;
        color: rgb(74 222 128 / var(--tw-text-opacity));
    }
    #webcrumbs .text-red-400 {
        --tw-text-opacity: 1;
        color: rgb(248 113 113 / var(--tw-text-opacity));
    }
    #webcrumbs .text-white {
        --tw-text-opacity: 1;
        color: rgb(255 255 255 / var(--tw-text-opacity));
    }
    #webcrumbs .shadow-lg {
        --tw-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.1);
        --tw-shadow-colored: 0 10px 15px -3px var(--tw-shadow-color), 0 4px 6px -4px var(--tw-shadow-color);
    }
    #webcrumbs .shadow-lg,
    #webcrumbs .shadow-md {
        box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
    }
    #webcrumbs .shadow-md {
        --tw-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.1);
        --tw-shadow-colored: 0 4px 6px -1px var(--tw-shadow-color), 0 2px 4px -2px var(--tw-shadow-color);
    }
    #webcrumbs .transition-all {
        transition-duration: 0.15s;
        transition-property: all;
        transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
    }
    #webcrumbs .transition-colors {
        transition-duration: 0.15s;
        transition-property: color, background-color, border-color, text-decoration-color, fill, stroke;
        transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
    }
    #webcrumbs .duration-200 {
        transition-duration: 0.2s;
    }
    #webcrumbs .duration-300 {
        transition-duration: 0.3s;
    }
    #webcrumbs {
        font-family: Open Sans !important;
        font-size: 16px !important;
    }
    #webcrumbs .hover\:-translate-y-1:hover {
        --tw-translate-y: -4px;
        transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate))
            skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
    }
    #webcrumbs .hover\:bg-\[\#282641\]:hover {
        --tw-bg-opacity: 1;
        background-color: rgb(40 38 65 / var(--tw-bg-opacity));
    }
    #webcrumbs .hover\:bg-\[\#615c8e\]:hover {
        --tw-bg-opacity: 1;
        background-color: rgb(97 92 142 / var(--tw-bg-opacity));
    }
    #webcrumbs .hover\:bg-\[\#a79de9\]:hover {
        --tw-bg-opacity: 1;
        background-color: rgb(167 157 233 / var(--tw-bg-opacity));
    }
    #webcrumbs .hover\:bg-red-700:hover {
        --tw-bg-opacity: 1;
        background-color: rgb(185 28 28 / var(--tw-bg-opacity));
    }
    #webcrumbs .hover\:text-\[\#a79de9\]:hover {
        --tw-text-opacity: 1;
        color: rgb(167 157 233 / var(--tw-text-opacity));
    }
    #webcrumbs .hover\:shadow-xl:hover {
        --tw-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1);
        --tw-shadow-colored: 0 20px 25px -5px var(--tw-shadow-color), 0 8px 10px -6px var(--tw-shadow-color);
        box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
    }
    #webcrumbs .focus\:outline-none:focus {
        outline: 2px solid transparent;
        outline-offset: 2px;
    }
    #webcrumbs .focus\:ring-2:focus {
        --tw-ring-offset-shadow: var(--tw-ring-inset) 0 0 0 var(--tw-ring-offset-width)
            var(--tw-ring-offset-color);
        --tw-ring-shadow: var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width))
            var(--tw-ring-color);
        box-shadow: var(--tw-ring-offset-shadow), var(--tw-ring-shadow), var(--tw-shadow, 0 0 #0000);
    }
    #webcrumbs .focus\:ring-\[\#a79de9\]:focus {
        --tw-ring-opacity: 1;
        --tw-ring-color: rgb(167 157 233 / var(--tw-ring-opacity));
    }
    @media (min-width: 768px) {
        #webcrumbs .md\:flex {
            display: flex;
        }
        #webcrumbs .md\:hidden {
            display: none;
        }
        #webcrumbs .md\:w-1\/4 {
            width: 25%;
        }
        #webcrumbs .md\:w-3\/4 {
            width: 75%;
        }
        #webcrumbs .md\:grid-cols-2 {
            grid-template-columns: repeat(2, minmax(0, 1fr));
        }
        #webcrumbs .md\:grid-cols-3 {
            grid-template-columns: repeat(3, minmax(0, 1fr));
        }
        #webcrumbs .md\:flex-row {
            flex-direction: row;
        }
    }
    @media (min-width: 1024px) {
        #webcrumbs .lg\:w-1\/5 {
            width: 20%;
        }
        #webcrumbs .lg\:w-4\/5 {
            width: 80%;
        }
        #webcrumbs .lg\:grid-cols-3 {
            grid-template-columns: repeat(3, minmax(0, 1fr));
        }
    }

    /* Estilos adicionais para os modais */
    #webcrumbs .fixed {
        position: fixed;
    }
    #webcrumbs .inset-0 {
        inset: 0;
    }
    #webcrumbs .z-50 {
        z-index: 50;
    }
    #webcrumbs .max-w-md {
        max-width: 28rem;
    }
    #webcrumbs .max-h-64 {
        max-height: 16rem;
    }
    #webcrumbs .bg-opacity-50 {
        --tw-bg-opacity: 0.5;
    }
    #webcrumbs .disabled\:opacity-50:disabled {
        opacity: 0.5;
    }
    #webcrumbs .backdrop-blur-sm {
        backdrop-filter: blur(4px);
    }

    body {
        line-height: inherit;
        padding: 24px;
        display: flex;
        flex-direction: column;
        min-width: 100vw;
        min-height: 100vh;
        align-items: center;
        justify-content: center;
        background: linear-gradient(135deg, #ffffff, #d4d4d4);
    }
</style>