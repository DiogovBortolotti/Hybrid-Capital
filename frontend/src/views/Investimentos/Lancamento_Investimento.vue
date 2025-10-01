<template>
  <div id="webcrumbs">

      <Header />
    <div class="min-h-screen bg-gray-50 p-4 md:p-6 lg:p-8">


      <!-- Main Content -->
      <main class="container mx-auto">
        <div class="bg-white rounded-xl shadow-lg overflow-hidden">
          <!-- Header do Formulário -->
          <div class="p-6 bg-gradient-to-r from-primary-600 to-primary-800 text-white">
            <h1 class="text-2xl font-bold mb-2">Gerenciador de Investimentos</h1>
            <p class="opacity-90">Registre, acompanhe e gerencie seus investimentos e rendimentos</p>
          </div>
          
          <div class="p-6">
            <!-- Formulário de Adição -->
            <div class="mb-8">
              <h2 class="text-xl font-semibold mb-4">{{ tituloFormulario }}</h2>
              <form @submit.prevent="submitForm" class="space-y-6">
                <!-- Informações Básicas -->
                <div class="bg-gray-50 p-4 rounded-lg shadow-sm hover:shadow-md transition-shadow duration-300">
                  <h3 class="text-lg font-semibold mb-4">Informações Básicas</h3>
                  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                    <!-- Tipo de Investimento -->
                    <div>
                      <label class="block text-sm font-medium text-gray-700 mb-1">Tipo de Investimento *</label>
                      <select v-model="formData.tipo" class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 transition-all" required>
                        <option value="">Selecione</option>
                        <option value="ACAO">Ação</option>
                        <option value="FII">Fundo Imobiliário (FII)</option>
                        <option value="CRIPTO">Criptomoeda</option>
                        <option value="TESOURO">Tesouro/Selic</option>
                        <option value="POUPANCA">Poupança</option>
                        <option value="CDB">CDB</option>
                        <option value="LCI">LCI</option>
                        <option value="LCA">LCA</option>
                      </select>
                    </div>
                    
                    <!-- Instituição -->
                    <div>
                      <label class="block text-sm font-medium text-gray-700 mb-1">Instituição *</label>
                      <input v-model="formData.instituicao" type="text" class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 transition-all" placeholder="Nome da corretora/banco" required>
                    </div>
                    
                    <!-- Nome do Ativo -->
                    <div>
                      <label class="block text-sm font-medium text-gray-700 mb-1">Nome do Ativo *</label>
                      <input v-model="formData.nome_patrimonio" type="text" class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 transition-all" placeholder="Ex: PETR4, XPLG11, Bitcoin" required>
                    </div>
                    
                    <!-- Valor da Cota -->
                    <div>
                      <label class="block text-sm font-medium text-gray-700 mb-1">Valor da Cota/Unidade *</label>
                      <input v-model="formData.valor_cota" type="number" step="0.01" min="0.01" class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 transition-all" placeholder="0,00" required>
                    </div>
                    
                    <!-- Quantidade -->
                    <div>
                      <label class="block text-sm font-medium text-gray-700 mb-1">Quantidade *</label>
                      <input v-model="formData.unidades" type="number" step="0.000001" min="0.000001" class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 transition-all" placeholder="0" required>
                    </div>
                    
                    <!-- Data de Compra -->
                    <div>
                      <label class="block text-sm font-medium text-gray-700 mb-1">Data da Compra *</label>
                      <input v-model="formData.data_compra" type="date" class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 transition-all" required>
                    </div>
                  </div>
                </div>
                
                <!-- Informações de Moeda -->
                <div class="bg-gray-50 p-4 rounded-lg shadow-sm hover:shadow-md transition-shadow duration-300">
                  <h3 class="text-lg font-semibold mb-4">Informações de Moeda</h3>
                  <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <!-- Moeda -->
                    <div>
                      <label class="block text-sm font-medium text-gray-700 mb-1">Moeda *</label>
                      <select v-model="formData.moeda" class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 transition-all" required>
                        <option value="BRL">Real (BRL)</option>
                        <option value="USD">Dólar (USD)</option>
                      </select>
                    </div>
                    
                    <!-- Cotação Dólar (condicional) -->
                    <div v-if="formData.moeda === 'USD'">
                      <label class="block text-sm font-medium text-gray-700 mb-1">Cotação do Dólar Pago</label>
                      <div class="flex">
                        <span class="inline-flex items-center px-3 border border-r-0 border-gray-300 bg-gray-100 text-gray-700 rounded-l-md">
                          <span class="material-symbols-outlined text-sm">currency_exchange</span>
                        </span>
                        <input v-model="formData.cotacao_dolar_pago" type="number" step="0.0001" min="0.0001" class="flex-1 px-3 py-2 border border-gray-300 rounded-r-md focus:outline-none focus:ring-2 focus:ring-primary-500 transition-all" placeholder="Taxa de câmbio">
                      </div>
                    </div>
                  </div>
                </div>
                
                <!-- Rendimento -->
                <div class="bg-gray-50 p-4 rounded-lg shadow-sm hover:shadow-md transition-shadow duration-300">
                  <h3 class="text-lg font-semibold mb-4">Rendimento (para Renda Fixa)</h3>
                  <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                    <!-- Taxa Anual -->
                    <div>
                      <label class="block text-sm font-medium text-gray-700 mb-1">Taxa Anual (%)</label>
                      <input v-model="formData.taxa_anual" type="number" step="0.01" min="0" class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 transition-all" placeholder="0,00%">
                    </div>
                    
                    <!-- Aporte Mensal -->
                    <div>
                      <label class="block text-sm font-medium text-gray-700 mb-1">Aporte Mensal (R$)</label>
                      <input v-model="formData.aporte_mensal" type="number" step="0.01" min="0" class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 transition-all" placeholder="0,00">
                    </div>
                    
                    <!-- Prazo -->
                    <div>
                      <label class="block text-sm font-medium text-gray-700 mb-1">Prazo (meses)</label>
                      <input v-model="formData.prazo_meses" type="number" min="1" class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 transition-all" placeholder="12">
                    </div>
                  </div>
                </div>
                
                <!-- Resumo -->
                <div class="bg-gray-50 p-4 rounded-lg shadow-sm hover:shadow-md transition-shadow duration-300">
                  <h3 class="text-lg font-semibold mb-4">Resumo do Investimento</h3>
                  <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div class="p-4 bg-white rounded-md shadow-sm hover:shadow transition-shadow duration-300">
                      <h4 class="text-lg font-semibold mb-2">Valor Total Investido</h4>
                      <p class="text-2xl font-bold text-primary-600">{{ valorTotalFormatado }}</p>
                    </div>
                    
                    <div class="p-4 bg-white rounded-md shadow-sm hover:shadow transition-shadow duration-300">
                      <h4 class="text-lg font-semibold mb-2">Rendimento Mensal Estimado</h4>
                      <p class="text-2xl font-bold text-green-600">{{ rendimentoMensalFormatado }}</p>
                    </div>
                  </div>
                </div>
                
                <!-- Botões de Ação -->
                <div class="flex justify-end gap-4 mt-6">
                  <button 
                    v-if="editandoId"
                    type="button" 
                    @click="cancelarEdicao" 
                    class="bg-gray-300 hover:bg-gray-400 text-gray-800 px-4 py-2 rounded-md transition-all transform hover:scale-105 focus:outline-none focus:ring-2 focus:ring-gray-500 focus:ring-opacity-50 shadow-md flex items-center gap-2"
                  >
                    <span class="material-symbols-outlined">cancel</span> Cancelar Edição
                  </button>
                  <button 
                    type="button" 
                    @click="goToInvestimentos" 
                    class="bg-gray-300 hover:bg-gray-400 text-gray-800 px-4 py-2 rounded-md transition-all transform hover:scale-105 focus:outline-none focus:ring-2 focus:ring-gray-500 focus:ring-opacity-50 shadow-md flex items-center gap-2"
                  >
                    <span class="material-symbols-outlined">arrow_back</span> Voltar
                  </button>
                  <button 
                    type="submit" 
                    :disabled="loading" 
                    class="bg-primary-600 hover:bg-primary-700 text-white px-4 py-2 rounded-md transition-all transform hover:scale-105 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-opacity-50 shadow-md flex items-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed"
                  >
                    <span v-if="loading" class="animate-spin">⏳</span>
                    <span v-else class="material-symbols-outlined">{{ editandoId ? 'save' : 'add_circle' }}</span>
                    {{ textoBotaoSubmit }}
                  </button>
                </div>
              </form>
            </div>

            <!-- Lista de Investimentos -->
            <div class="mt-8">
              <div class="flex items-center justify-between mb-4">
                <h2 class="text-xl font-semibold">Meus Investimentos</h2>
                <div class="flex gap-2">
                  <button @click="filtrarInvestimentos" class="bg-gray-100 hover:bg-gray-200 px-3 py-1 rounded-md text-sm flex items-center gap-1 transition-all">
                    <span class="material-symbols-outlined text-sm">filter_list</span> Filtrar
                  </button>
                  <button @click="exportarDados" class="bg-gray-100 hover:bg-gray-200 px-3 py-1 rounded-md text-sm flex items-center gap-1 transition-all">
                    <span class="material-symbols-outlined text-sm">download</span> Exportar
                  </button>
                </div>
              </div>
              
              <div v-if="carregando" class="text-center py-8">
                <span class="material-symbols-outlined text-6xl text-gray-300 mb-4 animate-spin">refresh</span>
                <p class="text-gray-500">Carregando investimentos...</p>
              </div>
              
              <div v-else-if="investimentos.length === 0" class="text-center py-8">
                <span class="material-symbols-outlined text-6xl text-gray-300 mb-4">account_balance</span>
                <p class="text-gray-500">Nenhum investimento cadastrado ainda.</p>
                <p class="text-gray-400 text-sm">Adicione seu primeiro investimento usando o formulário acima.</p>
              </div>
              
              <div v-else class="overflow-x-auto">
                <table class="min-w-full bg-white rounded-lg overflow-hidden shadow-sm">
                  <thead class="bg-gray-100 text-gray-700">
                    <tr>
                      <th class="py-3 px-4 text-left font-semibold">Tipo</th>
                      <th class="py-3 px-4 text-left font-semibold">Ativo</th>
                      <th class="py-3 px-4 text-left font-semibold">Instituição</th>
                      <th class="py-3 px-4 text-left font-semibold">Valor Unitário</th>
                      <th class="py-3 px-4 text-left font-semibold">Quantidade</th>
                      <th class="py-3 px-4 text-left font-semibold">Total</th>
                      <th class="py-3 px-4 text-left font-semibold">Data</th>
                      <th class="py-3 px-4 text-left font-semibold">Ações</th>
                    </tr>
                  </thead>
                  <tbody class="divide-y divide-gray-200">
                    <tr v-for="investimento in investimentos" :key="investimento.id" class="hover:bg-gray-50 transition-colors">
                      <td class="py-3 px-4">
                        <span :class="['px-2 py-1 rounded-full text-xs font-medium', getTipoBadgeClass(investimento.tipo)]">
                          {{ getTipoDisplay(investimento.tipo) }}
                        </span>
                      </td>
                      <td class="py-3 px-4 font-medium">{{ investimento.nome_patrimonio }}</td>
                      <td class="py-3 px-4">{{ investimento.instituicao }}</td>
                      <td class="py-3 px-4">{{ formatCurrency(investimento.valor_cota) }}</td>
                      <td class="py-3 px-4">{{ formatNumber(investimento.unidades) }}</td>
                      <td class="py-3 px-4 font-medium">{{ formatCurrency(investimento.valor_total) }}</td>
                      <td class="py-3 px-4">{{ formatDate(investimento.data_compra) }}</td>
                      <td class="py-3 px-4">
                        <div class="flex gap-2">
                          <button @click="editarInvestimento(investimento)" class="text-gray-500 hover:text-primary-600 transition-colors rounded-full p-1 hover:bg-gray-100">
                            <span class="material-symbols-outlined text-sm">edit</span>
                          </button>
                          <button @click="excluirInvestimento(investimento.id)" class="text-gray-500 hover:text-red-600 transition-colors rounded-full p-1 hover:bg-gray-100">
                            <span class="material-symbols-outlined text-sm">delete</span>
                          </button>
                        </div>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>

            <!-- Rendimentos Recebidos -->
            <div class="mt-8">
              <h2 class="text-xl font-semibold mb-4">Rendimentos Recebidos</h2>
              <div class="bg-gray-50 p-4 rounded-lg shadow-sm hover:shadow-md transition-shadow duration-300">
                <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4">
                  <div>
                    <label class="block text-sm font-medium text-gray-700 mb-1">Investimento</label>
                    <select v-model="novoRendimento.investimento" class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 transition-all">
                      <option value="">Selecione um ativo</option>
                      <option v-for="investimento in investimentos" :key="investimento.id" :value="investimento.id">
                        {{ investimento.nome_patrimonio }} - {{ getTipoDisplay(investimento.tipo) }}
                      </option>
                    </select>
                  </div>
                  <div>
                    <label class="block text-sm font-medium text-gray-700 mb-1">Valor Recebido (R$)</label>
                    <input v-model="novoRendimento.valor" type="number" step="0.01" min="0.01" class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 transition-all" placeholder="0,00">
                  </div>
                  <div>
                    <label class="block text-sm font-medium text-gray-700 mb-1">Data</label>
                    <input v-model="novoRendimento.data" type="date" class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 transition-all">
                  </div>
                </div>
                <div class="flex justify-end">
                  <button @click="adicionarRendimento" :disabled="!novoRendimento.investimento || !novoRendimento.valor || !novoRendimento.data" class="bg-primary-600 hover:bg-primary-700 text-white px-4 py-2 rounded-md transition-all transform hover:scale-105 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-opacity-50 shadow-md flex items-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed">
                    <span class="material-symbols-outlined">payments</span> Registrar Rendimento
                  </button>
                </div>
              </div>
              
              <div v-if="rendimentos.length === 0" class="text-center py-8">
                <span class="material-symbols-outlined text-6xl text-gray-300 mb-4">payments</span>
                <p class="text-gray-500">Nenhum rendimento registrado ainda.</p>
              </div>
              
              <div v-else class="mt-4 overflow-x-auto">
                <table class="min-w-full bg-white rounded-lg overflow-hidden shadow-sm">
                  <thead class="bg-gray-100 text-gray-700">
                    <tr>
                      <th class="py-3 px-4 text-left font-semibold">Ativo</th>
                      <th class="py-3 px-4 text-left font-semibold">Tipo</th>
                      <th class="py-3 px-4 text-left font-semibold">Valor</th>
                      <th class="py-3 px-4 text-left font-semibold">Data</th>
                      <th class="py-3 px-4 text-left font-semibold">Ações</th>
                    </tr>
                  </thead>
                  <tbody class="divide-y divide-gray-200">
                    <tr v-for="rendimento in rendimentos" :key="rendimento.id" class="hover:bg-gray-50 transition-colors">
                      <td class="py-3 px-4 font-medium">{{ getNomeAtivo(rendimento.investimento) }}</td>
                      <td class="py-3 px-4">{{ getTipoAtivo(rendimento.investimento) }}</td>
                      <td class="py-3 px-4 font-medium text-green-600">{{ formatCurrency(rendimento.valor) }}</td>
                      <td class="py-3 px-4">{{ formatDate(rendimento.data) }}</td>
                      <td class="py-3 px-4">
                        <div class="flex gap-2">
                          <button @click="excluirRendimento(rendimento.id)" class="text-gray-500 hover:text-red-600 transition-colors rounded-full p-1 hover:bg-gray-100">
                            <span class="material-symbols-outlined text-sm">delete</span>
                          </button>
                        </div>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>
      </main>

      <!-- Notificação -->
      <div v-if="showNotification" :class="['fixed top-4 right-4 z-50 p-4 rounded-lg shadow-lg flex items-center transition-all duration-300', notificationType === 'success' ? 'bg-green-100 text-green-800 border border-green-200' : 'bg-red-100 text-red-800 border border-red-200']">
        <span class="material-symbols-outlined mr-2">
          {{ notificationType === 'success' ? 'check_circle' : 'error' }}
        </span>
        {{ notificationMessage }}
      </div>

    </div>
  </div>
              <Footer />
</template>

<script>
import axios from 'axios';
import Header from '@/components/Header.vue';
import Footer from '@/components/Footer.vue';

export default {
  name: 'LancamentoInvestimento',
    components: {
    Header,
    Footer,
  },
  data() {
    return {
      apiUrl: process.env.VUE_APP_API_URL || 'http://localhost:8000',
      formData: {
        tipo: '',
        instituicao: '',
        nome_patrimonio: '',
        valor_cota: '',
        unidades: '',
        data_compra: new Date().toISOString().split('T')[0],
        moeda: 'BRL',
        cotacao_dolar_pago: null,
        taxa_anual: '',
        aporte_mensal: '',
        prazo_meses: ''
      },
      novoRendimento: {
        investimento: '',
        valor: '',
        data: new Date().toISOString().split('T')[0]
      },
      investimentos: [],
      rendimentos: [],
      loading: false,
      carregando: false,
      showNotification: false,
      notificationMessage: '',
      notificationType: 'success',
      editandoId: null
    };
  },
  computed: {
    valorTotal() {
      const valorCota = parseFloat(this.formData.valor_cota) || 0;
      const unidades = parseFloat(this.formData.unidades) || 0;
      let valorTotal = valorCota * unidades;
      
      if (this.formData.moeda === 'USD') {
        const cotacaoDolar = parseFloat(this.formData.cotacao_dolar_pago) || 1;
        valorTotal = valorTotal * cotacaoDolar;
      }
      
      return valorTotal;
    },
    valorTotalFormatado() {
      return new Intl.NumberFormat('pt-BR', {
        style: 'currency',
        currency: 'BRL'
      }).format(this.valorTotal);
    },
    rendimentoMensal() {
      if (!this.formData.taxa_anual) return 0;
      
      const taxaAnual = parseFloat(this.formData.taxa_anual) || 0;
      if (taxaAnual <= 0) return 0;
      
      const taxaDecimal = taxaAnual / 100;
      const mensal = Math.pow(1 + taxaDecimal, 1/12) - 1;
      return mensal * this.valorTotal;
    },
    rendimentoMensalFormatado() {
      return new Intl.NumberFormat('pt-BR', {
        style: 'currency',
        currency: 'BRL'
      }).format(this.rendimentoMensal);
    },
    tituloFormulario() {
      return this.editandoId ? 'Editar Investimento' : 'Adicionar Novo Investimento';
    },
    textoBotaoSubmit() {
      if (this.loading) return 'Processando...';
      return this.editandoId ? 'Atualizar Investimento' : 'Adicionar Investimento';
    }
  },
  mounted() {
    this.carregarInvestimentos();
    this.carregarRendimentos();
  },
  methods: {
    async carregarInvestimentos() {
      const token = localStorage.getItem('token');
      if (!token) {
        this.showNotificationMessage('Faça login para acessar os investimentos', 'error');
        return;
      }

      this.carregando = true;
      try {
        // CORREÇÃO: Usa a rota correta
        const response = await axios.get(`${this.apiUrl}/investimentos/investimentos/`, {
          headers: {
            'Authorization': `Token ${token}`
          }
        });
        
        this.investimentos = response.data.investimentos || response.data || [];
      } catch (error) {
        console.error('Erro ao carregar investimentos:', error);
        this.showNotificationMessage('Erro ao carregar investimentos', 'error');
      } finally {
        this.carregando = false;
      }
    },

    async carregarRendimentos() {
      const token = localStorage.getItem('token');
      if (!token) return;

      try {
        // CORREÇÃO: Usa a rota correta para rendimentos
        const response = await axios.get(`${this.apiUrl}/investimentos/rendimentos/`, {
          headers: {
            'Authorization': `Token ${token}`
          }
        });
        
        this.rendimentos = response.data || [];
      } catch (error) {
        console.error('Erro ao carregar rendimentos:', error);
        this.rendimentos = [];
      }
    },

    validarFormulario() {
      const camposObrigatorios = [
        { campo: 'tipo', nome: 'Tipo de Investimento' },
        { campo: 'instituicao', nome: 'Instituição' },
        { campo: 'nome_patrimonio', nome: 'Nome do Ativo' },
        { campo: 'valor_cota', nome: 'Valor da Cota' },
        { campo: 'unidades', nome: 'Quantidade' },
        { campo: 'data_compra', nome: 'Data da Compra' }
      ];

      const erros = [];

      for (const { campo, nome } of camposObrigatorios) {
        if (!this.formData[campo] || this.formData[campo].toString().trim() === '') {
          erros.push(`${nome} é obrigatório`);
        }
      }

      if (this.formData.valor_cota && parseFloat(this.formData.valor_cota) <= 0) {
        erros.push('Valor da cota deve ser maior que zero');
      }

      if (this.formData.unidades && parseFloat(this.formData.unidades) <= 0) {
        erros.push('Quantidade deve ser maior que zero');
      }

      return erros;
    },

    async submitForm() {
      console.log('Dados do formulário:', this.formData);
      
      const token = localStorage.getItem('token');
      if (!token) {
        this.showNotificationMessage('Faça login novamente', 'error');
        window.location.href = '/painel';
        return;
      }

      const erros = this.validarFormulario();
      if (erros.length > 0) {
        this.showNotificationMessage(erros.join('; '), 'error');
        return;
      }

      this.loading = true;
      
      try {
        const transactionData = {
          tipo: this.formData.tipo.trim(),
          instituicao: this.formData.instituicao.trim(),
          nome_patrimonio: this.formData.nome_patrimonio.trim(),
          valor_cota: Number(parseFloat(this.formData.valor_cota).toFixed(2)),
          unidades: Number(parseFloat(this.formData.unidades).toFixed(6)),
          data_compra: this.formData.data_compra,
          moeda: this.formData.moeda || 'BRL',
        };

        if (this.formData.moeda === 'USD' && this.formData.cotacao_dolar_pago) {
          transactionData.cotacao_dolar_pago = Number(parseFloat(this.formData.cotacao_dolar_pago).toFixed(4));
        }

        if (this.formData.taxa_anual) {
          transactionData.taxa_anual = Number(parseFloat(this.formData.taxa_anual).toFixed(2));
        }

        if (this.formData.aporte_mensal) {
          transactionData.aporte_mensal = Number(parseFloat(this.formData.aporte_mensal).toFixed(2));
        }

        if (this.formData.prazo_meses) {
          transactionData.prazo_meses = parseInt(this.formData.prazo_meses);
        }

        console.log('Dados sendo enviados:', transactionData);
        
        let response;
        if (this.editandoId) {
          // CORREÇÃO: Usa a rota correta para atualização
          response = await axios.put(
            `${this.apiUrl}/investimentos/investimentos/${this.editandoId}/`, 
            transactionData, 
            {
              headers: {
                'Authorization': `Token ${token}`,
                'Content-Type': 'application/json'
              }
            }
          );
        } else {
          // CORREÇÃO: Usa a rota correta para criação
          response = await axios.post(
            `${this.apiUrl}/investimentos/investimentos/`, 
            transactionData, 
            {
              headers: {
                'Authorization': `Token ${token}`,
                'Content-Type': 'application/json'
              }
            }
          );
        }
        
        const mensagem = this.editandoId ? 'Investimento atualizado com sucesso!' : 'Investimento criado com sucesso!';
        this.showNotificationMessage(mensagem, 'success');
        
        this.limparFormulario();
        this.carregarInvestimentos();
        
      } catch (error) {
        console.error('Erro ao salvar investimento:', error);
        this.tratarErro(error);
      } finally {
        this.loading = false;
      }
    },

    async adicionarRendimento() {
      const token = localStorage.getItem('token');
      if (!token) return;

      if (!this.novoRendimento.investimento || !this.novoRendimento.valor || !this.novoRendimento.data) {
        this.showNotificationMessage('Preencha todos os campos obrigatórios', 'error');
        return;
      }

      try {
        const rendimentoData = {
          investimento: parseInt(this.novoRendimento.investimento),
          valor: parseFloat(this.novoRendimento.valor),
          data: this.novoRendimento.data
        };
        
        // CORREÇÃO: Usa a rota correta para rendimentos
        await axios.post(
          `${this.apiUrl}/investimentos/rendimentos/`, 
          rendimentoData, 
          {
            headers: {
              'Authorization': `Token ${token}`,
              'Content-Type': 'application/json'
            }
          }
        );
        
        this.showNotificationMessage('Rendimento registrado com sucesso!', 'success');
        this.novoRendimento = { 
          investimento: '', 
          valor: '', 
          data: new Date().toISOString().split('T')[0] 
        };
        this.carregarRendimentos();
        
      } catch (error) {
        console.error('Erro ao adicionar rendimento:', error);
        this.tratarErro(error);
      }
    },

    async excluirInvestimento(id) {
      if (!confirm('Tem certeza que deseja excluir este investimento?')) return;

      const token = localStorage.getItem('token');
      if (!token) return;

      try {
        // CORREÇÃO: Usa a rota correta para exclusão
        await axios.delete(`${this.apiUrl}/investimentos/investimentos/${id}/`, {
          headers: {
            'Authorization': `Token ${token}`
          }
        });
        
        this.showNotificationMessage('Investimento excluído com sucesso!', 'success');
        this.carregarInvestimentos();
        
      } catch (error) {
        console.error('Erro ao excluir investimento:', error);
        this.tratarErro(error);
      }
    },

    async excluirRendimento(id) {
      if (!confirm('Tem certeza que deseja excluir este rendimento?')) return;

      const token = localStorage.getItem('token');
      if (!token) return;

      try {
        // CORREÇÃO: Usa a rota correta para exclusão de rendimentos
        await axios.delete(`${this.apiUrl}/investimentos/rendimentos/${id}/`, {
          headers: {
            'Authorization': `Token ${token}`
          }
        });
        
        this.showNotificationMessage('Rendimento excluído com sucesso!', 'success');
        this.carregarRendimentos();
        
      } catch (error) {
        console.error('Erro ao excluir rendimento:', error);
        this.tratarErro(error);
      }
    },

    limparFormulario() {
      this.formData = {
        tipo: '',
        instituicao: '',
        nome_patrimonio: '',
        valor_cota: '',
        unidades: '',
        data_compra: new Date().toISOString().split('T')[0],
        moeda: 'BRL',
        cotacao_dolar_pago: null,
        taxa_anual: '',
        aporte_mensal: '',
        prazo_meses: ''
      };
      this.editandoId = null;
    },

    tratarErro(error) {
      let errorMessage = 'Erro ao processar a solicitação.';
      
      if (error.response) {
        if (error.response.status === 404) {
          errorMessage = 'Endpoint não encontrado. Verifique as URLs da API.';
          console.error('URL não encontrada:', error.config.url);
        } else if (error.response.data) {
          if (typeof error.response.data === 'object') {
            // Trata erros de validação do Django
            const errors = [];
            for (const [field, messages] of Object.entries(error.response.data)) {
              if (Array.isArray(messages)) {
                errors.push(`${this.getFieldName(field)}: ${messages.join(', ')}`);
              } else {
                errors.push(`${this.getFieldName(field)}: ${messages}`);
              }
            }
            errorMessage = `Erros de validação: ${errors.join('; ')}`;
          } else if (error.response.data.detail) {
            errorMessage = error.response.data.detail;
          } else {
            errorMessage = JSON.stringify(error.response.data);
          }
        } else {
          errorMessage = `Erro ${error.response.status}: ${error.response.statusText}`;
        }
      } else if (error.request) {
        errorMessage = 'Erro de conexão. Verifique se o servidor está rodando.';
      } else {
        errorMessage = error.message;
      }
      
      this.showNotificationMessage(errorMessage, 'error');
    },

    getFieldName(field) {
      const fieldNames = {
        'tipo': 'Tipo de Investimento',
        'instituicao': 'Instituição',
        'nome_patrimonio': 'Nome do Ativo',
        'valor_cota': 'Valor da Cota',
        'unidades': 'Quantidade',
        'data_compra': 'Data da Compra',
        'moeda': 'Moeda'
      };
      return fieldNames[field] || field;
    },

    showNotificationMessage(message, type) {
      this.notificationMessage = message;
      this.notificationType = type;
      this.showNotification = true;
      
      setTimeout(() => {
        this.showNotification = false;
      }, 5000);
    },

    getTipoDisplay(tipo) {
      const tipos = {
        'ACAO': 'Ação',
        'FII': 'FII',
        'CRIPTO': 'Cripto',
        'TESOURO': 'Tesouro',
        'POUPANCA': 'Poupança',
        'CDB': 'CDB',
        'LCI': 'LCI',
        'LCA': 'LCA'
      };
      return tipos[tipo] || tipo;
    },

    getTipoBadgeClass(tipo) {
      const classes = {
        'ACAO': 'bg-blue-100 text-blue-800',
        'FII': 'bg-green-100 text-green-800',
        'CRIPTO': 'bg-purple-100 text-purple-800',
        'TESOURO': 'bg-yellow-100 text-yellow-800',
        'POUPANCA': 'bg-gray-100 text-gray-800',
        'CDB': 'bg-yellow-100 text-yellow-800',
        'LCI': 'bg-green-100 text-green-800',
        'LCA': 'bg-green-100 text-green-800'
      };
      return classes[tipo] || 'bg-gray-100 text-gray-800';
    },

    formatCurrency(value) {
      if (!value && value !== 0) return 'R$ 0,00';
      return new Intl.NumberFormat('pt-BR', {
        style: 'currency',
        currency: 'BRL'
      }).format(value);
    },

    formatNumber(value) {
      if (!value && value !== 0) return '0';
      return new Intl.NumberFormat('pt-BR', {
        minimumFractionDigits: 0,
        maximumFractionDigits: 6
      }).format(value);
    },

    formatDate(dateString) {
      if (!dateString) return 'N/A';
      return new Date(dateString).toLocaleDateString('pt-BR');
    },

    getNomeAtivo(investimentoId) {
      const investimento = this.investimentos.find(i => i.id === investimentoId);
      return investimento ? investimento.nome_patrimonio : 'N/A';
    },

    getTipoAtivo(investimentoId) {
      const investimento = this.investimentos.find(i => i.id === investimentoId);
      return investimento ? this.getTipoDisplay(investimento.tipo) : 'N/A';
    },

    editarInvestimento(investimento) {
      this.formData = {
        tipo: investimento.tipo,
        instituicao: investimento.instituicao,
        nome_patrimonio: investimento.nome_patrimonio,
        valor_cota: investimento.valor_cota,
        unidades: investimento.unidades,
        data_compra: investimento.data_compra.split('T')[0],
        moeda: investimento.moeda || 'BRL',
        cotacao_dolar_pago: investimento.cotacao_dolar_pago,
        taxa_anual: investimento.taxa_anual,
        aporte_mensal: investimento.aporte_mensal,
        prazo_meses: investimento.prazo_meses
      };
      
      this.editandoId = investimento.id;
      window.scrollTo({ top: 0, behavior: 'smooth' });
    },

    cancelarEdicao() {
      this.limparFormulario();
      this.showNotificationMessage('Edição cancelada', 'info');
    },

    filtrarInvestimentos() {
      this.showNotificationMessage('Funcionalidade de filtro em desenvolvimento', 'info');
    },

    exportarDados() {
      const data = {
        investimentos: this.investimentos,
        rendimentos: this.rendimentos,
        exportado_em: new Date().toISOString()
      };
      
      const dataStr = JSON.stringify(data, null, 2);
      const dataBlob = new Blob([dataStr], {type: 'application/json'});
      const url = URL.createObjectURL(dataBlob);
      const link = document.createElement('a');
      link.href = url;
      link.download = `investimentos_${new Date().toISOString().split('T')[0]}.json`;
      link.click();
      URL.revokeObjectURL(url);
      
      this.showNotificationMessage('Dados exportados com sucesso!', 'success');
    },

    goToDashboard() {
      window.location.href = '/dashboard';
    },
    
    goToInvestimentos() {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  }
};
</script>


<style scoped>
/* Importação de fontes e ícones */
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;500;600;700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200');

/* Reset e estilos base */
#webcrumbs *,
#webcrumbs :after,
#webcrumbs :before {
  border: 0 solid #e5e7eb;
  box-sizing: border-box;
}

#webcrumbs {
  font-family: 'Open Sans', ui-sans-serif, system-ui, sans-serif !important;
  font-size: 16px !important;
  line-height: 1.5;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

/* Container */
#webcrumbs .container {
  width: 100%;
  max-width: 1200px;
  margin-left: auto;
  margin-right: auto;
}

/* Layout */
#webcrumbs .absolute { position: absolute; }
#webcrumbs .fixed { position: fixed; }
#webcrumbs .relative { position: relative; }
#webcrumbs .right-4 { right: 16px; }
#webcrumbs .top-4 { top: 16px; }
#webcrumbs .z-50 { z-index: 50; }
#webcrumbs .mx-auto { margin-left: auto; margin-right: auto; }

/* Margins */
#webcrumbs .mb-1 { margin-bottom: 4px; }
#webcrumbs .mb-2 { margin-bottom: 8px; }
#webcrumbs .mb-4 { margin-bottom: 16px; }
#webcrumbs .mb-6 { margin-bottom: 24px; }
#webcrumbs .mb-8 { margin-bottom: 32px; }
#webcrumbs .mr-2 { margin-right: 8px; }
#webcrumbs .mt-4 { margin-top: 16px; }
#webcrumbs .mt-6 { margin-top: 24px; }
#webcrumbs .mt-8 { margin-top: 32px; }

/* Display */
#webcrumbs .block { display: block; }
#webcrumbs .flex { display: flex; }
#webcrumbs .inline-flex { display: inline-flex; }
#webcrumbs .grid { display: grid; }
#webcrumbs .hidden { display: none; }
#webcrumbs .inline-block { display: inline-block; }

/* Dimensões */
#webcrumbs .h-8 { height: 32px; }
#webcrumbs .h-full { height: 100%; }
#webcrumbs .min-h-screen { min-height: 100vh; }
#webcrumbs .w-8 { width: 32px; }
#webcrumbs .w-full { width: 100%; }
#webcrumbs .min-w-full { min-width: 100%; }
#webcrumbs .flex-1 { flex: 1 1 0%; }

/* Transform */
#webcrumbs .transform {
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate))
              skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

/* Grid */
#webcrumbs .grid-cols-1 { grid-template-columns: repeat(1, minmax(0, 1fr)); }

/* Flexbox */
#webcrumbs .flex-row { flex-direction: row; }
#webcrumbs .flex-col { flex-direction: column; }
#webcrumbs .items-center { align-items: center; }
#webcrumbs .items-start { align-items: flex-start; }
#webcrumbs .justify-start { justify-content: flex-start; }
#webcrumbs .justify-end { justify-content: flex-end; }
#webcrumbs .justify-center { justify-content: center; }
#webcrumbs .justify-between { justify-content: space-between; }
#webcrumbs .justify-around { justify-content: space-around; }

/* Espaçamento */
#webcrumbs .gap-1 { gap: 4px; }
#webcrumbs .gap-2 { gap: 8px; }
#webcrumbs .gap-4 { gap: 16px; }
#webcrumbs .space-x-2 > * + * { margin-left: 8px; }
#webcrumbs .space-x-4 > * + * { margin-left: 16px; }
#webcrumbs .space-y-4 > * + * { margin-top: 16px; }
#webcrumbs .space-y-6 > * + * { margin-top: 24px; }

/* Dividers */
#webcrumbs .divide-y > * + * {
  border-top-width: 1px;
}
#webcrumbs .divide-gray-200 > * + * {
  border-color: rgb(229 231 235);
}

/* Overflow */
#webcrumbs .overflow-hidden { overflow: hidden; }
#webcrumbs .overflow-x-auto { overflow-x: auto; }
#webcrumbs .overflow-y-auto { overflow-y: auto; }
#webcrumbs .overflow-x-hidden { overflow-x: hidden; }

/* Scrollbar personalizada */
#webcrumbs ::-webkit-scrollbar {
  width: 6px;
  height: 6px;
}

#webcrumbs ::-webkit-scrollbar-track {
  background: #f1f1f1;
  border-radius: 3px;
}

#webcrumbs ::-webkit-scrollbar-thumb {
  background: #c1c1c1;
  border-radius: 3px;
}

#webcrumbs ::-webkit-scrollbar-thumb:hover {
  background: #a8a8a8;
}

/* Bordas */
#webcrumbs .rounded { border-radius: 4px; }
#webcrumbs .rounded-full { border-radius: 9999px; }
#webcrumbs .rounded-lg { border-radius: 8px; }
#webcrumbs .rounded-md { border-radius: 6px; }
#webcrumbs .rounded-xl { border-radius: 12px; }
#webcrumbs .rounded-2xl { border-radius: 16px; }
#webcrumbs .rounded-l-md { 
  border-top-left-radius: 6px;
  border-bottom-left-radius: 6px;
}
#webcrumbs .rounded-r-md { 
  border-top-right-radius: 6px;
  border-bottom-right-radius: 6px;
}

#webcrumbs .border { border-width: 1px; }
#webcrumbs .border-2 { border-width: 2px; }
#webcrumbs .border-0 { border-width: 0; }
#webcrumbs .border-r-0 { border-right-width: 0; }
#webcrumbs .border-l-0 { border-left-width: 0; }

/* Cores de borda */
#webcrumbs .border-gray-200 { border-color: rgb(229 231 235); }
#webcrumbs .border-gray-300 { border-color: rgb(209 213 219); }
#webcrumbs .border-green-200 { border-color: rgb(187 247 208); }
#webcrumbs .border-red-200 { border-color: rgb(254 202 202); }
#webcrumbs .border-transparent { border-color: transparent; }

/* Cores de fundo */
#webcrumbs .bg-\[\#282641\] { background-color: rgb(40 38 65); }
#webcrumbs .bg-\[\#a79de9\] { background-color: rgb(167 157 233); }
#webcrumbs .bg-\[\#615c8e\] { background-color: rgb(97 92 142); }

#webcrumbs .bg-blue-100 { background-color: rgb(219 234 254); }
#webcrumbs .bg-blue-500 { background-color: rgb(59 130 246); }
#webcrumbs .bg-blue-600 { background-color: rgb(37 99 235); }

#webcrumbs .bg-gray-50 { background-color: rgb(249 250 251); }
#webcrumbs .bg-gray-100 { background-color: rgb(243 244 246); }
#webcrumbs .bg-gray-200 { background-color: rgb(229 231 235); }
#webcrumbs .bg-gray-300 { background-color: rgb(209 213 219); }
#webcrumbs .bg-gray-400 { background-color: rgb(156 163 175); }
#webcrumbs .bg-gray-500 { background-color: rgb(107 114 128); }

#webcrumbs .bg-green-100 { background-color: rgb(220 252 231); }
#webcrumbs .bg-green-500 { background-color: rgb(34 197 94); }

#webcrumbs .bg-primary-600 { 
  background-color: rgb(99 27 255);
  color: hsla(0, 0%, 100%, 0.9) !important;
}
#webcrumbs .bg-primary-700 { background-color: rgb(97 27 248); }

#webcrumbs .bg-purple-100 { background-color: rgb(243 232 255); }
#webcrumbs .bg-purple-500 { background-color: rgb(168 85 247); }

#webcrumbs .bg-red-100 { background-color: rgb(254 226 226); }
#webcrumbs .bg-red-500 { background-color: rgb(239 68 68); }

#webcrumbs .bg-white { background-color: rgb(255 255 255); }
#webcrumbs .bg-black { background-color: rgb(0 0 0); }

#webcrumbs .bg-yellow-100 { background-color: rgb(254 249 195); }
#webcrumbs .bg-yellow-500 { background-color: rgb(234 179 8); }

#webcrumbs .bg-opacity-50 { background-color: rgba(255, 255, 255, 0.5); }
#webcrumbs .bg-opacity-90 { background-color: rgba(255, 255, 255, 0.9); }

/* Gradientes */
#webcrumbs .bg-gradient-to-r {
  background-image: linear-gradient(to right, var(--tw-gradient-stops));
}
#webcrumbs .bg-gradient-to-b {
  background-image: linear-gradient(to bottom, var(--tw-gradient-stops));
}

#webcrumbs .from-primary-600 {
  --tw-gradient-from: #631bff;
  --tw-gradient-to: rgba(99, 27, 255, 0);
  --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to);
}
#webcrumbs .to-primary-800 {
  --tw-gradient-to: #4607d0;
}

/* Padding */
#webcrumbs .p-1 { padding: 4px; }
#webcrumbs .p-2 { padding: 8px; }
#webcrumbs .p-3 { padding: 12px; }
#webcrumbs .p-4 { padding: 16px; }
#webcrumbs .p-5 { padding: 20px; }
#webcrumbs .p-6 { padding: 24px; }
#webcrumbs .p-8 { padding: 32px; }

#webcrumbs .px-2 { padding-left: 8px; padding-right: 8px; }
#webcrumbs .px-3 { padding-left: 12px; padding-right: 12px; }
#webcrumbs .px-4 { padding-left: 16px; padding-right: 16px; }
#webcrumbs .px-6 { padding-left: 24px; padding-right: 24px; }

#webcrumbs .py-1 { padding-top: 4px; padding-bottom: 4px; }
#webcrumbs .py-2 { padding-top: 8px; padding-bottom: 8px; }
#webcrumbs .py-3 { padding-top: 12px; padding-bottom: 12px; }
#webcrumbs .py-4 { padding-top: 16px; padding-bottom: 16px; }

#webcrumbs .pt-4 { padding-top: 16px; }
#webcrumbs .pb-4 { padding-bottom: 16px; }
#webcrumbs .pl-4 { padding-left: 16px; }
#webcrumbs .pr-4 { padding-right: 16px; }

/* Texto */
#webcrumbs .text-left { text-align: left; }
#webcrumbs .text-center { text-align: center; }
#webcrumbs .text-right { text-align: right; }

#webcrumbs .text-xs { 
  font-size: 12px;
  line-height: 16px;
}
#webcrumbs .text-sm { 
  font-size: 14px;
  line-height: 20px;
}
#webcrumbs .text-base { 
  font-size: 16px;
  line-height: 24px;
}
#webcrumbs .text-lg { 
  font-size: 18px;
  line-height: 28px;
}
#webcrumbs .text-xl { 
  font-size: 20px;
  line-height: 28px;
}
#webcrumbs .text-2xl { 
  font-size: 24px;
  line-height: 32px;
}
#webcrumbs .text-3xl { 
  font-size: 30px;
  line-height: 36px;
}
#webcrumbs .text-4xl { 
  font-size: 36px;
  line-height: 40px;
}

/* Font weight */
#webcrumbs .font-light { font-weight: 300; }
#webcrumbs .font-normal { font-weight: 400; }
#webcrumbs .font-medium { font-weight: 500; }
#webcrumbs .font-semibold { font-weight: 600; }
#webcrumbs .font-bold { font-weight: 700; }
#webcrumbs .font-extrabold { font-weight: 800; }

/* Cores de texto */
#webcrumbs .text-white { color: rgb(255 255 255); }
#webcrumbs .text-black { color: rgb(0 0 0); }

#webcrumbs .text-gray-400 { color: rgb(156 163 175); }
#webcrumbs .text-gray-500 { color: rgb(107 114 128); }
#webcrumbs .text-gray-600 { color: rgb(75 85 99); }
#webcrumbs .text-gray-700 { color: rgb(55 65 81); }
#webcrumbs .text-gray-800 { color: rgb(31 41 55); }
#webcrumbs .text-gray-900 { color: rgb(17 24 39); }

#webcrumbs .text-blue-500 { color: rgb(59 130 246); }
#webcrumbs .text-blue-600 { color: rgb(37 99 235); }
#webcrumbs .text-blue-800 { color: rgb(30 64 175); }

#webcrumbs .text-green-500 { color: rgb(34 197 94); }
#webcrumbs .text-green-600 { color: rgb(22 163 74); }
#webcrumbs .text-green-800 { color: rgb(22 101 52); }

#webcrumbs .text-primary-600 { color: rgb(99 27 255); }

#webcrumbs .text-purple-500 { color: rgb(168 85 247); }
#webcrumbs .text-purple-800 { color: rgb(107 33 168); }

#webcrumbs .text-red-500 { color: rgb(239 68 68); }
#webcrumbs .text-red-600 { color: rgb(220 38 38); }
#webcrumbs .text-red-800 { color: rgb(153 27 27); }

#webcrumbs .text-yellow-500 { color: rgb(234 179 8); }
#webcrumbs .text-yellow-800 { color: rgb(133 77 14); }

#webcrumbs .text-\[\#a79de9\] { color: rgb(167 157 233); }

/* Opacidade */
#webcrumbs .opacity-0 { opacity: 0; }
#webcrumbs .opacity-50 { opacity: 0.5; }
#webcrumbs .opacity-70 { opacity: 0.7; }
#webcrumbs .opacity-90 { opacity: 0.9; }
#webcrumbs .opacity-100 { opacity: 1; }

/* Sombras */
#webcrumbs .shadow-sm {
  box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
}
#webcrumbs .shadow {
  box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06);
}
#webcrumbs .shadow-md {
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
}
#webcrumbs .shadow-lg {
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
}
#webcrumbs .shadow-xl {
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
}
#webcrumbs .shadow-2xl {
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
}

#webcrumbs .shadow-inner {
  box-shadow: inset 0 2px 4px 0 rgba(0, 0, 0, 0.06);
}

/* Transições */
#webcrumbs .transition-none { transition-property: none; }
#webcrumbs .transition-all {
  transition-property: all;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 150ms;
}
#webcrumbs .transition {
  transition-property: color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 150ms;
}
#webcrumbs .transition-colors {
  transition-property: color, background-color, border-color, text-decoration-color, fill, stroke;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 150ms;
}
#webcrumbs .transition-opacity {
  transition-property: opacity;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 150ms;
}
#webcrumbs .transition-shadow {
  transition-property: box-shadow;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 150ms;
}
#webcrumbs .transition-transform {
  transition-property: transform;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 150ms;
}

/* Durações */
#webcrumbs .duration-75 { transition-duration: 75ms; }
#webcrumbs .duration-100 { transition-duration: 100ms; }
#webcrumbs .duration-150 { transition-duration: 150ms; }
#webcrumbs .duration-200 { transition-duration: 200ms; }
#webcrumbs .duration-300 { transition-duration: 300ms; }
#webcrumbs .duration-500 { transition-duration: 500ms; }

/* Estados hover */
#webcrumbs .hover\:bg-\[\#615c8e\]:hover { background-color: rgb(97 92 142); }
#webcrumbs .hover\:bg-gray-50:hover { background-color: rgb(249 250 251); }
#webcrumbs .hover\:bg-gray-100:hover { background-color: rgb(243 244 246); }
#webcrumbs .hover\:bg-gray-200:hover { background-color: rgb(229 231 235); }
#webcrumbs .hover\:bg-gray-300:hover { background-color: rgb(209 213 219); }
#webcrumbs .hover\:bg-gray-400:hover { background-color: rgb(156 163 175); }
#webcrumbs .hover\:bg-primary-700:hover { background-color: rgb(97 27 248); }

#webcrumbs .hover\:text-\[\#a79de9\]:hover { color: rgb(167 157 233); }
#webcrumbs .hover\:text-primary-600:hover { color: rgb(99 27 255); }
#webcrumbs .hover\:text-gray-600:hover { color: rgb(75 85 99); }
#webcrumbs .hover\:text-gray-900:hover { color: rgb(17 24 39); }
#webcrumbs .hover\:text-red-600:hover { color: rgb(220 38 38); }

#webcrumbs .hover\:scale-105:hover {
  transform: scale(1.05);
}
#webcrumbs .hover\:scale-110:hover {
  transform: scale(1.1);
}

#webcrumbs .hover\:shadow:hover {
  box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06);
}
#webcrumbs .hover\:shadow-md:hover {
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
}
#webcrumbs .hover\:shadow-lg:hover {
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
}

#webcrumbs .hover\:border-gray-300:hover { border-color: rgb(209 213 219); }
#webcrumbs .hover\:border-primary-500:hover { border-color: rgb(115 65 255); }

/* Estados focus */
#webcrumbs .focus\:outline-none:focus {
  outline: 2px solid transparent;
  outline-offset: 2px;
}
#webcrumbs .focus\:outline-2:focus {
  outline-width: 2px;
}
#webcrumbs .focus\:outline-offset-2:focus {
  outline-offset: 2px;
}

#webcrumbs .focus\:ring-0:focus {
  --tw-ring-offset-shadow: var(--tw-ring-inset) 0 0 0 var(--tw-ring-offset-width) var(--tw-ring-offset-color);
  --tw-ring-shadow: var(--tw-ring-inset) 0 0 0 calc(0px + var(--tw-ring-offset-width)) var(--tw-ring-color);
  box-shadow: var(--tw-ring-offset-shadow), var(--tw-ring-shadow), var(--tw-shadow, 0 0 #0000);
}
#webcrumbs .focus\:ring-2:focus {
  --tw-ring-offset-shadow: var(--tw-ring-inset) 0 0 0 var(--tw-ring-offset-width) var(--tw-ring-offset-color);
  --tw-ring-shadow: var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color);
  box-shadow: var(--tw-ring-offset-shadow), var(--tw-ring-shadow), var(--tw-shadow, 0 0 #0000);
}
#webcrumbs .focus\:ring-4:focus {
  --tw-ring-offset-shadow: var(--tw-ring-inset) 0 0 0 var(--tw-ring-offset-width) var(--tw-ring-offset-color);
  --tw-ring-shadow: var(--tw-ring-inset) 0 0 0 calc(4px + var(--tw-ring-offset-width)) var(--tw-ring-color);
  box-shadow: var(--tw-ring-offset-shadow), var(--tw-ring-shadow), var(--tw-shadow, 0 0 #0000);
}

#webcrumbs .focus\:ring-gray-500:focus {
  --tw-ring-color: rgb(107 114 128);
}
#webcrumbs .focus\:ring-primary-500:focus {
  --tw-ring-color: rgb(115 65 255);
}
#webcrumbs .focus\:ring-blue-500:focus {
  --tw-ring-color: rgb(59 130 246);
}

#webcrumbs .focus\:ring-opacity-50:focus {
  --tw-ring-opacity: 0.5;
}
#webcrumbs .focus\:ring-opacity-25:focus {
  --tw-ring-opacity: 0.25;
}

#webcrumbs .focus\:border-primary-500:focus {
  border-color: rgb(115 65 255);
}
#webcrumbs .focus\:border-blue-500:focus {
  border-color: rgb(59 130 246);
}

/* Estados active */
#webcrumbs .active\:scale-95:active {
  transform: scale(0.95);
}
#webcrumbs .active\:bg-gray-100:active {
  background-color: rgb(243 244 246);
}

/* Estados disabled */
#webcrumbs .disabled\:opacity-50:disabled {
  opacity: 0.5;
}
#webcrumbs .disabled\:cursor-not-allowed:disabled {
  cursor: not-allowed;
}
#webcrumbs .disabled\:bg-gray-200:disabled {
  background-color: rgb(229 231 235);
}
#webcrumbs .disabled\:text-gray-500:disabled {
  color: rgb(107 114 128);
}

/* Responsividade */
@media (min-width: 640px) {
  #webcrumbs .sm\:block { display: block; }
  #webcrumbs .sm\:flex { display: flex; }
  #webcrumbs .sm\:hidden { display: none; }
  #webcrumbs .sm\:text-lg { font-size: 18px; }
  #webcrumbs .sm\:p-6 { padding: 24px; }
}

@media (min-width: 768px) {
  #webcrumbs .md\:flex { display: flex; }
  #webcrumbs .md\:grid { display: grid; }
  #webcrumbs .md\:hidden { display: none; }
  #webcrumbs .md\:block { display: block; }
  
  #webcrumbs .md\:grid-cols-2 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  #webcrumbs .md\:grid-cols-3 { grid-template-columns: repeat(3, minmax(0, 1fr)); }
  #webcrumbs .md\:grid-cols-4 { grid-template-columns: repeat(4, minmax(0, 1fr)); }
  
  #webcrumbs .md\:p-6 { padding: 24px; }
  #webcrumbs .md\:p-8 { padding: 32px; }
  #webcrumbs .md\:text-xl { font-size: 20px; }
  #webcrumbs .md\:text-2xl { font-size: 24px; }
}

@media (min-width: 1024px) {
  #webcrumbs .lg\:flex { display: flex; }
  #webcrumbs .lg\:grid-cols-3 { grid-template-columns: repeat(3, minmax(0, 1fr)); }
  #webcrumbs .lg\:grid-cols-4 { grid-template-columns: repeat(4, minmax(0, 1fr)); }
  #webcrumbs .lg\:p-8 { padding: 32px; }
  #webcrumbs .lg\:text-3xl { font-size: 30px; }
}

@media (min-width: 1280px) {
  #webcrumbs .xl\:grid-cols-4 { grid-template-columns: repeat(4, minmax(0, 1fr)); }
  #webcrumbs .xl\:grid-cols-5 { grid-template-columns: repeat(5, minmax(0, 1fr)); }
}

/* Animações customizadas */
.animate-spin {
  animation: spin 1s linear infinite;
}

.animate-pulse {
  animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}

.animate-bounce {
  animation: bounce 1s infinite;
}

.animate-fade-in {
  animation: fadeIn 0.5s ease-in-out;
}

.animate-slide-in {
  animation: slideIn 0.3s ease-out;
}

@keyframes spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

@keyframes pulse {
  0%, 100% {
    opacity: 1;
  }
  50% {
    opacity: .5;
  }
}

@keyframes bounce {
  0%, 100% {
    transform: translateY(-25%);
    animation-timing-function: cubic-bezier(0.8,0,1,1);
  }
  50% {
    transform: none;
    animation-timing-function: cubic-bezier(0,0,0.2,1);
  }
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes slideIn {
  from {
    transform: translateX(-100%);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}

/* Melhorias de acessibilidade */
#webcrumbs button:focus-visible,
#webcrumbs input:focus-visible,
#webcrumbs select:focus-visible,
#webcrumbs textarea:focus-visible {
  outline: 2px solid #631bff;
  outline-offset: 2px;
  border-color: #631bff;
}

/* Scroll suave para toda a aplicação */
#webcrumbs {
  scroll-behavior: smooth;
}

/* Seleção de texto personalizada */
#webcrumbs ::selection {
  background-color: rgb(99 27 255 / 0.2);
  color: inherit;
}

/* Placeholder styling */
#webcrumbs ::-webkit-input-placeholder {
  color: rgb(156 163 175);
  opacity: 1;
}
#webcrumbs :-moz-placeholder {
  color: rgb(156 163 175);
  opacity: 1;
}
#webcrumbs ::-moz-placeholder {
  color: rgb(156 163 175);
  opacity: 1;
}
#webcrumbs :-ms-input-placeholder {
  color: rgb(156 163 175);
  opacity: 1;
}

/* Material Icons sizing */
.material-symbols-outlined {
  font-variation-settings:
  'FILL' 0,
  'wght' 400,
  'GRAD' 0,
  'opsz' 24;
}

.material-symbols-outlined.text-sm {
  font-size: 14px;
}

.material-symbols-outlined.text-lg {
  font-size: 18px;
}

.material-symbols-outlined.text-xl {
  font-size: 20px;
}

.material-symbols-outlined.text-2xl {
  font-size: 24px;
}

/* Loading states específicos */
#webcrumbs button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
  transform: none !important;
}

#webcrumbs button:disabled:hover {
  transform: none !important;
  box-shadow: none !important;
}

/* Estados para tabelas */
#webcrumbs table {
  border-collapse: collapse;
  width: 100%;
}

#webcrumbs th {
  font-weight: 600;
  text-align: left;
  background-color: rgb(249 250 251);
}

#webcrumbs td, #webcrumbs th {
  padding: 12px 16px;
  border-bottom: 1px solid rgb(229 231 235);
}

#webcrumbs tr:last-child td {
  border-bottom: none;
}

/* Estados para formulários */
#webcrumbs input, #webcrumbs select, #webcrumbs textarea {
  transition: all 0.2s ease-in-out;
}

#webcrumbs input:focus, #webcrumbs select:focus, #webcrumbs textarea:focus {
  border-color: #631bff;
  box-shadow: 0 0 0 3px rgb(99 27 255 / 0.1);
}

/* Estados para cards */
#webcrumbs .card {
  transition: all 0.3s ease;
}

#webcrumbs .card:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1);
}

/* Utilitários extras */
.cursor-pointer { cursor: pointer; }
.cursor-not-allowed { cursor: not-allowed; }
.cursor-default { cursor: default; }

.select-none { user-select: none; }
.select-text { user-select: text; }
.select-all { user-select: all; }

.pointer-events-none { pointer-events: none; }
.pointer-events-auto { pointer-events: auto; }

.whitespace-nowrap { white-space: nowrap; }
.whitespace-normal { white-space: normal; }
.whitespace-pre { white-space: pre; }

.break-words { word-wrap: break-word; }
.break-all { word-break: break-all; }

.truncate {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.leading-normal { line-height: 1.5; }
.leading-relaxed { line-height: 1.625; }
.leading-tight { line-height: 1.25; }

.tracking-wide { letter-spacing: 0.025em; }
.tracking-tight { letter-spacing: -0.025em; }


/* Print styles */
@media print {
  #webcrumbs .no-print {
    display: none !important;
  }
  
  #webcrumbs {
    font-size: 12pt;
    line-height: 1.4;
  }
  
  #webcrumbs .break-after-page {
    page-break-after: always;
  }
}
</style>