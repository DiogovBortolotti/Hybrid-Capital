<template>
  <div id="webcrumbs">
    <div class="min-h-screen flex flex-col bg-[#eed4ed]/10">
      <header class="bg-[#282641] text-white p-4 shadow-md">
        <div class="container mx-auto flex justify-between items-center">
          <div class="flex items-center space-x-2">
            <span class="material-symbols-outlined text-2xl">account_balance</span>
            <h1 class="text-xl font-bold">FinanceTracker</h1>
          </div>
          <nav class="hidden md:flex space-x-6">
            <a class="hover:text-[#a79de9] transition-colors duration-300" href="#">Dashboard</a>
            <a class="hover:text-[#a79de9] transition-colors duration-300" href="#">Transações</a>
            <a class="hover:text-[#a79de9] transition-colors duration-300" href="#">Investimentos</a>
            <a class="hover:text-[#a79de9] transition-colors duration-300" href="#">Relatórios</a>
          </nav>
          <div class="flex items-center space-x-2">
            <button class="p-2 rounded-full hover:bg-[#615c8e] transition-colors duration-300">
              <span class="material-symbols-outlined">notifications</span>
            </button>
            <div class="w-8 h-8 bg-[#a79de9] rounded-full flex items-center justify-center">
              <span class="text-sm font-bold">JS</span>
            </div>
          </div>
        </div>
      </header>

      <main class="flex-grow p-4 md:p-6 container mx-auto">
        <!-- Cabeçalho com boas-vindas e botões -->
        <div class="flex items-center justify-between mb-8">
          <div>
            <h2 class="text-2xl font-bold text-[#282641]">Bem-vindo de volta, João Silva!</h2>
            <p class="text-[#615c8e]">Resumo dos seus investimentos - Mês Atual</p>
          </div>
          <div class="flex gap-4">
            <button
              class="bg-[#282641] text-white px-6 py-2 rounded-md hover:bg-[#615c8e] transition-colors duration-300 flex items-center space-x-2 shadow-md hover:shadow-lg transform hover:translate-y-[-2px]"
            >
              <span class="material-symbols-outlined">add</span>
              <span>Novo Investimento</span>
            </button>
            <button
              class="bg-[#282641] text-white px-6 py-2 rounded-md hover:bg-[#615c8e] transition-colors duration-300 flex items-center space-x-2 shadow-md hover:shadow-lg transform hover:translate-y-[-2px]"
            >
              <span class="material-symbols-outlined">details</span>
              <span>Histórico</span>
            </button>
          </div>
        </div>

        <!-- Filtro de período -->
        <div class="flex justify-end mb-6">
          <select
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

        <!-- Cards de métricas -->
        <div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-6 gap-4 md:gap-6 mb-8">
          <div
            class="bg-white p-5 rounded-lg shadow-md hover:shadow-lg transition-all duration-300 transform hover:translate-y-[-2px] border border-gray-100 md:col-span-1 lg:col-span-1"
          >
            <div class="flex justify-between items-center mb-3">
              <h3 class="font-semibold text-[#282641]">Portfolio Total</h3>
              <span class="material-symbols-outlined text-[#615c8e]">account_balance_wallet</span>
            </div>
            <p class="text-3xl font-bold text-[#282641]">R$ 348.950,00</p>
            <div class="flex items-center mt-2 text-green-500">
              <span class="material-symbols-outlined text-sm">trending_up</span>
              <span class="text-sm ml-1">8.5% este mês</span>
            </div>
          </div>

          <div
            class="bg-white p-5 rounded-lg shadow-md hover:shadow-lg transition-all duration-300 transform hover:translate-y-[-2px] border border-gray-100"
          >
            <div class="flex justify-between items-center mb-3">
              <h3 class="font-semibold text-[#282641]">Ações</h3>
              <span class="material-symbols-outlined text-[#615c8e]">trending_up</span>
            </div>
            <p class="text-3xl font-bold text-[#282641]">R$ 95.230,00</p>
            <div class="flex items-center mt-2 text-green-500">
              <span class="material-symbols-outlined text-sm">trending_up</span>
              <span class="text-sm ml-1">7.8% este mês</span>
            </div>
          </div>

          <div
            class="bg-white p-5 rounded-lg shadow-md hover:shadow-lg transition-all duration-300 transform hover:translate-y-[-2px] border border-gray-100"
          >
            <div class="flex justify-between items-center mb-3">
              <h3 class="font-semibold text-[#282641]">FIIs</h3>
              <span class="material-symbols-outlined text-[#615c8e]">apartment</span>
            </div>
            <p class="text-3xl font-bold text-[#282641]">R$ 73.500,00</p>
            <div class="flex items-center mt-2 text-green-500">
              <span class="material-symbols-outlined text-sm">trending_up</span>
              <span class="text-sm ml-1">6.2% este mês</span>
            </div>
          </div>

          <div
            class="bg-white p-5 rounded-lg shadow-md hover:shadow-lg transition-all duration-300 transform hover:translate-y-[-2px] border border-gray-100"
          >
            <div class="flex justify-between items-center mb-3">
              <h3 class="font-semibold text-[#282641]">Criptomoedas</h3>
              <span class="material-symbols-outlined text-[#615c8e]">currency_bitcoin</span>
            </div>
            <p class="text-3xl font-bold text-[#282641]">R$ 85.730,00</p>
            <div class="flex items-center mt-2 text-green-500">
              <span class="material-symbols-outlined text-sm">trending_up</span>
              <span class="text-sm ml-1">12.3% este mês</span>
            </div>
          </div>

          <div
            class="bg-white p-5 rounded-lg shadow-md hover:shadow-lg transition-all duration-300 transform hover:translate-y-[-2px] border border-gray-100"
          >
            <div class="flex justify-between items-center mb-3">
              <h3 class="font-semibold text-[#282641]">Tesouro/Selic</h3>
              <span class="material-symbols-outlined text-[#615c8e]">savings</span>
            </div>
            <p class="text-3xl font-bold text-[#282641]">R$ 54.470,00</p>
            <div class="flex items-center mt-2 text-green-500">
              <span class="material-symbols-outlined text-sm">trending_up</span>
              <span class="text-sm ml-1">1.8% este mês</span>
            </div>
          </div>

          <div
            class="bg-white p-5 rounded-lg shadow-md hover:shadow-lg transition-all duration-300 transform hover:translate-y-[-2px] border border-gray-100"
          >
            <div class="flex justify-between items-center mb-3">
              <h3 class="font-semibold text-[#282641]">Poupança</h3>
              <span class="material-symbols-outlined text-[#615c8e]">account_balance</span>
            </div>
            <p class="text-3xl font-bold text-[#282641]">R$ 40.020,00</p>
            <div class="flex items-center mt-2 text-red-500">
              <span class="material-symbols-outlined text-sm">trending_down</span>
              <span class="text-sm ml-1">0.5% este mês</span>
            </div>
          </div>
        </div>

        <!-- Gráficos -->
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-8">
          <div
            class="bg-white p-5 rounded-lg shadow-md lg:col-span-2 hover:shadow-lg transition-all duration-300 border border-gray-100"
          >
            <div class="flex justify-between items-center mb-5">
              <h3 class="font-semibold text-[#282641]">Desempenho dos Investimentos</h3>
              <span class="text-sm text-[#615c8e]">Últimos 6 Meses</span>
            </div>
            <div class="h-[300px]">
              <div data-chart="chart_0"></div>
            </div>
          </div>

          <div
            class="bg-white p-5 rounded-lg shadow-md hover:shadow-lg transition-all duration-300 border border-gray-100"
          >
            <div class="flex justify-between items-center mb-5">
              <h3 class="font-semibold text-[#282641]">Distribuição de Ativos</h3>
              <span
                class="material-symbols-outlined text-[#615c8e] cursor-pointer hover:text-[#282641] transition-colors hover:rotate-90 duration-300"
              >
                more_vert
              </span>
            </div>
            <div class="h-[300px]">
              <div data-chart="chart_1"></div>
            </div>
          </div>
        </div>

        <!-- Carteiras -->
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-4 md:gap-6 mb-8">
          <!-- Carteira de Ações -->
          <div
            class="bg-white p-5 rounded-lg shadow-md hover:shadow-lg transition-all duration-300 border border-gray-100"
          >
            <div class="flex justify-between items-center mb-5">
              <h3 class="font-semibold text-[#282641]">Carteira de Ações</h3>
              <button
                class="text-[#615c8e] hover:text-[#282641] transition-colors duration-300 bg-[#eed4ed]/10 p-2 rounded-full hover:bg-[#eed4ed]/20"
              >
                <span class="material-symbols-outlined">add</span>
              </button>
            </div>
            <div class="space-y-4 max-h-[300px] overflow-y-auto pr-2">
              <div
                class="flex items-center justify-between p-3 border border-gray-100 rounded-lg hover:bg-[#eed4ed]/10 transition-colors duration-200 cursor-pointer transform hover:scale-[1.02]"
              >
                <div class="flex items-center space-x-3">
                  <div class="w-10 h-10 rounded-full bg-blue-100 flex items-center justify-center">
                    <span class="material-symbols-outlined text-blue-600">business</span>
                  </div>
                  <div>
                    <p class="font-medium text-[#282641]">PETR4</p>
                    <p class="text-sm text-[#615c8e]">Petrobras</p>
                  </div>
                </div>
                <div class="text-right">
                  <p class="font-semibold text-[#282641]">R$ 38.250,00</p>
                  <p class="text-sm text-green-500">+5.8%</p>
                </div>
              </div>

              <div
                class="flex items-center justify-between p-3 border border-gray-100 rounded-lg hover:bg-[#eed4ed]/10 transition-colors duration-200 cursor-pointer transform hover:scale-[1.02]"
              >
                <div class="flex items-center space-x-3">
                  <div class="w-10 h-10 rounded-full bg-yellow-100 flex items-center justify-center">
                    <span class="material-symbols-outlined text-yellow-600">local_atm</span>
                  </div>
                  <div>
                    <p class="font-medium text-[#282641]">ITUB4</p>
                    <p class="text-sm text-[#615c8e]">Itaú Unibanco</p>
                  </div>
                </div>
                <div class="text-right">
                  <p class="font-semibold text-[#282641]">R$ 32.480,00</p>
                  <p class="text-sm text-green-500">+4.2%</p>
                </div>
              </div>

              <div
                class="flex items-center justify-between p-3 border border-gray-100 rounded-lg hover:bg-[#eed4ed]/10 transition-colors duration-200 cursor-pointer transform hover:scale-[1.02]"
              >
                <div class="flex items-center space-x-3">
                  <div class="w-10 h-10 rounded-full bg-green-100 flex items-center justify-center">
                    <span class="material-symbols-outlined text-green-600">shopping_cart</span>
                  </div>
                  <div>
                    <p class="font-medium text-[#282641]">MGLU3</p>
                    <p class="text-sm text-[#615c8e]">Magazine Luiza</p>
                  </div>
                </div>
                <div class="text-right">
                  <p class="font-semibold text-[#282641]">R$ 24.500,00</p>
                  <p class="text-sm text-red-500">-2.3%</p>
                </div>
              </div>
            </div>
          </div>

          <!-- Carteira de FIIs -->
          <div
            class="bg-white p-5 rounded-lg shadow-md hover:shadow-lg transition-all duration-300 border border-gray-100"
          >
            <div class="flex justify-between items-center mb-5">
              <h3 class="font-semibold text-[#282641]">Carteira de FIIs</h3>
              <button
                class="text-[#615c8e] hover:text-[#282641] transition-colors duration-300 bg-[#eed4ed]/10 p-2 rounded-full hover:bg-[#eed4ed]/20"
              >
                <span class="material-symbols-outlined">add</span>
              </button>
            </div>
            <div class="space-y-4 max-h-[300px] overflow-y-auto pr-2">
              <div
                class="flex items-center justify-between p-3 border border-gray-100 rounded-lg hover:bg-[#eed4ed]/10 transition-colors duration-200 cursor-pointer transform hover:scale-[1.02]"
              >
                <div class="flex items-center space-x-3">
                  <div class="w-10 h-10 rounded-full bg-purple-100 flex items-center justify-center">
                    <span class="material-symbols-outlined text-purple-600">apartment</span>
                  </div>
                  <div>
                    <p class="font-medium text-[#282641]">KNRI11</p>
                    <p class="text-sm text-[#615c8e]">Kinea Renda Imobiliária</p>
                  </div>
                </div>
                <div class="text-right">
                  <p class="font-semibold text-[#282641]">R$ 25.850,00</p>
                  <p class="text-sm text-green-500">+5.2%</p>
                </div>
              </div>

              <div
                class="flex items-center justify-between p-3 border border-gray-100 rounded-lg hover:bg-[#eed4ed]/10 transition-colors duration-200 cursor-pointer transform hover:scale-[1.02]"
              >
                <div class="flex items-center space-x-3">
                  <div class="w-10 h-10 rounded-full bg-blue-100 flex items-center justify-center">
                    <span class="material-symbols-outlined text-blue-600">store</span>
                  </div>
                  <div>
                    <p class="font-medium text-[#282641]">HGLG11</p>
                    <p class="text-sm text-[#615c8e]">CSHG Logística</p>
                  </div>
                </div>
                <div class="text-right">
                  <p class="font-semibold text-[#282641]">R$ 20.450,00</p>
                  <p class="text-sm text-green-500">+3.8%</p>
                </div>
              </div>

              <div
                class="flex items-center justify-between p-3 border border-gray-100 rounded-lg hover:bg-[#eed4ed]/10 transition-colors duration-200 cursor-pointer transform hover:scale-[1.02]"
              >
                <div class="flex items-center space-x-3">
                  <div class="w-10 h-10 rounded-full bg-green-100 flex items-center justify-center">
                    <span class="material-symbols-outlined text-green-600">location_city</span>
                  </div>
                  <div>
                    <p class="font-medium text-[#282641]">VISC11</p>
                    <p class="text-sm text-[#615c8e]">Vinci Shopping Centers</p>
                  </div>
                </div>
                <div class="text-right">
                  <p class="font-semibold text-[#282641]">R$ 27.200,00</p>
                  <p class="text-sm text-green-500">+7.4%</p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Histórico de Transações -->
        <div
          class="bg-white p-5 rounded-lg shadow-md hover:shadow-lg transition-all duration-300 border border-gray-100 mb-8"
        >
          <div class="flex justify-between items-center mb-5">
            <h3 class="font-semibold text-[#282641]">Histórico de Transações</h3>
            <button class="text-[#615c8e] hover:text-[#282641] transition-colors duration-300">
              Ver tudo
            </button>
          </div>
          <div class="overflow-x-auto">
            <table class="w-full min-w-full">
              <thead>
                <tr class="bg-[#eed4ed]/10 text-[#282641]">
                  <th class="py-3 px-4 text-left">Data</th>
                  <th class="py-3 px-4 text-left">Tipo</th>
                  <th class="py-3 px-4 text-left">Ativo</th>
                  <th class="py-3 px-4 text-left">Quantidade</th>
                  <th class="py-3 px-4 text-left">Preço</th>
                  <th class="py-3 px-4 text-left">Valor Total</th>
                  <th class="py-3 px-4 text-left">Status</th>
                </tr>
              </thead>
              <tbody>
                <tr class="border-b border-gray-100 hover:bg-[#eed4ed]/10">
                  <td class="py-3 px-4">15/06/2023</td>
                  <td class="py-3 px-4 text-green-500">Compra</td>
                  <td class="py-3 px-4">PETR4</td>
                  <td class="py-3 px-4">200 ações</td>
                  <td class="py-3 px-4">R$ 28,75</td>
                  <td class="py-3 px-4">R$ 5.750,00</td>
                  <td class="py-3 px-4">
                    <span class="px-2 py-1 bg-green-100 text-green-800 rounded-md text-xs">Concluído</span>
                  </td>
                </tr>
                <tr class="border-b border-gray-100 hover:bg-[#eed4ed]/10">
                  <td class="py-3 px-4">12/06/2023</td>
                  <td class="py-3 px-4 text-green-500">Compra</td>
                  <td class="py-3 px-4">Bitcoin</td>
                  <td class="py-3 px-4">0.25 BTC</td>
                  <td class="py-3 px-4">R$ 148.320,00</td>
                  <td class="py-3 px-4">R$ 37.080,00</td>
                  <td class="py-3 px-4">
                    <span class="px-2 py-1 bg-green-100 text-green-800 rounded-md text-xs">Concluído</span>
                  </td>
                </tr>
                <tr class="border-b border-gray-100 hover:bg-[#eed4ed]/10">
                  <td class="py-3 px-4">10/06/2023</td>
                  <td class="py-3 px-4 text-green-500">Compra</td>
                  <td class="py-3 px-4">KNRI11</td>
                  <td class="py-3 px-4">150 cotas</td>
                  <td class="py-3 px-4">R$ 102,50</td>
                  <td class="py-3 px-4">R$ 15.375,00</td>
                  <td class="py-3 px-4">
                    <span class="px-2 py-1 bg-green-100 text-green-800 rounded-md text-xs">Concluído</span>
                  </td>
                </tr>
                <tr class="border-b border-gray-100 hover:bg-[#eed4ed]/10">
                  <td class="py-3 px-4">08/06/2023</td>
                  <td class="py-3 px-4 text-red-500">Venda</td>
                  <td class="py-3 px-4">Ethereum</td>
                  <td class="py-3 px-4">2.5 ETH</td>
                  <td class="py-3 px-4">R$ 9.850,00</td>
                  <td class="py-3 px-4">R$ 24.625,00</td>
                  <td class="py-3 px-4">
                    <span class="px-2 py-1 bg-green-100 text-green-800 rounded-md text-xs">Concluído</span>
                  </td>
                </tr>
                <tr class="border-b border-gray-100 hover:bg-[#eed4ed]/10">
                  <td class="py-3 px-4">05/06/2023</td>
                  <td class="py-3 px-4 text-green-500">Aplicação</td>
                  <td class="py-3 px-4">Tesouro Direto</td>
                  <td class="py-3 px-4">-</td>
                  <td class="py-3 px-4">-</td>
                  <td class="py-3 px-4">R$ 10.000,00</td>
                  <td class="py-3 px-4">
                    <span class="px-2 py-1 bg-green-100 text-green-800 rounded-md text-xs">Concluído</span>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script>
import { onMounted } from 'vue'
import ApexCharts from 'apexcharts'

export default {
  name: 'FinanceDashboard',
  setup() {
    onMounted(() => {
      // Gráfico de linha - Desempenho dos Investimentos
      new ApexCharts(document.querySelector('[data-chart="chart_0"]'), {
        chart: {
          type: "line",
          width: "100%",
          height: "300",
          toolbar: { show: false }
        },
        colors: ["#615c8e", "#a79de9", "#4CAF50", "#FFD700", "#82B1FF", "#FF9800"],
        stroke: {
          curve: "smooth",
          width: 3
        },
        xaxis: {
          categories: ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"]
        },
        tooltip: {
          theme: "light",
          y: {}
        },
        legend: {
          position: "top"
        },
        series: [
          { name: "Total", data: [310450, 315300, 325800, 332000, 340500, 348950] },
          { name: "Ações", data: [85000, 87200, 89500, 91300, 93400, 95230] },
          { name: "FIIs", data: [68300, 69100, 70200, 71400, 72500, 73500] },
          { name: "Criptomoedas", data: [65400, 68200, 72500, 78300, 82400, 85730] },
          { name: "Tesouro/Selic", data: [51750, 52000, 53100, 53300, 53600, 54470] },
          { name: "Poupança", data: [40000, 40000, 40000, 40000, 40000, 40020] }
        ]
      }).render()

      // Gráfico de donut - Distribuição de Ativos
      new ApexCharts(document.querySelector('[data-chart="chart_1"]'), {
        chart: {
          type: "donut",
          width: "100%",
          height: "300",
          toolbar: { show: false }
        },
        colors: ["#615c8e", "#a79de9", "#4CAF50", "#FFD700", "#82B1FF", "#FF9800"],
        labels: ["Ações", "FIIs", "Criptomoedas", "Tesouro/Selic", "Poupança"],
        dataLabels: {
          enabled: true
        },
        legend: {
          position: "bottom"
        },
        series: [27.3, 21.1, 24.6, 15.6, 11.4]
      }).render()
    })
  }
}
</script>

<style scoped>
            @import url(https://fonts.googleapis.com/css2?family=Lato&display=swap);
            @import url(https://fonts.googleapis.com/css2?family=Open+Sans&display=swap);
            @import url(https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined);

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
            } /*! tailwindcss v3.4.17 | MIT License | https://tailwindcss.com*/
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
            [hidden]:where(:not([hidden="until-found"])) {
                display: none;
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
            #webcrumbs .mx-auto {
                margin-left: auto;
                margin-right: auto;
            }
            #webcrumbs .mb-3 {
                margin-bottom: 12px;
            }
            #webcrumbs .mb-5 {
                margin-bottom: 20px;
            }
            #webcrumbs .mb-6 {
                margin-bottom: 24px;
            }
            #webcrumbs .mb-8 {
                margin-bottom: 32px;
            }
            #webcrumbs .ml-1 {
                margin-left: 4px;
            }
            #webcrumbs .mt-2 {
                margin-top: 8px;
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
            #webcrumbs .h-8 {
                height: 32px;
            }
            #webcrumbs .h-\[300px\] {
                height: 300px;
            }
            #webcrumbs .max-h-\[300px\] {
                max-height: 300px;
            }
            #webcrumbs .min-h-screen {
                min-height: 100vh;
            }
            #webcrumbs .w-10 {
                width: 40px;
            }
            #webcrumbs .w-8 {
                width: 32px;
            }
            #webcrumbs .w-full {
                width: 100%;
            }
            #webcrumbs .min-w-full {
                min-width: 100%;
            }
            #webcrumbs .flex-grow {
                flex-grow: 1;
            }
            #webcrumbs .transform {
                transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate))
                    skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
            }
            #webcrumbs .cursor-pointer {
                cursor: pointer;
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
            #webcrumbs .items-center {
                align-items: center;
            }
            #webcrumbs .justify-end {
                justify-content: flex-end;
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
            #webcrumbs :is(.space-x-3 > :not([hidden]) ~ :not([hidden])) {
                --tw-space-x-reverse: 0;
                margin-left: calc(12px * (1 - var(--tw-space-x-reverse)));
                margin-right: calc(12px * var(--tw-space-x-reverse));
            }
            #webcrumbs :is(.space-x-6 > :not([hidden]) ~ :not([hidden])) {
                --tw-space-x-reverse: 0;
                margin-left: calc(24px * (1 - var(--tw-space-x-reverse)));
                margin-right: calc(24px * var(--tw-space-x-reverse));
            }
            #webcrumbs :is(.space-y-4 > :not([hidden]) ~ :not([hidden])) {
                --tw-space-y-reverse: 0;
                margin-bottom: calc(16px * var(--tw-space-y-reverse));
                margin-top: calc(16px * (1 - var(--tw-space-y-reverse)));
            }
            #webcrumbs .overflow-x-auto {
                overflow-x: auto;
            }
            #webcrumbs .overflow-y-auto {
                overflow-y: auto;
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
            #webcrumbs .border {
                border-width: 1px;
            }
            #webcrumbs .border-b {
                border-bottom-width: 1px;
            }
            #webcrumbs .border-gray-100 {
                --tw-border-opacity: 1;
                border-color: rgb(243 244 246 / var(--tw-border-opacity, 1));
            }
            #webcrumbs .border-gray-300 {
                --tw-border-opacity: 1;
                border-color: rgb(209 213 219 / var(--tw-border-opacity, 1));
            }
            #webcrumbs .bg-\[\#282641\] {
                --tw-bg-opacity: 1;
                background-color: rgb(40 38 65 / var(--tw-bg-opacity, 1));
            }
            #webcrumbs .bg-\[\#a79de9\] {
                --tw-bg-opacity: 1;
                background-color: rgb(167 157 233 / var(--tw-bg-opacity, 1));
            }
            #webcrumbs .bg-\[\#eed4ed\]\/10 {
                background-color: rgba(238, 212, 237, 0.1);
            }
            #webcrumbs .bg-blue-100 {
                --tw-bg-opacity: 1;
                background-color: rgb(219 234 254 / var(--tw-bg-opacity, 1));
            }
            #webcrumbs .bg-green-100 {
                --tw-bg-opacity: 1;
                background-color: rgb(220 252 231 / var(--tw-bg-opacity, 1));
            }
            #webcrumbs .bg-purple-100 {
                --tw-bg-opacity: 1;
                background-color: rgb(243 232 255 / var(--tw-bg-opacity, 1));
            }
            #webcrumbs .bg-white {
                --tw-bg-opacity: 1;
                background-color: rgb(255 255 255 / var(--tw-bg-opacity, 1));
            }
            #webcrumbs .bg-yellow-100 {
                --tw-bg-opacity: 1;
                background-color: rgb(254 249 195 / var(--tw-bg-opacity, 1));
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
            #webcrumbs .px-2 {
                padding-left: 8px;
                padding-right: 8px;
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
            #webcrumbs .py-2 {
                padding-bottom: 8px;
                padding-top: 8px;
            }
            #webcrumbs .py-3 {
                padding-bottom: 12px;
                padding-top: 12px;
            }
            #webcrumbs .pr-2 {
                padding-right: 8px;
            }
            #webcrumbs .text-left {
                text-align: left;
            }
            #webcrumbs .text-right {
                text-align: right;
            }
            #webcrumbs .text-2xl {
                font-size: 24px;
                line-height: 31.200000000000003px;
            }
            #webcrumbs .text-3xl {
                font-size: 30px;
                line-height: 36px;
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
            #webcrumbs .font-medium {
                font-weight: 500;
            }
            #webcrumbs .font-semibold {
                font-weight: 600;
            }
            #webcrumbs .text-\[\#282641\] {
                --tw-text-opacity: 1;
                color: rgb(40 38 65 / var(--tw-text-opacity, 1));
            }
            #webcrumbs .text-\[\#615c8e\] {
                --tw-text-opacity: 1;
                color: rgb(97 92 142 / var(--tw-text-opacity, 1));
            }
            #webcrumbs .text-blue-600 {
                --tw-text-opacity: 1;
                color: rgb(37 99 235 / var(--tw-text-opacity, 1));
            }
            #webcrumbs .text-green-500 {
                --tw-text-opacity: 1;
                color: rgb(34 197 94 / var(--tw-text-opacity, 1));
            }
            #webcrumbs .text-green-600 {
                --tw-text-opacity: 1;
                color: rgb(22 163 74 / var(--tw-text-opacity, 1));
            }
            #webcrumbs .text-green-800 {
                --tw-text-opacity: 1;
                color: rgb(22 101 52 / var(--tw-text-opacity, 1));
            }
            #webcrumbs .text-purple-600 {
                --tw-text-opacity: 1;
                color: rgb(147 51 234 / var(--tw-text-opacity, 1));
            }
            #webcrumbs .text-red-500 {
                --tw-text-opacity: 1;
                color: rgb(239 68 68 / var(--tw-text-opacity, 1));
            }
            #webcrumbs .text-white {
                --tw-text-opacity: 1;
                color: rgb(255 255 255 / var(--tw-text-opacity, 1));
            }
            #webcrumbs .text-yellow-600 {
                --tw-text-opacity: 1;
                color: rgb(202 138 4 / var(--tw-text-opacity, 1));
            }
            #webcrumbs .shadow-md {
                --tw-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.1);
                --tw-shadow-colored: 0 4px 6px -1px var(--tw-shadow-color), 0 2px 4px -2px var(--tw-shadow-color);
                box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
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
            #webcrumbs .hover\:translate-y-\[-2px\]:hover {
                --tw-translate-y: -2px;
            }
            #webcrumbs .hover\:rotate-90:hover,
            #webcrumbs .hover\:translate-y-\[-2px\]:hover {
                transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate))
                    skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
            }
            #webcrumbs .hover\:rotate-90:hover {
                --tw-rotate: 90deg;
            }
            #webcrumbs .hover\:scale-\[1\.02\]:hover {
                --tw-scale-x: 1.02;
                --tw-scale-y: 1.02;
                transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate))
                    skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
            }
            #webcrumbs .hover\:bg-\[\#615c8e\]:hover {
                --tw-bg-opacity: 1;
                background-color: rgb(97 92 142 / var(--tw-bg-opacity, 1));
            }
            #webcrumbs .hover\:bg-\[\#eed4ed\]\/10:hover {
                background-color: rgba(238, 212, 237, 0.1);
            }
            #webcrumbs .hover\:bg-\[\#eed4ed\]\/20:hover {
                background-color: rgba(238, 212, 237, 0.2);
            }
            #webcrumbs .hover\:text-\[\#282641\]:hover {
                --tw-text-opacity: 1;
                color: rgb(40 38 65 / var(--tw-text-opacity, 1));
            }
            #webcrumbs .hover\:text-\[\#a79de9\]:hover {
                --tw-text-opacity: 1;
                color: rgb(167 157 233 / var(--tw-text-opacity, 1));
            }
            #webcrumbs .hover\:shadow-lg:hover {
                --tw-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.1);
                --tw-shadow-colored: 0 10px 15px -3px var(--tw-shadow-color), 0 4px 6px -4px var(--tw-shadow-color);
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
                --tw-ring-color: rgb(167 157 233 / var(--tw-ring-opacity, 1));
            }
            @media (min-width: 768px) {
                #webcrumbs .md\:col-span-3 {
                    grid-column: span 3 / span 3;
                }
                #webcrumbs .md\:flex {
                    display: flex;
                }
                #webcrumbs .md\:grid-cols-3 {
                    grid-template-columns: repeat(3, minmax(0, 1fr));
                }
                #webcrumbs .md\:gap-6 {
                    gap: 24px;
                }
                #webcrumbs .md\:p-6 {
                    padding: 24px;
                }
            }
            @media (min-width: 1024px) {
                #webcrumbs .lg\:col-span-2 {
                    grid-column: span 2 / span 2;
                }
                #webcrumbs .lg\:grid-cols-2 {
                    grid-template-columns: repeat(2, minmax(0, 1fr));
                }
                #webcrumbs .lg\:grid-cols-3 {
                    grid-template-columns: repeat(3, minmax(0, 1fr));
                }
                #webcrumbs .lg\:grid-cols-6 {
                    grid-template-columns: repeat(6, minmax(0, 1fr));
                }
            }
   
</style>