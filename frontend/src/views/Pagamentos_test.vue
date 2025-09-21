<template>

<div id="webcrumbs" class="w-full">
  <Header /> 
  <div class="w-full p-6 bg-gray-50 min-h-screen">
      <div class="max-w-7xl mx-auto space-y-8">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
          <!-- Pagamentos do Mês -->
          <div class="bg-white rounded-xl shadow-lg p-6 hover:shadow-xl transition-shadow">
            <div class="flex justify-between items-center mb-6">
              <h2 class="text-2xl font-bold text-gray-900">Pagamentos do Mês</h2>
              <div class="flex gap-2">
                <details class="relative">
                  <summary
                    class="bg-gray-100 hover:bg-gray-200 px-4 py-2 rounded-lg cursor-pointer transition-colors flex items-center gap-2"
                  >
                    <span class="material-symbols-outlined text-sm">date_range</span> Data
                  </summary>
                  <div
                    class="absolute right-0 top-12 bg-white border border-gray-300 rounded-lg shadow-lg p-4 z-10 w-48"
                  >
                    <div class="space-y-2">
                      <div class="mb-2">
                        <label class="text-sm font-medium text-gray-700">De:</label>
                        <input
                          type="date"
                          class="w-full mt-1 rounded border border-gray-300 bg-gray-50 px-2 py-1 text-sm"
                        />
                      </div>
                      <div>
                        <label class="text-sm font-medium text-gray-700">Até:</label>
                        <input
                          type="date"
                          class="w-full mt-1 rounded border border-gray-300 bg-gray-50 px-2 py-1 text-sm"
                        />
                      </div>
                      <button
                        class="w-full bg-primary-500 hover:bg-primary-600 text-white mt-2 px-3 py-1 rounded text-sm transition-colors"
                      >
                        Aplicar
                      </button>
                    </div>
                  </div>
                </details>
                <details class="relative">
                  <summary
                    class="bg-gray-100 hover:bg-gray-200 px-4 py-2 rounded-lg cursor-pointer transition-colors flex items-center gap-2"
                  >
                    <span class="material-symbols-outlined text-sm">sort</span> Status
                  </summary>
                  <div
                    class="absolute right-0 top-12 bg-white border border-gray-300 rounded-lg shadow-lg p-4 z-10 w-48"
                  >
                    <div class="space-y-2">
                      <label
                        class="flex items-center hover:bg-gray-50 p-1 rounded cursor-pointer"
                      >
                        <input type="checkbox" class="mr-2" /> Pago
                      </label>
                      <label
                        class="flex items-center hover:bg-gray-50 p-1 rounded cursor-pointer"
                      >
                        <input type="checkbox" class="mr-2" /> Pendente
                      </label>
                      <label
                        class="flex items-center hover:bg-gray-50 p-1 rounded cursor-pointer"
                      >
                        <input type="checkbox" class="mr-2" /> Atrasado
                      </label>
                    </div>
                  </div>
                </details>
                <details class="relative">
                  <summary
                    class="bg-gray-100 hover:bg-gray-200 px-4 py-2 rounded-lg cursor-pointer transition-colors flex items-center gap-2"
                  >
                    <span class="material-symbols-outlined text-sm">filter_list</span> Filtrar
                  </summary>
                  <div
                    class="absolute right-0 top-12 bg-white border border-gray-300 rounded-lg shadow-lg p-4 z-10 w-48"
                  >
                    <div class="space-y-2">
                      <label
                        class="flex items-center hover:bg-gray-50 p-1 rounded cursor-pointer"
                      >
                        <input type="checkbox" class="mr-2" /> Moradia
                      </label>
                      <label
                        class="flex items-center hover:bg-gray-50 p-1 rounded cursor-pointer"
                      >
                        <input type="checkbox" class="mr-2" /> Alimentação
                      </label>
                      <label
                        class="flex items-center hover:bg-gray-50 p-1 rounded cursor-pointer"
                      >
                        <input type="checkbox" class="mr-2" /> Lazer
                      </label>
                      <label
                        class="flex items-center hover:bg-gray-50 p-1 rounded cursor-pointer"
                      >
                        <input type="checkbox" class="mr-2" /> Transporte
                      </label>
                    </div>
                  </div>
                </details>
              </div>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
              <div class="bg-green-50 p-4 rounded-lg hover:bg-green-100 transition-colors">
                <h3 class="text-sm font-medium text-green-600 mb-1">Total Pago</h3>
                <p class="text-2xl font-bold text-green-700">R$ 2.450,00</p>
              </div>
              <div class="bg-red-50 p-4 rounded-lg hover:bg-red-100 transition-colors">
                <h3 class="text-sm font-medium text-red-600 mb-1">Total Pendente</h3>
                <p class="text-2xl font-bold text-red-700">R$ 1.180,00</p>
              </div>
              <div class="bg-blue-50 p-4 rounded-lg hover:bg-blue-100 transition-colors">
                <h3 class="text-sm font-medium text-blue-600 mb-1">Total do Mês</h3>
                <p class="text-2xl font-bold text-blue-700">R$ 3.630,00</p>
              </div>
            </div>
            <div class="space-y-4 mb-6 h-[600px] overflow-y-auto pr-2">
              <div
                class="border border-gray-300 rounded-lg p-4 hover:shadow-md transition-shadow hover:border-primary-200"
              >
                <div class="flex justify-between items-center">
                  <div class="flex-1">
                    <div class="flex items-center gap-3">
                      <div class="w-3 h-3 bg-blue-500 rounded-full"></div>
                      <h4 class="font-medium text-gray-900">Aluguel</h4>
                      <span class="text-xs bg-gray-100 px-2 py-1 rounded">Moradia</span>
                    </div>
                    <p class="text-sm text-gray-600 mt-1">Vence em 05/12/2024</p>
                    <p class="text-lg font-semibold text-gray-900">R$ 1.200,00</p>
                  </div>
                  <div class="flex items-center gap-2">
                    <span class="text-xs bg-green-100 text-green-700 px-2 py-1 rounded"
                      >Pago</span
                    >
                    <span
                      class="material-symbols-outlined text-green-500 hover:scale-110 transition-transform cursor-pointer"
                      >check_circle</span
                    >
                  </div>
                </div>
              </div>
              <div
                class="border border-gray-300 rounded-lg p-4 hover:shadow-md transition-shadow hover:border-primary-200"
              >
                <div class="flex justify-between items-center">
                  <div class="flex-1">
                    <div class="flex items-center gap-3">
                      <div class="w-3 h-3 bg-orange-500 rounded-full"></div>
                      <h4 class="font-medium text-gray-900">Energia Elétrica</h4>
                      <span class="text-xs bg-gray-100 px-2 py-1 rounded">Moradia</span>
                    </div>
                    <p class="text-sm text-gray-600 mt-1">Vence em 15/12/2024</p>
                    <p class="text-lg font-semibold text-gray-900">R$ 280,00</p>
                  </div>
                  <div class="flex items-center gap-2">
                    <span class="text-xs bg-red-100 text-red-700 px-2 py-1 rounded"
                      >Pendente</span
                    >
                    <button
                      class="bg-primary-500 hover:bg-primary-600 text-white px-3 py-1 rounded text-sm transition-colors hover:scale-105"
                    >
                      Pagar
                    </button>
                  </div>
                </div>
              </div>
              <div
                class="border border-gray-300 rounded-lg p-4 hover:shadow-md transition-shadow hover:border-primary-200"
              >
                <div class="flex justify-between items-center">
                  <div class="flex-1">
                    <div class="flex items-center gap-3">
                      <div class="w-3 h-3 bg-green-500 rounded-full"></div>
                      <h4 class="font-medium text-gray-900">Supermercado</h4>
                      <span class="text-xs bg-gray-100 px-2 py-1 rounded">Alimentação</span>
                    </div>
                    <p class="text-sm text-gray-600 mt-1">Vence em 20/12/2024</p>
                    <p class="text-lg font-semibold text-gray-900">R$ 450,00</p>
                  </div>
                  <div class="flex items-center gap-2">
                    <span class="text-xs bg-red-100 text-red-700 px-2 py-1 rounded"
                      >Pendente</span
                    >
                    <button
                      class="bg-primary-500 hover:bg-primary-600 text-white px-3 py-1 rounded text-sm transition-colors hover:scale-105"
                    >
                      Pagar
                    </button>
                  </div>
                </div>
              </div>
              <div
                class="border border-gray-300 rounded-lg p-4 hover:shadow-md transition-shadow hover:border-primary-200"
              >
                <div class="flex justify-between items-center">
                  <div class="flex-1">
                    <div class="flex items-center gap-3">
                      <div class="w-3 h-3 bg-purple-500 rounded-full"></div>
                      <h4 class="font-medium text-gray-900">Netflix</h4>
                      <span class="text-xs bg-gray-100 px-2 py-1 rounded">Lazer</span>
                    </div>
                    <p class="text-sm text-gray-600 mt-1">Vence em 25/12/2024</p>
                    <p class="text-lg font-semibold text-gray-900">R$ 45,00</p>
                  </div>
                  <div class="flex items-center gap-2">
                    <span class="text-xs bg-green-100 text-green-700 px-2 py-1 rounded"
                      >Pago</span
                    >
                    <span
                      class="material-symbols-outlined text-green-500 hover:scale-110 transition-transform cursor-pointer"
                      >check_circle</span
                    >
                  </div>
                </div>
              </div>
            </div>
            <div class="border-t border-gray-300 pt-6">
              <h3 class="text-lg font-semibold text-gray-900 mb-4">Próximos Meses</h3>
              <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                <div class="bg-gray-50 p-4 rounded-lg hover:bg-gray-100 transition-colors">
                  <h4 class="font-medium text-gray-700 mb-2">Janeiro 2025</h4>
                  <p class="text-xl font-bold text-gray-900">R$ 3.520,00</p>
                </div>
                <div class="bg-gray-50 p-4 rounded-lg hover:bg-gray-100 transition-colors">
                  <h4 class="font-medium text-gray-700 mb-2">Fevereiro 2025</h4>
                  <p class="text-xl font-bold text-gray-900">R$ 3.630,00</p>
                </div>
                <div class="bg-gray-50 p-4 rounded-lg hover:bg-gray-100 transition-colors">
                  <h4 class="font-medium text-gray-700 mb-2">Março 2025</h4>
                  <p class="text-xl font-bold text-gray-900">R$ 3.480,00</p>
                </div>
              </div>
            </div>
          </div>
          <div class="bg-white rounded-xl shadow-lg p-6 hover:shadow-xl transition-shadow">
            <div class="flex justify-between items-center mb-6">
              <h2 class="text-2xl font-bold text-gray-900">Compartilhadas</h2>
              <div class="flex gap-2">
                <details class="relative">
                  <summary
                    class="bg-gray-100 hover:bg-gray-200 px-4 py-2 rounded-lg cursor-pointer transition-colors flex items-center gap-2"
                  >
                    <span class="material-symbols-outlined text-sm">date_range</span> Data
                  </summary>
                  <div
                    class="absolute right-0 top-12 bg-white border border-gray-300 rounded-lg shadow-lg p-4 z-10 w-48"
                  >
                    <div class="space-y-2">
                      <div class="mb-2">
                        <label class="text-sm font-medium text-gray-700">De:</label>
                        <input
                          type="date"
                          class="w-full mt-1 rounded border border-gray-300 bg-gray-50 px-2 py-1 text-sm"
                        />
                      </div>
                      <div>
                        <label class="text-sm font-medium text-gray-700">Até:</label>
                        <input
                          type="date"
                          class="w-full mt-1 rounded border border-gray-300 bg-gray-50 px-2 py-1 text-sm"
                        />
                      </div>
                      <button
                        class="w-full bg-primary-500 hover:bg-primary-600 text-white mt-2 px-3 py-1 rounded text-sm transition-colors"
                      >
                        Aplicar
                      </button>
                    </div>
                  </div>
                </details>
                <details class="relative">
                  <summary
                    class="bg-gray-100 hover:bg-gray-200 px-4 py-2 rounded-lg cursor-pointer transition-colors flex items-center gap-2"
                  >
                    <span class="material-symbols-outlined text-sm">sort</span> Status
                  </summary>
                  <div
                    class="absolute right-0 top-12 bg-white border border-gray-300 rounded-lg shadow-lg p-4 z-10 w-48"
                  >
                    <div class="space-y-2">
                      <label
                        class="flex items-center hover:bg-gray-50 p-1 rounded cursor-pointer"
                      >
                        <input type="checkbox" class="mr-2" /> Pago
                      </label>
                      <label
                        class="flex items-center hover:bg-gray-50 p-1 rounded cursor-pointer"
                      >
                        <input type="checkbox" class="mr-2" /> Pendente
                      </label>
                      <label
                        class="flex items-center hover:bg-gray-50 p-1 rounded cursor-pointer"
                      >
                        <input type="checkbox" class="mr-2" /> Atrasado
                      </label>
                    </div>
                  </div>
                </details>
                <details class="relative">
                  <summary
                    class="bg-gray-100 hover:bg-gray-200 px-4 py-2 rounded-lg cursor-pointer transition-colors flex items-center gap-2"
                  >
                    <span class="material-symbols-outlined text-sm">filter_list</span> Filtrar
                  </summary>
                  <div
                    class="absolute right-0 top-12 bg-white border border-gray-300 rounded-lg shadow-lg p-4 z-10 w-48"
                  >
                    <div class="space-y-2">
                      <label
                        class="flex items-center hover:bg-gray-50 p-1 rounded cursor-pointer"
                      >
                        <input type="checkbox" class="mr-2" /> Moradia
                      </label>
                      <label
                        class="flex items-center hover:bg-gray-50 p-1 rounded cursor-pointer"
                      >
                        <input type="checkbox" class="mr-2" /> Alimentação
                      </label>
                      <label
                        class="flex items-center hover:bg-gray-50 p-1 rounded cursor-pointer"
                      >
                        <input type="checkbox" class="mr-2" /> Lazer
                      </label>
                      <label
                        class="flex items-center hover:bg-gray-50 p-1 rounded cursor-pointer"
                      >
                        <input type="checkbox" class="mr-2" /> Transporte
                      </label>
                    </div>
                  </div>
                </details>
              </div>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
              <div class="bg-green-50 p-4 rounded-lg hover:bg-green-100 transition-colors">
                <h3 class="text-sm font-medium text-green-600 mb-1">Pagaram</h3>
                <p class="text-2xl font-bold text-green-700">3/5 pessoas</p>
              </div>
              <div class="bg-blue-50 p-4 rounded-lg hover:bg-blue-100 transition-colors">
                <h3 class="text-sm font-medium text-blue-600 mb-1">Total Recebido</h3>
                <p class="text-2xl font-bold text-blue-700">R$ 180,00</p>
              </div>
              <div class="bg-orange-50 p-4 rounded-lg hover:bg-orange-100 transition-colors">
                <h3 class="text-sm font-medium text-orange-600 mb-1">Restante</h3>
                <p class="text-2xl font-bold text-orange-700">R$ 120,00</p>
              </div>
            </div>
            <div class="space-y-4 h-[600px] overflow-y-auto pr-2">
              <div
                class="border border-gray-300 rounded-lg p-4 hover:shadow-md transition-shadow hover:border-primary-200"
              >
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <div
                      class="w-10 h-10 bg-gradient-to-br from-blue-500 to-purple-600 rounded-full flex items-center justify-center text-white font-semibold hover:scale-105 transition-transform"
                    >
                      M
                    </div>
                    <div>
                      <h4 class="font-medium text-gray-900">Maria Silva</h4>
                      <p class="text-sm text-gray-600">Jantar no restaurante</p>
                      <p class="text-sm font-semibold text-gray-900">R$ 60,00</p>
                    </div>
                  </div>
                  <div class="flex items-center gap-2">
                    <span class="text-xs bg-green-100 text-green-700 px-2 py-1 rounded"
                      >Pago</span
                    >
                    <span class="text-xs text-gray-500">15/12/2024</span>
                  </div>
                </div>
              </div>
              <div
                class="border border-gray-300 rounded-lg p-4 hover:shadow-md transition-shadow hover:border-primary-200"
              >
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <div
                      class="w-10 h-10 bg-gradient-to-br from-green-500 to-teal-600 rounded-full flex items-center justify-center text-white font-semibold hover:scale-105 transition-transform"
                    >
                      J
                    </div>
                    <div>
                      <h4 class="font-medium text-gray-900">João Santos</h4>
                      <p class="text-sm text-gray-600">Jantar no restaurante</p>
                      <p class="text-sm font-semibold text-gray-900">R$ 60,00</p>
                    </div>
                  </div>
                  <div class="flex items-center gap-2">
                    <span class="text-xs bg-red-100 text-red-700 px-2 py-1 rounded"
                      >Pendente</span
                    >
                    <button
                      class="text-primary-600 hover:text-primary-700 transition-colors hover:scale-110"
                    >
                      <span class="material-symbols-outlined text-sm">send</span>
                    </button>
                    <button
                      class="bg-primary-500 hover:bg-primary-600 text-white px-2 py-1 rounded text-xs transition-colors hover:scale-105"
                    >
                      Marcar Pago
                    </button>
                  </div>
                </div>
              </div>
              <div
                class="border border-gray-300 rounded-lg p-4 hover:shadow-md transition-shadow hover:border-primary-200"
              >
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <div
                      class="w-10 h-10 bg-gradient-to-br from-pink-500 to-rose-600 rounded-full flex items-center justify-center text-white font-semibold hover:scale-105 transition-transform"
                    >
                      A
                    </div>
                    <div>
                      <h4 class="font-medium text-gray-900">Ana Costa</h4>
                      <p class="text-sm text-gray-60">Jantar no restaurante</p>
                      <p class="text-sm font-semibold text-gray-900">R$ 60,00</p>
                    </div>
                  </div>
                  <div class="flex items-center gap-2">
                    <span class="text-xs bg-green-100 text-green-700 px-2 py-1 rounded"
                      >Pago</span
                    >
                    <span class="text-xs text-gray-500">14/12/2024</span>
                  </div>
                </div>
              </div>
              <div
                class="border border-gray-300 rounded-lg p-4 hover:shadow-md transition-shadow hover:border-primary-200"
              >
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <div
                      class="w-10 h-10 bg-gradient-to-br from-orange-500 to-red-600 rounded-full flex items-center justify-center text-white font-semibold hover:scale-105 transition-transform"
                    >
                      P
                    </div>
                    <div>
                      <h4 class="font-medium text-gray-900">Pedro Lima</h4>
                      <p class="text-sm text-gray-600">Jantar no restaurante</p>
                      <p class="text-sm font-semibold text-gray-900">R$ 60,00</p>
                    </div>
                  </div>
                  <div class="flex items-center gap-2">
                    <span class="text-xs bg-red-100 text-red-700 px-2 py-1 rounded"
                      >Atrasado</span
                    >
                    <button
                      class="text-red-600 hover:text-red-700 transition-colors hover:scale-110"
                    >
                      <span class="material-symbols-outlined text-sm">notifications</span>
                    </button>
                    <button
                      class="bg-primary-500 hover:bg-primary-600 text-white px-2 py-1 rounded text-xs transition-colors hover:scale-105"
                    >
                      Marcar Pago
                    </button>
                  </div>
                </div>
              </div>
              <div
                class="border border-gray-300 rounded-lg p-4 hover:shadow-md transition-shadow hover:border-primary-200"
              >
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <div
                      class="w-10 h-10 bg-gradient-to-br from-indigo-500 to-purple-600 rounded-full flex items-center justify-center text-white font-semibold hover:scale-105 transition-transform"
                    >
                      C
                    </div>
                    <div>
                      <h4 class="font-medium text-gray-900">Carlos Oliveira</h4>
                      <p class="text-sm text-gray-600">Jantar no restaurante</p>
                      <p class="text-sm font-semibold text-gray-900">R$ 60,00</p>
                    </div>
                  </div>
                  <div class="flex items-center gap-2">
                    <span class="text-xs bg-green-100 text-green-700 px-2 py-1 rounded"
                      >Pago</span
                    >
                    <span class="text-xs text-gray-500">13/12/2024</span>
                  </div>
                </div>
              </div>
            </div>
            <div class="mt-6 pt-6 border-t border-gray-300">
              <div class="flex justify-between items-center">
                <h3 class="text-lg font-semibold text-gray-900 mb-4">Próximos Meses</h3>
              </div>
              <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                <div class="bg-gray-50 p-4 rounded-lg hover:bg-gray-100 transition-colors">
                  <h4 class="font-medium text-gray-700 mb-2">Janeiro 2025</h4>
                  <p class="text-xl font-bold text-gray-900">R$ 3.520,00</p>
                </div>
                <div class="bg-gray-50 p-4 rounded-lg hover:bg-gray-100 transition-colors">
                  <h4 class="font-medium text-gray-700 mb-2">Fevereiro 2025</h4>
                  <p class="text-xl font-bold text-gray-900">R$ 3.630,00</p>
                </div>
                <div class="bg-gray-50 p-4 rounded-lg hover:bg-gray-100 transition-colors">
                  <h4 class="font-medium text-gray-700 mb-2">Março 2025</h4>
                  <p class="text-xl font-bold text-gray-900">R$ 3.480,00</p>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="bg-white rounded-xl shadow-lg p-6 hover:shadow-xl transition-shadow mt-8">
          <h3 class="text-xl font-semibold text-gray-900 mb-4">Evolução Mensal de Gastos</h3>
          <div
            class="h-64 flex items-center justify-center bg-gray-50 rounded-lg hover:bg-gray-100 transition-colors"
          >
            <div class="text-center">
              <span
                class="material-symbols-outlined text-4xl text-gray-400 mb-2 hover:text-primary-500 transition-colors cursor-pointer"
                >trending_up</span
              >
              <p class="text-gray-600 text-lg">Gráfico de evolução dos gastos</p>
              <p class="text-sm text-gray-500">Últimos 6 meses</p>
              <div class="mt-2">
                <button
                  class="bg-primary-500 hover:bg-primary-600 text-white px-4 py-2 rounded text-sm transition-colors hover:scale-105"
                >
                  Visualizar gráfico completo
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Header from '../components/Header.vue';
export default {
  components: {
    Header,
  }}
</script>

<style>
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
            #webcrumbs .absolute {
                position: absolute;
            }
            #webcrumbs .relative {
                position: relative;
            }
            #webcrumbs .right-0 {
                right: 0;
            }
            #webcrumbs .top-12 {
                top: 48px;
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
            #webcrumbs .mb-4 {
                margin-bottom: 16px;
            }
            #webcrumbs .mb-6 {
                margin-bottom: 24px;
            }
            #webcrumbs .mb-8 {
                margin-bottom: 32px;
            }
            #webcrumbs .mr-2 {
                margin-right: 8px;
            }
            #webcrumbs .mt-1 {
                margin-top: 4px;
            }
            #webcrumbs .mt-2 {
                margin-top: 8px;
            }
            #webcrumbs .mt-6 {
                margin-top: 24px;
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
            #webcrumbs .h-10 {
                height: 40px;
            }
            #webcrumbs .h-3 {
                height: 12px;
            }
            #webcrumbs .h-64 {
                height: 256px;
            }
            #webcrumbs .h-\[600px\] {
                height: 600px;
            }
            #webcrumbs .min-h-screen {
                min-height: 100vh;
            }
            #webcrumbs .w-10 {
                width: 40px;
            }
            #webcrumbs .w-3 {
                width: 12px;
            }
            #webcrumbs .w-48 {
                width: 192px;
            }
            #webcrumbs .w-\[1280px\] {
                 width: 100%;
            }
            #webcrumbs .w-full {
                width: 100%;
            }
            #webcrumbs .max-w-7xl {
                max-width: 80rem;
            }
            #webcrumbs .flex-1 {
                flex: 1 1 0%;
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
            #webcrumbs .items-center {
                align-items: center;
            }
            #webcrumbs .justify-center {
                justify-content: center;
            }
            #webcrumbs .justify-between {
                justify-content: space-between;
            }
            #webcrumbs .gap-2 {
                gap: 8px;
            }
            #webcrumbs .gap-3 {
                gap: 12px;
            }
            #webcrumbs .gap-4 {
                gap: 16px;
            }
            #webcrumbs .gap-8 {
                gap: 32px;
            }
            #webcrumbs :is(.space-y-2 > :not([hidden]) ~ :not([hidden])) {
                --tw-space-y-reverse: 0;
                margin-bottom: calc(8px * var(--tw-space-y-reverse));
                margin-top: calc(8px * (1 - var(--tw-space-y-reverse)));
            }
            #webcrumbs :is(.space-y-4 > :not([hidden]) ~ :not([hidden])) {
                --tw-space-y-reverse: 0;
                margin-bottom: calc(16px * var(--tw-space-y-reverse));
                margin-top: calc(16px * (1 - var(--tw-space-y-reverse)));
            }
            #webcrumbs :is(.space-y-8 > :not([hidden]) ~ :not([hidden])) {
                --tw-space-y-reverse: 0;
                margin-bottom: calc(32px * var(--tw-space-y-reverse));
                margin-top: calc(32px * (1 - var(--tw-space-y-reverse)));
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
            #webcrumbs .rounded-xl {
                border-radius: 36px;
            }
            #webcrumbs .border {
                border-width: 1px;
            }
            #webcrumbs .border-t {
                border-top-width: 1px;
            }
            #webcrumbs .border-gray-300 {
                --tw-border-opacity: 1;
                border-color: rgb(209 213 219 / var(--tw-border-opacity));
            }
            #webcrumbs .bg-blue-50 {
                --tw-bg-opacity: 1;
                background-color: rgb(239 246 255 / var(--tw-bg-opacity));
            }
            #webcrumbs .bg-blue-500 {
                --tw-bg-opacity: 1;
                background-color: rgb(59 130 246 / var(--tw-bg-opacity));
            }
            #webcrumbs .bg-gray-100 {
                --tw-bg-opacity: 1;
                background-color: rgb(243 244 246 / var(--tw-bg-opacity));
            }
            #webcrumbs .bg-gray-50 {
                --tw-bg-opacity: 1;
                background-color: rgb(249 250 251 / var(--tw-bg-opacity));
            }
            #webcrumbs .bg-green-100 {
                --tw-bg-opacity: 1;
                background-color: rgb(220 252 231 / var(--tw-bg-opacity));
            }
            #webcrumbs .bg-green-50 {
                --tw-bg-opacity: 1;
                background-color: rgb(240 253 244 / var(--tw-bg-opacity));
            }
            #webcrumbs .bg-green-500 {
                --tw-bg-opacity: 1;
                background-color: rgb(34 197 94 / var(--tw-bg-opacity));
            }
            #webcrumbs .bg-orange-50 {
                --tw-bg-opacity: 1;
                background-color: rgb(255 247 237 / var(--tw-bg-opacity));
            }
            #webcrumbs .bg-orange-500 {
                --tw-bg-opacity: 1;
                background-color: rgb(249 115 22 / var(--tw-bg-opacity));
            }
            #webcrumbs .bg-primary-500 {
                --tw-bg-opacity: 1;
                background-color: rgb(115 65 255 / var(--tw-bg-opacity));
            }
            #webcrumbs .bg-purple-500 {
                --tw-bg-opacity: 1;
                background-color: rgb(168 85 247 / var(--tw-bg-opacity));
            }
            #webcrumbs .bg-red-100 {
                --tw-bg-opacity: 1;
                background-color: rgb(254 226 226 / var(--tw-bg-opacity));
            }
            #webcrumbs .bg-red-50 {
                --tw-bg-opacity: 1;
                background-color: rgb(254 242 242 / var(--tw-bg-opacity));
            }
            #webcrumbs .bg-white {
                --tw-bg-opacity: 1;
                background-color: rgb(255 255 255 / var(--tw-bg-opacity));
            }
            #webcrumbs .bg-gradient-to-br {
                background-image: linear-gradient(to bottom right, var(--tw-gradient-stops));
            }
            #webcrumbs .from-blue-500 {
                --tw-gradient-from: #3b82f6 var(--tw-gradient-from-position);
                --tw-gradient-to: rgba(59, 130, 246, 0) var(--tw-gradient-to-position);
                --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to);
            }
            #webcrumbs .from-green-500 {
                --tw-gradient-from: #22c55e var(--tw-gradient-from-position);
                --tw-gradient-to: rgba(34, 197, 94, 0) var(--tw-gradient-to-position);
                --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to);
            }
            #webcrumbs .from-indigo-500 {
                --tw-gradient-from: #6366f1 var(--tw-gradient-from-position);
                --tw-gradient-to: rgba(99, 102, 241, 0) var(--tw-gradient-to-position);
                --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to);
            }
            #webcrumbs .from-orange-500 {
                --tw-gradient-from: #f97316 var(--tw-gradient-from-position);
                --tw-gradient-to: rgba(249, 115, 22, 0) var(--tw-gradient-to-position);
                --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to);
            }
            #webcrumbs .from-pink-500 {
                --tw-gradient-from: #ec4899 var(--tw-gradient-from-position);
                --tw-gradient-to: rgba(236, 72, 153, 0) var(--tw-gradient-to-position);
                --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to);
            }
            #webcrumbs .to-purple-600 {
                --tw-gradient-to: #9333ea var(--tw-gradient-to-position);
            }
            #webcrumbs .to-red-600 {
                --tw-gradient-to: #dc2626 var(--tw-gradient-to-position);
            }
            #webcrumbs .to-rose-600 {
                --tw-gradient-to: #e11d48 var(--tw-gradient-to-position);
            }
            #webcrumbs .to-teal-600 {
                --tw-gradient-to: #0d9488 var(--tw-gradient-to-position);
            }
            #webcrumbs .p-1 {
                padding: 4px;
            }
            #webcrumbs .p-4 {
                padding: 16px;
            }
            #webcrumbs .p-6 {
                padding: 24px;
            }
            #webcrumbs .px-2 {
                padding-left: 8px;
                padding-right: 8px;
            }
            #webcrumbs .px-3 {
                padding-left: 12px;
                padding-right: 12px;
            }
            #webcrumbs .px-4 {
                padding-left: 16px;
                padding-right: 16px;
            }
            #webcrumbs .py-1 {
                padding-bottom: 4px;
                padding-top: 4px;
            }
            #webcrumbs .py-2 {
                padding-bottom: 8px;
                padding-top: 8px;
            }
            #webcrumbs .pr-2 {
                padding-right: 8px;
            }
            #webcrumbs .pt-6 {
                padding-top: 24px;
            }
            #webcrumbs .text-center {
                text-align: center;
            }
            #webcrumbs .text-2xl {
                font-size: 24px;
                line-height: 31.200000000000003px;
            }
            #webcrumbs .text-4xl {
                font-size: 36px;
                line-height: 41.4px;
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
            #webcrumbs .font-medium {
                font-weight: 500;
            }
            #webcrumbs .font-semibold {
                font-weight: 600;
            }
            #webcrumbs .text-blue-600 {
                --tw-text-opacity: 1;
                color: rgb(37 99 235 / var(--tw-text-opacity));
            }
            #webcrumbs .text-blue-700 {
                --tw-text-opacity: 1;
                color: rgb(29 78 216 / var(--tw-text-opacity));
            }
            #webcrumbs .text-gray-400 {
                --tw-text-opacity: 1;
                color: rgb(156 163 175 / var(--tw-text-opacity));
            }
            #webcrumbs .text-gray-500 {
                --tw-text-opacity: 1;
                color: rgb(107 114 128 / var(--tw-text-opacity));
            }
            #webcrumbs .text-gray-600 {
                --tw-text-opacity: 1;
                color: rgb(75 85 99 / var(--tw-text-opacity));
            }
            #webcrumbs .text-gray-700 {
                --tw-text-opacity: 1;
                color: rgb(55 65 81 / var(--tw-text-opacity));
            }
            #webcrumbs .text-gray-900 {
                --tw-text-opacity: 1;
                color: rgb(17 24 39 / var(--tw-text-opacity));
            }
            #webcrumbs .text-green-500 {
                --tw-text-opacity: 1;
                color: rgb(34 197 94 / var(--tw-text-opacity));
            }
            #webcrumbs .text-green-600 {
                --tw-text-opacity: 1;
                color: rgb(22 163 74 / var(--tw-text-opacity));
            }
            #webcrumbs .text-green-700 {
                --tw-text-opacity: 1;
                color: rgb(21 128 61 / var(--tw-text-opacity));
            }
            #webcrumbs .text-orange-600 {
                --tw-text-opacity: 1;
                color: rgb(234 88 12 / var(--tw-text-opacity));
            }
            #webcrumbs .text-orange-700 {
                --tw-text-opacity: 1;
                color: rgb(194 65 12 / var(--tw-text-opacity));
            }
            #webcrumbs .text-primary-600 {
                --tw-text-opacity: 1;
                color: rgb(99 27 255 / var(--tw-text-opacity));
            }
            #webcrumbs .text-red-600 {
                --tw-text-opacity: 1;
                color: rgb(220 38 38 / var(--tw-text-opacity));
            }
            #webcrumbs .text-red-700 {
                --tw-text-opacity: 1;
                color: rgb(185 28 28 / var(--tw-text-opacity));
            }
            #webcrumbs .text-white {
                --tw-text-opacity: 1;
                color: rgb(255 255 255 / var(--tw-text-opacity));
            }
            #webcrumbs .shadow-lg {
                --tw-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.1);
                --tw-shadow-colored: 0 10px 15px -3px var(--tw-shadow-color), 0 4px 6px -4px var(--tw-shadow-color);
                box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
            }
            #webcrumbs .transition-colors {
                transition-duration: 0.15s;
                transition-property: color, background-color, border-color, text-decoration-color, fill, stroke;
                transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
            }
            #webcrumbs .transition-shadow {
                transition-duration: 0.15s;
                transition-property: box-shadow;
                transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
            }
            #webcrumbs .transition-transform {
                transition-duration: 0.15s;
                transition-property: transform;
                transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
            }
            #webcrumbs {
                font-family: Open Sans !important;
                font-size: 16px !important;
            }
            #webcrumbs :is(.bg-primary-500) {
                color: hsla(0, 0%, 100%, 0.9) !important;
            }
            #webcrumbs .hover\:scale-105:hover {
                --tw-scale-x: 1.05;
                --tw-scale-y: 1.05;
            }
            #webcrumbs .hover\:scale-105:hover,
            #webcrumbs .hover\:scale-110:hover {
                transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate))
                    skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
            }
            #webcrumbs .hover\:scale-110:hover {
                --tw-scale-x: 1.1;
                --tw-scale-y: 1.1;
            }
            #webcrumbs .hover\:border-primary-200:hover {
                --tw-border-opacity: 1;
                border-color: rgb(213 207 255 / var(--tw-border-opacity));
            }
            #webcrumbs .hover\:bg-blue-100:hover {
                --tw-bg-opacity: 1;
                background-color: rgb(219 234 254 / var(--tw-bg-opacity));
            }
            #webcrumbs .hover\:bg-gray-100:hover {
                --tw-bg-opacity: 1;
                background-color: rgb(243 244 246 / var(--tw-bg-opacity));
            }
            #webcrumbs .hover\:bg-gray-200:hover {
                --tw-bg-opacity: 1;
                background-color: rgb(229 231 235 / var(--tw-bg-opacity));
            }
            #webcrumbs .hover\:bg-gray-50:hover {
                --tw-bg-opacity: 1;
                background-color: rgb(249 250 251 / var(--tw-bg-opacity));
            }
            #webcrumbs .hover\:bg-green-100:hover {
                --tw-bg-opacity: 1;
                background-color: rgb(220 252 231 / var(--tw-bg-opacity));
            }
            #webcrumbs .hover\:bg-orange-100:hover {
                --tw-bg-opacity: 1;
                background-color: rgb(255 237 213 / var(--tw-bg-opacity));
            }
            #webcrumbs .hover\:bg-primary-600:hover {
                --tw-bg-opacity: 1;
                background-color: rgb(99 27 255 / var(--tw-bg-opacity));
            }
            #webcrumbs .hover\:bg-red-100:hover {
                --tw-bg-opacity: 1;
                background-color: rgb(254 226 226 / var(--tw-bg-opacity));
            }
            #webcrumbs .hover\:text-primary-500:hover {
                --tw-text-opacity: 1;
                color: rgb(115 65 255 / var(--tw-text-opacity));
            }
            #webcrumbs .hover\:text-primary-700:hover {
                --tw-text-opacity: 1;
                color: rgb(97 27 248 / var(--tw-text-opacity));
            }
            #webcrumbs .hover\:text-red-700:hover {
                --tw-text-opacity: 1;
                color: rgb(185 28 28 / var(--tw-text-opacity));
            }
            #webcrumbs .hover\:shadow-md:hover {
                --tw-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.1);
                --tw-shadow-colored: 0 4px 6px -1px var(--tw-shadow-color), 0 2px 4px -2px var(--tw-shadow-color);
            }
            #webcrumbs .hover\:shadow-md:hover,
            #webcrumbs .hover\:shadow-xl:hover {
                box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
            }
            #webcrumbs .hover\:shadow-xl:hover {
                --tw-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1);
                --tw-shadow-colored: 0 20px 25px -5px var(--tw-shadow-color), 0 8px 10px -6px var(--tw-shadow-color);
            }
            @media (min-width: 768px) {
                #webcrumbs .md\:grid-cols-3 {
                    grid-template-columns: repeat(3, minmax(0, 1fr));
                }
            }
            @media (min-width: 1024px) {
                #webcrumbs .lg\:grid-cols-2 {
                    grid-template-columns: repeat(2, minmax(0, 1fr));
                }
            }


        </style>