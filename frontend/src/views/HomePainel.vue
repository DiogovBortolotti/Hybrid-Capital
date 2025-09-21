<template>
  <div id="painelhome">
    <div class="min-h-screen flex flex-col">
      <Header />
      <main class="flex-grow p-4 md:p-6 bg-[#eed4ed]/10 container mx-auto">
        <div class="flex items-center justify-between mb-8">
          <div>
            <h2 class="text-2xl font-bold text-[#282641]">Bem-vindo de volta, {{ user.full_name }}!</h2>
            <p class="text-[#615c8e]">Resumo da sua situação financeira - {{ periodLabel }}</p>
          </div>
          <div class="flex gap-4">
            <button
              class="bg-[#282641] text-white px-6 py-2 rounded-md hover:bg-[#615c8e] transition-colors duration-300 flex items-center space-x-2 shadow-md hover:shadow-lg transform hover:translate-y-[-2px]"
              @click="$router.push('/lancamento')"
            >
              <span class="material-symbols-outlined">add</span>
              <span>Novo Lançamento</span>
            </button>

            <button
              class="bg-[#282641] text-white px-6 py-2 rounded-md hover:bg-[#615c8e] transition-colors duration-300 flex items-center space-x-2 shadow-md hover:shadow-lg transform hover:translate-y-[-2px]"
              @click="$router.push('/lancamentos')"
            >
              <span class="material-symbols-outlined">details</span>
              <span>Lançamentos</span>
            </button>
          </div>
        </div>

        <!-- Filtro de Período -->
        <div class="flex justify-end mb-6">
          <select 
            v-model="selectedPeriod" 
            @change="fetchDashboardData"
            :disabled="loading"
            class="bg-white border border-gray-300 rounded-md px-4 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-[#a79de9]"
          >
            <option value="this_month">Mês Atual</option>
            <option value="last_month">Mês Anterior</option>
            <option value="last_3_months">Últimos 3 Meses</option>
            <option value="last_6_months">Últimos 6 Meses</option>
            <option value="this_year">Ano Atual</option>
            <option value="last_year">Ano Anterior</option>
          </select>
        </div>

        <!-- Loading state -->
        <div v-if="loading" class="text-center py-8">
          <span class="material-symbols-outlined animate-spin text-[#615c8e] text-4xl">refresh</span>
          <p class="text-[#615c8e] mt-2">Carregando dados...</p>
        </div>

        <!-- Error state -->
        <div v-if="error" class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-6">
          <p>Erro ao carregar dados: {{ error }}</p>
          <button 
            @click="fetchDashboardData" 
            class="mt-2 bg-red-600 text-white px-4 py-2 rounded hover:bg-red-700"
          >
            Tentar Novamente
          </button>
        </div>

        <!-- Dashboard data -->
        <div v-if="!loading && !error && hasData">
          <div class="grid grid-cols-1 md:grid-cols-3 gap-4 md:gap-6 mb-8">
            <div
              class="bg-white p-5 rounded-lg shadow-md hover:shadow-lg transition-all duration-300 transform hover:translate-y-[-2px] border border-gray-100">
              <div class="flex justify-between items-center mb-3">
                <h3 class="font-semibold text-[#282641]">Saldo Total</h3>
                <span class="material-symbols-outlined text-[#615c8e]">account_balance_wallet</span>
              </div>
              <p class="text-3xl font-bold" :class="dashboardData.saldo_total >= 0 ? 'text-[#282641]' : 'text-red-500'">
                R$ {{ formatCurrency(dashboardData.saldo_total) }}
              </p>
              <div class="flex items-center mt-2" :class="saldoVariation >= 0 ? 'text-green-500' : 'text-red-500'" v-if="saldoVariation !== 0">
                <span class="material-symbols-outlined text-sm">
                  {{ saldoVariation >= 0 ? 'trending_up' : 'trending_down' }}
                </span>
                <span class="text-sm ml-1">{{ formatPercentage(Math.abs(saldoVariation)) }}% este mês</span>
              </div>
            </div>
            <div
              class="bg-white p-5 rounded-lg shadow-md hover:shadow-lg transition-all duration-300 transform hover:translate-y-[-2px] border border-gray-100">
              <div class="flex justify-between items-center mb-3">
                <h3 class="font-semibold text-[#282641]">Receitas</h3>
                <span class="material-symbols-outlined text-green-500">arrow_upward</span>
              </div>
              <p class="text-3xl font-bold text-green-500">R$ {{ formatCurrency(dashboardData.entrada) }}</p>
              <div class="flex items-center mt-2 text-[#615c8e]">
                <span class="material-symbols-outlined text-sm">calendar_today</span>
                <span class="text-sm ml-1">Último mês: R$ {{ formatCurrency(lastMonthEntrada) }}</span>
              </div>
            </div>
            <div
              class="bg-white p-5 rounded-lg shadow-md hover:shadow-lg transition-all duration-300 transform hover:translate-y-[-2px] border border-gray-100">
              <div class="flex justify-between items-center mb-3">
                <h3 class="font-semibold text-[#282641]">Despesas</h3>
                <span class="material-symbols-outlined text-red-500">arrow_downward</span>
              </div>
              <p class="text-3xl font-bold text-red-500">R$ {{ formatCurrency(dashboardData.saida) }}</p>
              <div class="flex items-center mt-2 text-[#615c8e]">
                <span class="material-symbols-outlined text-sm">calendar_today</span>
                <span class="text-sm ml-1">Último mês: R$ {{ formatCurrency(lastMonthSaida) }}</span>
              </div>
            </div>
          </div>

          <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-8">
            <div
              class="bg-white p-5 rounded-lg shadow-md lg:col-span-2 hover:shadow-lg transition-all duration-300 border border-gray-100">
              <div class="flex justify-between items-center mb-5">
                <h3 class="font-semibold text-[#282641]">Gastos por Categoria</h3>
                <span class="text-sm text-[#615c8e]">{{ periodLabel }}</span>
              </div>
              <div class="h-[300px]">
                <div id="category-chart" ref="categoryChart"></div>
              </div>
            </div>
            <div
              class="bg-white p-5 rounded-lg shadow-md hover:shadow-lg transition-all duration-300 border border-gray-100">
              <div class="flex justify-between items-center mb-5">
                <h3 class="font-semibold text-[#282641]">Distribuição de Gastos (%)</h3>
                <span
                  class="material-symbols-outlined text-[#615c8e] cursor-pointer hover:text-[#282641] transition-colors hover:rotate-90 duration-300">more_vert</span>
              </div>
              <div class="h-[300px]">
                <div id="donut-chart" ref="donutChart"></div>
              </div>
            </div>
          </div>

          <div class="grid grid-cols-1 lg:grid-cols-2 gap-4 md:gap-6">
            <div
              class="bg-white p-5 rounded-lg shadow-md hover:shadow-lg transition-all duration-300 border border-gray-100">
              <div class="flex justify-between items-center mb-5">
                <h3 class="font-semibold text-[#282641]">Evolução Financeira</h3>
                <span class="text-sm text-[#615c8e]">{{ periodLabel }}</span>
              </div>
              <div class="h-[300px]">
                <div id="line-chart" ref="lineChart"></div>
              </div>
            </div>
            <div class="bg-white p-5 rounded-lg shadow-md hover:shadow-lg transition-shadow">
              <div class="flex justify-between items-center mb-5">
                <h3 class="font-semibold text-[#282641]">Pessoas</h3>
                <button
                  class="text-[#615c8e] hover:text-[#282641] transition-colors duration-300 bg-[#eed4ed]/10 p-2 rounded-full hover:bg-[#eed4ed]/20">
                  <span class="material-symbols-outlined">person_add</span>
                </button>
              </div>
              <div
                class="space-y-4 max-h-[300px] overflow-y-auto pr-2 scrollbar-thin scrollbar-thumb-[#a79de9] scrollbar-track-gray-100">
                <div v-for="person in sharedPeople" :key="person.id"
                  class="flex items-center justify-between p-3 border border-gray-100 rounded-lg hover:bg-[#eed4ed]/10 transition-colors duration-200 cursor-pointer transform hover:scale-[1.02]">
                  <div class="flex items-center space-x-3">
                    <div class="w-10 h-10 rounded-full bg-[#615c8e] text-white flex items-center justify-center">
                      <span>{{ getInitials(person.name) }}</span>
                    </div>
                    <div>
                      <p class="font-medium text-[#282641]">{{ person.name }}</p>
                      <p class="text-sm text-[#615c8e]">{{ person.relationship }}</p>
                    </div>
                  </div>
                  <div class="text-right">
                    <p class="font-semibold text-[#282641]">R$ {{ formatCurrency(person.amount) }}</p>
                    <p :class="['text-sm', person.trend >= 0 ? 'text-green-500' : 'text-red-500']">
                      {{ person.trend >= 0 ? '+' : '' }}{{ formatPercentage(person.trend) }}%
                    </p>
                  </div>
                </div>
                <button
                  class="w-full py-2 text-[#615c8e] border border-dashed border-[#615c8e] rounded-lg hover:bg-[#eed4ed]/20 transition-all duration-300 transform hover:translate-y-[-2px]">
                  Adicionar nova pessoa
                </button>
              </div>
            </div>
          </div>
        </div>

        <!-- Empty state -->
        <div v-if="!loading && !error && !hasData" class="text-center py-12">
          <span class="material-symbols-outlined text-[#615c8e] text-6xl">analytics</span>
          <h3 class="text-xl font-semibold text-[#282641] mt-4">Nenhum dado disponível</h3>
          <p class="text-[#615c8e] mt-2">Comece adicionando suas primeiras transações</p>
          <button
            @click="$router.push('/lancamento')"
            class="mt-4 bg-[#615c8e] text-white px-6 py-2 rounded-md hover:bg-[#282641] transition-colors">
            Adicionar Primeira Transação
            </button>
        </div>
      </main>
      <Footer />
    </div>
  </div>
</template>

<script>
import ApexCharts from 'apexcharts';
import Header from '../components/Header.vue';
import Footer from '../components/Footer.vue';

export default {
  name: 'HomePainel',
  components: {
    Header,
    Footer,
  },
  data() {
    return {
      apiUrl: process.env.VUE_APP_API_URL,
      user: {
        id: null,
        email: '',
        full_name: '',
      },
      loading: true,
      error: null,
      selectedPeriod: 'this_month',
      dashboardData: {
        entrada: 0,
        saida: 0,
        saldo_total: 0
      },
      categoriasGasto: [],
      categoriasPercentual: [],
      graficoMensal: [],
      charts: {
        category: null,
        donut: null,
        line: null
      },
      sharedPeople: [
        { id: 1, name: 'João Damasceno', relationship: 'Cônjuge', amount: 3200, trend: 8 },
        { id: 2, name: 'Maria Silva', relationship: 'Filha', amount: 850, trend: -3 },
        { id: 3, name: 'Pedro Oliveira', relationship: 'Filho', amount: 1200, trend: 5 }
      ],
      lastMonthEntrada: 0,
      lastMonthSaida: 0,
      saldoVariation: 0
    };
  },
  computed: {
    hasData() {
      return this.categoriasGasto.length > 0 && this.graficoMensal.length > 0;
    },
    periodLabel() {
      const labels = {
        'this_month': 'Este Mês',
        'last_month': 'Mês Anterior',
        'last_3_months': 'Últimos 3 Meses',
        'last_6_months': 'Últimos 6 Meses',
        'this_year': 'Este Ano',
        'last_year': 'Ano Anterior'
      };
      return labels[this.selectedPeriod] || 'Período';
    }
  },
  async mounted() {
    await this.fetchUserData();
    await this.fetchDashboardData();
  },
  beforeUnmount() {
    this.destroyCharts();
  },
  methods: {
    formatCurrency(value) {
      return new Intl.NumberFormat('pt-BR', {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2
      }).format(value);
    },
    
    formatPercentage(value) {
      return new Intl.NumberFormat('pt-BR', {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2
      }).format(value);
    },
    
    getInitials(name) {
      return name.split(' ').map(word => word[0]).join('').toUpperCase().substring(0, 2);
    },

    async fetchUserData() {
      try {
        const token = localStorage.getItem('token');
        if (!token) {
          this.$router.push({ name: 'painel' });
          return;
        }

        const response = await fetch(`${this.apiUrl}/account/check_auth/`, {
          method: 'GET',
          headers: {
            'Authorization': `Token ${token}`,
          },
        });

        if (response.ok) {
          const data = await response.json();
          this.user = data.user;
        } else {
          localStorage.removeItem('token');
          this.$router.push({ name: 'painel' });
        }
      } catch (error) {
        console.error('Erro ao buscar dados do usuário:', error);
        this.$router.push({ name: 'painel' });
      }
    },

    async fetchDashboardData() {
      this.loading = true;
      this.error = null;
      
      try {
        const token = localStorage.getItem('token');
        const response = await fetch(`${this.apiUrl}/api/dashboard/?period=${this.selectedPeriod}`, {
          method: 'GET',
          headers: {
            'Authorization': `Token ${token}`,
          },
        });

        if (response.ok) {
          const data = await response.json();
          this.dashboardData = data.dashboard;
          this.categoriasGasto = data.categorias_gasto || [];
          this.categoriasPercentual = data.categorias_percentual || [];
          this.graficoMensal = data.grafico_mensal || [];
          
          this.calculateVariations();
          this.calculatePercentages();
          
          await this.$nextTick();
          this.renderCharts();
        } else {
          throw new Error('Erro ao carregar dados do dashboard');
        }
      } catch (error) {
        console.error('Erro ao buscar dados do dashboard:', error);
        this.error = error.message;
      } finally {
        this.loading = false;
      }
    },

    calculatePercentages() {
      const totalGasto = this.categoriasGasto.reduce((sum, cat) => sum + parseFloat(cat.gasto || 0), 0);
      
      this.categoriasPercentual = this.categoriasGasto.map(cat => {
        const gasto = parseFloat(cat.gasto || 0);
        const percentual = totalGasto > 0 ? (gasto / totalGasto) * 100 : 0;
        return {
          ...cat,
          percentual: parseFloat(percentual.toFixed(2))
        };
      });
    },

    calculateVariations() {
      if (this.graficoMensal.length >= 2) {
        const currentMonth = this.graficoMensal[this.graficoMensal.length - 1];
        const previousMonth = this.graficoMensal[this.graficoMensal.length - 2];
        
        this.lastMonthEntrada = previousMonth.entrada || 0;
        this.lastMonthSaida = previousMonth.saida || 0;
        
        const currentSaldo = (currentMonth.entrada || 0) - (currentMonth.saida || 0);
        const previousSaldo = (previousMonth.entrada || 0) - (previousMonth.saida || 0);
        
        if (previousSaldo !== 0) {
          this.saldoVariation = ((currentSaldo - previousSaldo) / Math.abs(previousSaldo)) * 100;
        } else {
          this.saldoVariation = 0;
        }
      }
    },

    destroyCharts() {
      Object.values(this.charts).forEach(chart => {
        if (chart) {
          try {
            chart.destroy();
          } catch (error) {
            console.warn('Erro ao destruir gráfico:', error);
          }
        }
      });
      this.charts = { category: null, donut: null, line: null };
    },

    renderCharts() {
      setTimeout(() => {
        this.destroyCharts();
        
        // Gráfico de barras - Gastos por categoria
        if (this.$refs.categoryChart && this.categoriasGasto.length > 0) {
          try {
            const categoryOptions = {
              chart: {
                type: "bar",
                height: "280",
                toolbar: { show: false }
              },
              colors: ["#615c8e"],
              plotOptions: { 
                bar: { 
                  borderRadius: 4, 
                  horizontal: true 
                } 
              },
              dataLabels: { enabled: false },
              xaxis: { 
                categories: this.categoriasGasto.map(cat => cat.categoria),
                labels: {
                  formatter: (val) => {
                    return 'R$ ' + val.toLocaleString('pt-BR', { 
                      minimumFractionDigits: 2,
                      maximumFractionDigits: 2 
                    });
                  }
                }
              },
              grid: { borderColor: "#f5f5f5" },
              tooltip: { 
                theme: "light",
                y: {
                  formatter: (val) => {
                    return 'R$ ' + val.toLocaleString('pt-BR', { 
                      minimumFractionDigits: 2,
                      maximumFractionDigits: 2 
                    });
                  }
                }
              },
              series: [{ 
                name: "Gastos", 
                data: this.categoriasGasto.map(cat => parseFloat(cat.gasto) || 0)
              }]
            };

            this.charts.category = new ApexCharts(this.$refs.categoryChart, categoryOptions);
            this.charts.category.render();
          } catch (error) {
            console.error('Erro ao renderizar gráfico de categoria:', error);
          }
        }

        // Gráfico de pizza - Distribuição de gastos em %
        if (this.$refs.donutChart && this.categoriasPercentual.length > 0) {
          try {
            const donutOptions = {
              chart: {
                type: "donut",
                height: "280",
                toolbar: { show: false }
              },
              colors: ["#282641", "#3f3d63", "#615c8e", "#8580b0", "#a79de9", "#eed4ed"],
              labels: this.categoriasPercentual.map(cat => cat.categoria),
              legend: { 
                position: "bottom"
              },
              dataLabels: {
                enabled: true,
                formatter: function(val) {
                  return val.toFixed(1) + '%';
                },
                style: {
                  fontSize: '12px',
                  fontWeight: 'bold',
                  colors: ['white']
                }
              },
              tooltip: { 
                theme: "light"
              },
              series: this.categoriasPercentual.map(cat => cat.percentual)
            };

            this.charts.donut = new ApexCharts(this.$refs.donutChart, donutOptions);
            this.charts.donut.render();
          } catch (error) {
            console.error('Erro ao renderizar gráfico de pizza:', error);
          }
        }

        // Gráfico de linha - Gastos x Receitas
        if (this.$refs.lineChart && this.graficoMensal.length > 0) {
          try {
            const lineOptions = {
              chart: {
                type: "line",
                height: "280",
                toolbar: { show: false }
              },
              colors: ["#615c8e", "#a79de9"],
              stroke: { curve: "smooth", width: 3 },
              xaxis: { 
                categories: this.graficoMensal.map(item => item.mes_ano)
              },
              markers: { size: 4, hover: { size: 6 } },
              grid: { borderColor: "#f5f5f5" },
              tooltip: { 
                theme: "light",
                y: {
                  formatter: (val) => {
                    return 'R$ ' + val.toLocaleString('pt-BR', { 
                      minimumFractionDigits: 2,
                      maximumFractionDigits: 2 
                    });
                  }
                }
              },
              series: [
                { 
                  name: "Receitas", 
                  data: this.graficoMensal.map(item => parseFloat(item.entrada) || 0)
                },
                { 
                  name: "Despesas", 
                  data: this.graficoMensal.map(item => parseFloat(item.saida) || 0)
                }
              ]
            };

            this.charts.line = new ApexCharts(this.$refs.lineChart, lineOptions);
            this.charts.line.render();
          } catch (error) {
            console.error('Erro ao renderizar gráfico de linha:', error);
          }
        }
      }, 100);
    },

    async logout() {
      try {
        const token = localStorage.getItem('token');
        await fetch(`${this.apiUrl}/account/logout/`, {
          method: 'POST',
          headers: {
            'Authorization': `Token ${token}`,
          },
        });

        localStorage.removeItem('token');
        this.$router.push({ name: 'painel' });
      } catch (err) {
        console.error('Erro ao fazer logout:', err);
      }
    }
  }
};
</script>

<style scoped>
@import url(https://fonts.googleapis.com/css2?family=Lato&display=swap);
@import url(https://fonts.googleapis.com/css2?family=Open+Sans&display=swap);
@import url(https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200);

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


#painelhome :is(.space-x-1 > :not([hidden]) ~ :not([hidden])) {
  --tw-space-x-reverse: 0;
  margin-left: calc(4px * (1 - var(--tw-space-x-reverse)));
  margin-right: calc(4px * var(--tw-space-x-reverse));
}

#painelhome :is(.space-x-2 > :not([hidden]) ~ :not([hidden])) {
  --tw-space-x-reverse: 0;
  margin-left: calc(8px * (1 - var(--tw-space-x-reverse)));
  margin-right: calc(8px * var(--tw-space-x-reverse));
}

#painelhome :is(.space-x-3 > :not([hidden]) ~ :not([hidden])) {
  --tw-space-x-reverse: 0;
  margin-left: calc(12px * (1 - var(--tw-space-x-reverse)));
  margin-right: calc(12px * var(--tw-space-x-reverse));
}

#painelhome :is(.space-x-6 > :not([hidden]) ~ :not([hidden])) {
  --tw-space-x-reverse: 0;
  margin-left: calc(24px * (1 - var(--tw-space-x-reverse)));
  margin-right: calc(24px * var(--tw-space-x-reverse));
}

#painelhome :is(.space-y-4 > :not([hidden]) ~ :not([hidden])) {
  --tw-space-y-reverse: 0;
  margin-bottom: calc(16px * var(--tw-space-y-reverse));
  margin-top: calc(16px * (1 - var(--tw-space-y-reverse)));
}

#painelhome .overflow-hidden {
  overflow: hidden;
}

#painelhome .overflow-y-auto {
  overflow-y: auto;
}

#painelhome .rounded {
  border-radius: 12px;
}

#painelhome .rounded-full {
  border-radius: 9999px;
}

#painelhome .rounded-lg {
  border-radius: 24px;
}

#painelhome .rounded-md {
  border-radius: 18px;
}

#painelhome .border {
  border-width: 1px;
}

#painelhome .border-dashed {
  border-style: dashed;
}

#painelhome .border-\[\#615c8e\] {
  --tw-border-opacity: 1;
  border-color: rgb(97 92 142 / var(--tw-border-opacity));
}

#painelhome .border-gray-100 {
  --tw-border-opacity: 1;
  border-color: rgb(243 244 246 / var(--tw-border-opacity));
}

#painelhome .border-gray-300 {
  --tw-border-opacity: 1;
  border-color: rgb(209 213 219 / var(--tw-border-opacity));
}

#painelhome .bg-\[\#282641\] {
  --tw-bg-opacity: 1;
  background-color: rgb(40 38 65 / var(--tw-bg-opacity));
}

#painelhome .bg-\[\#615c8e\] {
  --tw-bg-opacity: 1;
  background-color: rgb(97 92 142 / var(--tw-bg-opacity));
}

#painelhome .bg-\[\#a79de9\] {
  --tw-bg-opacity: 1;
  background-color: rgb(167 157 233 / var(--tw-bg-opacity));
}

#painelhome .bg-\[\#eed4ed\] {
  --tw-bg-opacity: 1;
  background-color: rgb(238 212 237 / var(--tw-bg-opacity));
}

#painelhome .bg-\[\#eed4ed\]\/10 {
  background-color: rgba(238, 212, 237, 0.1);
}

#painelhome .bg-white {
  --tw-bg-opacity: 1;
  background-color: rgb(255 255 255 / var(--tw-bg-opacity));
}

#painelhome .p-2 {
  padding: 8px;
}

#painelhome .p-3 {
  padding: 12px;
}

#painelhome .p-4 {
  padding: 16px;
}

#painelhome .p-5 {
  padding: 20px;
}

#painelhome .px-2 {
  padding-left: 8px;
  padding-right: 8px;
}

#painelhome .px-4 {
  padding-left: 16px;
  padding-right: 16px;
}

#painelhome .px-6 {
  padding-left: 24px;
  padding-right: 24px;
}

#painelhome .py-1 {
  padding-bottom: 4px;
  padding-top: 4px;
}

#painelhome .py-2 {
  padding-bottom: 8px;
  padding-top: 8px;
}

#painelhome .pr-2 {
  padding-right: 8px;
}

#painelhome .text-right {
  text-align: right;
}

#painelhome .font-sans {
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

#painelhome .text-2xl {
  font-size: 24px;
  line-height: 31.200000000000003px;
}

#painelhome .text-3xl {
  font-size: 30px;
  line-height: 36px;
}

#painelhome .text-sm {
  font-size: 14px;
  line-height: 21px;
}

#painelhome .text-xl {
  font-size: 20px;
  line-height: 28px;
}

#painelhome .font-bold {
  font-weight: 700;
}

#painelhome .font-medium {
  font-weight: 500;
}

#painelhome .font-semibold {
  font-weight: 600;
}

#painelhome .tracking-tight {
  letter-spacing: -0.025em;
}

#painelhome .text-\[\#120907\] {
  --tw-text-opacity: 1;
  color: rgb(18 9 7 / var(--tw-text-opacity));
}

#painelhome .text-\[\#282641\] {
  --tw-text-opacity: 1;
  color: rgb(40 38 65 / var(--tw-text-opacity));
}

#painelhome .text-\[\#615c8e\] {
  --tw-text-opacity: 1;
  color: rgb(97 92 142 / var(--tw-text-opacity));
}

#painelhome .text-\[\#a79de9\] {
  --tw-text-opacity: 1;
  color: rgb(167 157 233 / var(--tw-text-opacity));
}

#painelhome .text-green-500 {
  --tw-text-opacity: 1;
  color: rgb(34 197 94 / var(--tw-text-opacity));
}

#painelhome .text-red-500 {
  --tw-text-opacity: 1;
  color: rgb(239 68 68 / var(--tw-text-opacity));
}

#painelhome .text-white {
  --tw-text-opacity: 1;
  color: rgb(255 255 255 / var(--tw-text-opacity));
}

#painelhome .shadow-lg {
  --tw-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.1);
  --tw-shadow-colored: 0 10px 15px -3px var(--tw-shadow-color), 0 4px 6px -4px var(--tw-shadow-color);
}

#painelhome .shadow-lg,
#painelhome .shadow-md {
  box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
}

#painelhome .shadow-md {
  --tw-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.1);
  --tw-shadow-colored: 0 4px 6px -1px var(--tw-shadow-color), 0 2px 4px -2px var(--tw-shadow-color);
}

#painelhome .transition-all {
  transition-duration: 0.15s;
  transition-property: all;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
}

#painelhome .transition-colors {
  transition-duration: 0.15s;
  transition-property: color, background-color, border-color, text-decoration-color, fill, stroke;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
}

#painelhome .transition-shadow {
  transition-duration: 0.15s;
  transition-property: box-shadow;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
}

#painelhome .duration-200 {
  transition-duration: 0.2s;
}

#painelhome .duration-300 {
  transition-duration: 0.3s;
}

#painelhome {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  overflow-y: auto;
  background: linear-gradient(135deg, #ffffff, #d4d4d4);
}

#painelhome .hover\:translate-y-\[-2px\]:hover {
  --tw-translate-y: -2px;
}

#painelhome .hover\:rotate-90:hover,
#painelhome .hover\:translate-y-\[-2px\]:hover {
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

#painelhome .hover\:rotate-90:hover {
  --tw-rotate: 90deg;
}

#painelhome .hover\:scale-105:hover {
  --tw-scale-x: 1.05;
  --tw-scale-y: 1.05;
}

#painelhome .hover\:scale-105:hover,
#painelhome .hover\:scale-\[1\.02\]:hover {
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

#painelhome .hover\:scale-\[1\.02\]:hover {
  --tw-scale-x: 1.02;
  --tw-scale-y: 1.02;
}

#painelhome .hover\:bg-\[\#615c8e\]:hover {
  --tw-bg-opacity: 1;
  background-color: rgb(97 92 142 / var(--tw-bg-opacity));
}

#painelhome .hover\:bg-\[\#eed4ed\]:hover {
  --tw-bg-opacity: 1;
  background-color: rgb(238 212 237 / var(--tw-bg-opacity));
}

#painelhome .hover\:bg-\[\#eed4ed\]\/10:hover {
  background-color: rgba(238, 212, 237, 0.1);
}

#painelhome .hover\:bg-\[\#eed4ed\]\/20:hover {
  background-color: rgba(238, 212, 237, 0.2);
}

#painelhome .hover\:text-\[\#282641\]:hover {
  --tw-text-opacity: 1;
  color: rgb(40 38 65 / var(--tw-text-opacity));
}

#painelhome .hover\:text-\[\#a79de9\]:hover {
  --tw-text-opacity: 1;
  color: rgb(167 157 233 / var(--tw-text-opacity));
}

#painelhome .hover\:shadow-lg:hover {
  --tw-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.1);
  --tw-shadow-colored: 0 10px 15px -3px var(--tw-shadow-color), 0 4px 6px -4px var(--tw-shadow-color);
  box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
}

#painelhome .hover\:ring-2:hover {
  --tw-ring-offset-shadow: var(--tw-ring-inset) 0 0 0 var(--tw-ring-offset-width) var(--tw-ring-offset-color);
  --tw-ring-shadow: var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color);
  box-shadow: var(--tw-ring-offset-shadow), var(--tw-ring-shadow), var(--tw-shadow, 0 0 #0000);
}

#painelhome .hover\:ring-\[\#a79de9\]:hover {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(167 157 233 / var(--tw-ring-opacity));
}

#painelhome .focus\:outline-none:focus {
  outline: 2px solid transparent;
  outline-offset: 2px;
}

#painelhome .focus\:ring-2:focus {
  --tw-ring-offset-shadow: var(--tw-ring-inset) 0 0 0 var(--tw-ring-offset-width) var(--tw-ring-offset-color);
  --tw-ring-shadow: var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color);
  box-shadow: var(--tw-ring-offset-shadow), var(--tw-ring-shadow), var(--tw-shadow, 0 0 #0000);
}

#painelhome .focus\:ring-\[\#a79de9\]:focus {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(167 157 233 / var(--tw-ring-opacity));
}

#painelhome :is(.group:hover .group-hover\:text-\[\#a79de9\]) {
  --tw-text-opacity: 1;
  color: rgb(167 157 233 / var(--tw-text-opacity));
}

@media (min-width: 768px) {
  #painelhome .md\:grid-cols-3 {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }

  #painelhome .md\:gap-6 {
    gap: 24px;
  }

  #painelhome .md\:p-6 {
    padding: 24px;
  }

  #painelhome .md\:text-2xl {
    font-size: 24px;
    line-height: 31.200000000000003px;
  }
}

@media (min-width: 1024px) {
  #painelhome .lg\:col-span-2 {
    grid-column: span 2 / span 2;
  }

  #painelhome .lg\:grid-cols-2 {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  #painelhome .lg\:grid-cols-3 {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }
}

html {
  background: linear-gradient(135deg, #ffffff, #d4d4d4);
  min-height: 100%;
}

body {
  margin: 0;
  min-height: 100vh;
}
</style>