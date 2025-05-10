<template>
  <div class="fixed top-4 right-4 z-50 space-y-2">
    <div v-for="(notif, index) in notifications" 
         :key="index"
         :class="['p-4 rounded-lg shadow-lg text-white flex items-center',
                  notif.type === 'success' ? 'bg-green-500' : 'bg-red-500']">
      <span class="material-symbols-outlined mr-2">
        {{ notif.type === 'success' ? 'check_circle' : 'error' }}
      </span>
      {{ notif.message }}
    </div>
  </div>
  <Header />
  <div id="root" class="flex justify-center items-center min-h-screen p-4">
    <div class="w-[1200px] bg-white rounded-lg shadow-lg overflow-hidden font-sans">
      <div class="flex flex-col md:flex-row">
        <div class="w-full md:w-3/4 p-6">
          <h1 class="text-3xl font-bold text-[#282641] mb-6">Cadastro de Transação</h1>
          <div class="bg-white rounded-lg p-6 mb-6 shadow">
            <h2 class="text-xl font-semibold text-[#282641] mb-4 flex items-center">
              <span class="material-symbols-outlined mr-2">account_balance</span> Informações Básicas
            </h2>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
  <!-- Banco Field -->
  <div class="relative">
    <label class="block text-sm font-medium text-[#615c8e] mb-1" for="banco">
      Banco <span class="text-red-500 ml-1">*</span>
    </label>
    <select v-model="transaction.banco"
      class="w-full px-4 py-2.5 border border-gray-300 rounded-lg bg-white hover:border-[#a79de9] transition-all appearance-none">
      <option value="" disabled selected>Selecione o banco</option>
      <option v-for="(label, value) in bancoChoices" :key="value" :value="value">
        {{ label }}
      </option>
    </select>
    <span class="material-symbols-outlined absolute right-3 top-1/2 transform -translate-y-1/2 text-[#615c8e] pointer-events-none"></span>
  </div>
  
  <!-- Categoria Field -->
  <div class="relative">
    <label class="block text-sm font-medium text-[#615c8e] mb-1" for="categoria">
      Categoria <span class="text-red-500 ml-1">*</span>
    </label>
    <select v-model="transaction.categoria"
      class="w-full px-4 py-2.5 border border-gray-300 rounded-lg bg-white hover:border-[#a79de9] transition-all appearance-none">
      <option value="" disabled selected>Selecione a categoria</option>
      <option v-for="(label, value) in categoriaChoices" :key="value" :value="value">
        {{ label }}
      </option>
    </select>
    <span class="material-symbols-outlined absolute right-3 top-1/2 transform -translate-y-1/2 text-[#615c8e] pointer-events-none"></span>
  </div>
  
  <!-- Tipo Field -->
  <div class="relative w-48">
    <label class="block text-sm font-medium text-[#615c8e] mb-1" for="tipo">
      Tipo <span class="text-red-500 ml-1">*</span>
    </label>
    <select v-model="transaction.tipo"
      class="w-full px-4 py-2.5 border border-gray-300 rounded-lg bg-white hover:border-[#a79de9] transition-all appearance-none">
      <option value="" disabled selected>Selecione tipo</option>
      <option v-for="(label, value) in tipoChoices" :key="value" :value="value">
        {{ label }}
      </option>
    </select>
    <span class="material-symbols-outlined absolute right-3 top-1/2 transform -translate-y-1/2 text-[#615c8e] pointer-events-none"></span>
  </div>
  
  <!-- Forma Field -->
  <div class="relative w-48">
    <label class="block text-sm font-medium text-[#615c8e] mb-1" for="forma">
      Forma <span class="text-red-500 ml-1">*</span>
    </label>
    <select v-model="transaction.forma"
      class="w-full px-4 py-2.5 border border-gray-300 rounded-lg bg-white hover:border-[#a79de9] transition-all appearance-none">
      <option value="" disabled selected>Selecione a forma</option>
      <option v-for="(label, value) in formaChoices" :key="value" :value="value">
        {{ label }}
      </option>
    </select>
    <span class="material-symbols-outlined absolute right-3 top-1/2 transform -translate-y-1/2 text-[#615c8e] pointer-events-none"></span>
  </div>
              <!-- Valor Field -->
              <div class="relative w-48">
                <label class="block text-sm font-medium text-[#615c8e] mb-1" for="valor">
                  Valor Total <span class="text-red-500 ml-1">*</span>
                </label>
                <div class="relative">
                  <span class="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-500">R$</span>
                  <input v-model="transaction.valor" type="text"
                    class="pl-8 w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#a79de9] focus:border-transparent hover:border-[#a79de9] transition-all"
                    placeholder="0,00" @input="formatCurrency" />
                </div>
              </div>

              <!-- Parcelas Field -->
              <div>
                <label class="block text-sm font-medium text-[#615c8e] mb-1" for="parcelas">
                  Número de Parcelas
                </label>
                <div class="relative">
                  <input v-model="transaction.parcelas" type="number" min="1" max="20"
                    class="px-4 py-2.5 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#a79de9] focus:border-transparent hover:border-[#a79de9] transition-all"
                    style="width:120px" />
                </div>
              </div>

              <!-- Descrição Field -->
              <div class="md:col-span-2">
                <label class="block text-sm font-medium text-[#615c8e] mb-1" for="descricao">
                  Descrição <span class="text-red-500 ml-1">*</span>
                </label>
                <textarea v-model="transaction.descricao"
                  class="w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#a79de9] focus:border-transparent hover:border-[#a79de9] transition-all resize-none"
                  rows="2" maxlength="300" placeholder="Digite uma descrição para esta transação"></textarea>
                <p class="text-xs text-gray-500 mt-1 text-right">{{ transaction.descricao ? transaction.descricao.length
                  : 0 }}/300 caracteres</p>
              </div>

              <!-- Data Field -->
              <div>
                <label class="block text-sm font-medium text-[#615c8e] mb-1" for="data">
                  Data da Transação <span class="text-red-500 ml-1">*</span>
                </label>
                <div class="relative">
                  <input v-model="transaction.data" type="date"
                    class="w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#a79de9] focus:border-transparent hover:border-[#a79de9] transition-all" />
                  <span
                    class="material-symbols-outlined absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-500 pointer-events-none"></span>
                </div>
              </div>
            </div>
          </div>

          <!-- Compartilhamento Section -->
          <details class="bg-white rounded-lg p-6 mb-6 shadow group">
            <summary class="list-none cursor-pointer">
              <div class="flex justify-between items-center">
                <h2 class="text-xl font-semibold text-[#282641] mb-0 flex items-center">
                  <span class="material-symbols-outlined mr-2">group</span> Compartilhamento
                </h2>
                <span
                  class="material-symbols-outlined transform group-open:rotate-180 transition-transform text-[#615c8e]">expand_more</span>
              </div>
            </summary>
            <div class="mt-4 pt-4 border-t border-gray-100">
              <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
                <div>
                  <label class="block text-sm font-medium text-[#615c8e] mb-1" for="porcentagemTotal">
                    Porcentagem total a compartilhar:
                    <span class="text-[#282641] font-semibold ml-1">{{ compartilhamento.porcentagemTotal }}%</span>
                  </label>
                  <input type="range" min="0" max="100" v-model="compartilhamento.porcentagemTotal"
                    class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer accent-[#615c8e]" />
                  <div class="flex justify-between text-xs text-gray-500 mt-1">
                    <span>0%</span>
                    <span>50%</span>
                    <span>100%</span>
                  </div>
                </div>
              </div>

              <div class="relative mb-4">
                <label class="block text-sm font-medium text-[#615c8e] mb-1" for="compartilharCom">
                  Compartilhar com
                </label>
                <details class="w-full cursor-pointer relative" @toggle="toggleUserDropdown">
                  <summary
                    class="list-none flex items-center justify-between w-full px-4 py-2.5 border border-gray-300 rounded-lg bg-white hover:border-[#a79de9] transition-all">
                    <span class="text-gray-500">
                      {{compartilhamento.usuarios.length > 0 ? compartilhamento.usuarios.map(u => u.name).join(', ') :
                      'Selecione os usuários'}}
                    </span>
                    <span
                      class="material-symbols-outlined text-[#615c8e] transition-transform group-open:rotate-180">expand_more</span>
                  </summary>
                  <div
                    class="absolute top-full left-0 w-full mt-1 bg-white border border-gray-200 rounded-lg shadow-lg z-10">
                    <div class="p-2">
                      <input type="text" v-model="userSearch"
                        class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-1 focus:ring-[#a79de9] mb-2"
                        placeholder="Buscar usuários..." />
                    </div>
                    <ul class="py-1 max-h-60 overflow-y-auto">
                      <li v-for="user in filteredUsers" :key="user.id"
                        class="px-4 py-2 hover:bg-[#eed4ed] text-[#282641] cursor-pointer transition-colors">
                        <label class="flex items-center space-x-2 cursor-pointer">
                          <input type="checkbox" class="rounded text-[#615c8e] focus:ring-[#a79de9]"
                            :checked="compartilhamento.usuarios.some(u => u.id === user.id)"
                            @change="toggleUserSelection(user)" />
                          <span class="flex items-center">
                            <span
                              class="w-8 h-8 rounded-full bg-[#a79de9] flex items-center justify-center text-white mr-2">
                              {{ getInitials(user.name) }}
                            </span>
                            {{ user.name }}
                          </span>
                        </label>
                      </li>
                    </ul>
                  </div>
                </details>
              </div>

              <div v-if="compartilhamento.usuarios.length > 0" class="space-y-4">
                <div v-for="(user, index) in compartilhamento.usuarios" :key="user.id"
                  class="p-4 bg-[#f5f5ff] rounded-lg">
                  <div class="flex items-center mb-3">
                    <span class="w-8 h-8 rounded-full bg-[#a79de9] flex items-center justify-center text-white mr-2">
                      {{ getInitials(user.name) }}
                    </span>
                    <span class="font-medium">{{ user.name }}</span>
                  </div>

                  <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                      <label class="block text-sm font-medium text-[#615c8e] mb-1">
                        Porcentagem deste usuário:
                        <span class="text-[#282641] font-semibold">{{ user.porcentagem.toFixed(1) }}%</span>
                      </label>
                      <input type="range" min="0" max="100" v-model.number="user.porcentagem"
                        @input="updateUserPercentage(index, $event.target.value)"
                        class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer accent-[#615c8e]" />
                    </div>

                    <div>
                      <label class="block text-sm font-medium text-[#615c8e] mb-1">
                        Número de Parcelas
                      </label>
                      <select v-model.number="user.parcelas"
                        class="w-full px-4 py-2.5 border border-gray-300 rounded-lg bg-white hover:border-[#a79de9] transition-all">
                        <option value="1">À vista (1x)</option>
                        <option value="2">2x</option>
                        <option value="3">3x</option>
                        <option value="4">4x</option>
                        <option value="5">5x</option>
                        <option value="6">6x</option>
                        <option value="7">7x</option>
                        <option value="8">8x</option>
                        <option value="9">9x</option>
                        <option value="10">10x</option>
                        <option value="11">11x</option>
                        <option value="12">12x</option>
                      </select>
                    </div>
                  </div>

                  <div class="mt-3 text-sm">
                    <div class="flex justify-between">
                      <span class="text-[#615c8e]">Valor total:</span>
                      <span class="font-semibold">{{ formatCurrencyValue(calculateUserShare(user)) }}</span>
                    </div>
                    <div class="flex justify-between">
                      <span class="text-[#615c8e]">Valor por parcela:</span>
                      <span class="font-semibold">{{ formatCurrencyValue(calculateInstallmentValueForUser(user))
                        }}</span>
                    </div>
                  </div>
                </div>
              </div>

              <div class="mt-4 p-3 bg-[#eed4ed] bg-opacity-30 rounded-lg">
                <p class="text-sm text-[#282641]">Resumo do compartilhamento:</p>
                <div class="flex justify-between mt-2">
                  <div>
                    <p class="text-sm text-[#615c8e]">Valor total:</p>
                    <p class="font-semibold text-[#282641]">{{ formatCurrencyValue(transaction.valor || '0') }}</p>
                  </div>
                  <div>
                    <p class="text-sm text-[#615c8e]">Sua parte:</p>
                    <p class="font-semibold text-[#282641]">{{ formatCurrencyValue(calculateIndividualValue()) }}</p>
                  </div>
                  <div>
                    <p class="text-sm text-[#615c8e]">Parte compartilhada:</p>
                    <p class="font-semibold text-[#282641]">{{ formatCurrencyValue(calculateSharedAmount()) }}</p>
                  </div>
                </div>
              </div>
            </div>
          </details>

          <!-- Recorrência Section -->
          <details class="bg-white rounded-lg p-6 mb-6 shadow group">
            <summary class="list-none cursor-pointer">
              <div class="flex justify-between items-center">
                <h2 class="text-xl font-semibold text-[#282641] flex items-center">
                  <span class="material-symbols-outlined mr-2">repeat</span> Recorrência
                </h2>
                <span
                  class="material-symbols-outlined transform group-open:rotate-180 transition-transform text-[#615c8e]">expand_more</span>
              </div>
            </summary>
            <div class="mt-4 pt-4 border-t border-gray-100">
              <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div class="relative">
                  <label class="block text-sm font-medium text-[#615c8e] mb-1" for="frequencia">
                    Frequência
                  </label>
                  <select v-model="recorrencia.frequencia"
                    class="w-full px-4 py-2.5 border border-gray-300 rounded-lg bg-white hover:border-[#a79de9] transition-all appearance-none">
                    <option value="" disabled selected>Selecione a frequência</option>
                    <option value="Diária">Diária</option>
                    <option value="Semanal">Semanal</option>
                    <option value="Mensal">Mensal</option>
                    <option value="Anual">Anual</option>
                  </select>
                </div>
                <div>
                  <label class="block text-sm font-medium text-[#615c8e] mb-1" for="dataFinal">
                    Data de Término
                  </label>
                  <div class="relative">
                    <input v-model="recorrencia.dataFinal" type="date"
                      class="w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#a79de9] focus:border-transparent hover:border-[#a79de9] transition-all" />
                    <span
                      class="material-symbols-outlined absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-500 pointer-events-none"></span>
                  </div>
                </div>
              </div>

              <!-- Configuração Semanal -->
              <div v-if="recorrencia.frequencia === 'Semanal'" class="mt-6">
                <label class="block text-sm font-medium text-[#615c8e] mb-3">
                  Selecione os dias da semana:
                </label>
                <div class="flex flex-wrap gap-3">
                  <label v-for="day in diasDaSemana" :key="day.value"
                    class="flex items-center space-x-2 p-2 rounded-lg hover:bg-gray-50 cursor-pointer">
                    <input type="checkbox" v-model="recorrencia.diasSemana" :value="day.value"
                      class="h-5 w-5 rounded border-gray-300 text-[#615c8e] focus:ring-[#a79de9]">
                    <span>{{ day.label }}</span>
                  </label>
                </div>
              </div>

              <!-- Configuração Mensal -->
              <div v-if="recorrencia.frequencia === 'Mensal'" class="mt-6">
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <div>
                    <label class="block text-sm font-medium text-[#615c8e] mb-1">
                      Dia do mês
                    </label>
                    <select v-model="recorrencia.diaMes" class="w-full px-4 py-2.5 border border-gray-300 rounded-lg">
                      <option v-for="n in 31" :value="n" :key="n">{{ n }}</option>
                      <option value="ultimo">Último dia do mês</option>
                    </select>
                  </div>
                </div>
              </div>

              <!-- Configuração Anual -->
              <div v-if="recorrencia.frequencia === 'Anual'" class="mt-6">
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <div>
                    <label class="block text-sm font-medium text-[#615c8e] mb-1">
                      Dia
                    </label>
                    <select v-model="recorrencia.diaAnual" class="w-full px-4 py-2.5 border border-gray-300 rounded-lg">
                      <option v-for="n in 31" :value="n" :key="n">{{ n }}</option>
                      <option value="ultimo">Último dia do mês</option>
                    </select>
                  </div>
                  <div>
                    <label class="block text-sm font-medium text-[#615c8e] mb-1">
                      Mês
                    </label>
                    <select v-model="recorrencia.mesAnual" class="w-full px-4 py-2.5 border border-gray-300 rounded-lg">
                      <option v-for="(mes, index) in meses" :value="index + 1" :key="index">
                        {{ mes }}
                      </option>
                    </select>
                  </div>
                </div>
              </div>
            </div>
          </details>

          <!-- NFC-e Section -->
          <details class="bg-white rounded-lg p-6 mb-6 shadow group" :open="qrScannerActive">
            <summary class="list-none cursor-pointer">
              <div class="flex justify-between items-center">
                <h2 class="text-xl font-semibold text-[#282641] flex items-center">
                  <span class="material-symbols-outlined mr-2">qr_code_scanner</span> NFC-e / Cupom Fiscal
                </h2>
                <span
                  class="material-symbols-outlined transform group-open:rotate-180 transition-transform text-[#615c8e]">expand_more</span>
              </div>
            </summary>
            <div class="mt-4 pt-4 border-t border-gray-100">
              <div class="flex flex-col md:flex-row gap-4">
                <div class="flex-1">
                  <label class="block text-sm font-medium text-[#615c8e] mb-1" for="qrcode">
                    QR Code da NFC-e
                  </label>
                  <textarea v-model="nfce.qrcode"
                    class="w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#a79de9] focus:border-transparent hover:border-[#a79de9] transition-all resize-none"
                    rows="3" placeholder="Cole o texto do QR Code aqui"></textarea>
                </div>
                <div class="flex flex-col justify-end">
                  <button @click="toggleQRScanner" type="button"
                    class="bg-[#a79de9] hover:bg-[#615c8e] text-white font-medium py-2.5 px-4 rounded-lg transition-colors flex items-center justify-center">
                    <span class="material-symbols-outlined mr-2">qr_code_scanner</span>
                    {{ qrScannerActive ? 'Parar Leitura' : 'Ler NFC-e' }}
                  </button>
                  <p class="text-xs text-center mt-2 text-gray-500">Ou escaneie usando câmera</p>
                </div>
              </div>

              <!-- QR Code Scanner Container -->
              <div v-if="qrScannerActive" id="qr-reader" class="mt-4 w-full h-64 bg-black rounded-lg overflow-hidden">
              </div>

              <!-- Dados extraídos (opcional, para debug) -->
              <div v-if="nfce.qrcode" class="mt-4 p-3 bg-gray-100 rounded-lg">

              </div>
            </div>
          </details>

<!-- Buttons -->
<div class="flex justify-end space-x-4 mt-6">
  <button
    @click="cancelTransaction"
    class="border border-[#615c8e] text-[#615c8e] hover:bg-[#eed4ed] hover:bg-opacity-30 font-medium py-2.5 px-6 rounded-full transition-colors">
    Cancelar
  </button>
  
  <button 
    @click="submitTransaction"
    :disabled="!isFormValid || isSaving"
    class="bg-[#615c8e] hover:bg-[#282641] text-white font-medium py-2.5 px-6 rounded-full transition-colors flex items-center disabled:opacity-50 disabled:cursor-not-allowed">
    <span v-if="isSaving" class="material-symbols-outlined mr-2 animate-spin">refresh</span>
    <span v-else class="material-symbols-outlined mr-2">save</span> 
    {{ isSaving ? 'Salvando...' : 'Salvar Transação' }}
  </button>
</div>

        </div>

        <!-- Summary Section -->
        <div class="w-full md:w-1/4 bg-[#282641] p-6 text-white">
          <h2 class="text-xl font-semibold mb-6 flex items-center">
            <span class="material-symbols-outlined mr-2">summarize</span> Resumo da Transação
          </h2>
          <div class="bg-[#615c8e] rounded-lg p-4 mb-6 hover:bg-[#6d68a0] transition-colors">
            <div class="flex items-center justify-between mb-3">
              <span class="text-sm opacity-80">Valor Total:</span>
              <span class="text-lg font-bold">{{ formatCurrencyValue(transaction.valor) }}</span>
            </div>
            <div class="flex items-center justify-between mb-3">
              <span class="text-sm opacity-80">Valor Individual:</span>
              <span class="text-lg font-bold">{{ formatCurrencyValue(calculateIndividualValue()) }}</span>
            </div>
            <div class="flex items-center justify-between">
              <span class="text-sm opacity-80">Parcelas:</span>
              <span class="text-lg font-bold">{{ transaction.parcelas || 1 }}x</span>
            </div>
          </div>

          <!-- Shared With Section -->
          <div v-if="compartilhamento.usuarios.length > 0" class="mb-6">
            <h3 class="text-md font-medium mb-3">Compartilhado com:</h3>
            <div class="space-y-2">
              <div v-for="user in compartilhamento.usuarios" :key="user.id"
                class="flex items-center justify-between bg-[#615c8e] bg-opacity-50 rounded-lg p-2 hover:bg-opacity-70 transition-colors">
                <div class="flex items-center">
                  <span class="w-8 h-8 rounded-full bg-[#a79de9] flex items-center justify-center text-white mr-2">
                    {{ getInitials(user.name) }}
                  </span>
                  <div>
                    <div>{{ user.name }}</div>
                    <div class="text-xs opacity-80">{{ user.parcelas }}x de {{
                      formatCurrencyValue(calculateInstallmentValueForUser(user)) }}</div>
                  </div>
                </div>
                <div class="text-right">
                  <span class="font-medium">{{ formatCurrencyValue(calculateUserShare(user)) }}</span>
                  <div class="text-xs opacity-80">{{ user.porcentagem.toFixed(1) }}%</div>
                </div>
              </div>
            </div>
          </div>
          <!-- Installments Section -->
          <div>
            <h3 class="text-md font-medium mb-3">Parcelas:</h3>
            <div class="space-y-2">
              <div v-for="n in parseInt(transaction.parcelas || 1)" :key="n"
                :class="['flex justify-between rounded-lg p-2 transition-colors',
                  n === 1 ? 'bg-[#615c8e] bg-opacity-50' : 'bg-[#615c8e] bg-opacity-20 opacity-70 hover:bg-opacity-30']">
                <span>{{ n }}ª Parcela</span>
                <span class="font-medium">{{ formatCurrencyValue(calculateInstallmentValue(n)) }}</span>
              </div>
            </div>
          </div>

          <!-- Transaction Info -->
          <div class="mt-6 border-t border-[#615c8e] pt-4">
            <div class="flex justify-between items-center">
              <span class="text-sm opacity-80">Data:</span>
              <span>{{ transaction.data ? formatDate(transaction.data) : '--/--/----' }}</span>
            </div>
            <div class="flex justify-between items-center mt-2">
              <span class="text-sm opacity-80">Categoria:</span>
              <span>{{ transaction.categoria || 'Não definida' }}</span>
            </div>
            <div class="flex justify-between items-center mt-2">
              <span class="text-sm opacity-80">Banco:</span>
              <span>{{ transaction.banco || 'Não definido' }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios';
import Swal from 'sweetalert2';
import Header from '../components/Header.vue';
import { Html5Qrcode } from 'html5-qrcode';

export default {
  components: {
    Header,
  },

  data() {
    return {
      apiUrl: process.env.VUE_APP_API_URL,
      isSaving: false,
      notifications: [],
      transaction: {
        banco: '',
        categoria: '',
        tipo: '',
        forma: '',
        valor: '',
        parcelas: 1,
        descricao: '',
        data: this.getCurrentDate(),
        status_pagamento: 'Pendente'
      },
            loadingChoices: true,
            bancoChoices: {},
      categoriaChoices: {},
      tipoChoices: {},
      formaChoices: {},
      statusPagamentoChoices: {},
      compartilhamento: {
        ativo: false,
        usuarios: [],
        porcentagemTotal: 50
      },
      recorrencia: {
        ativo: false,
        frequencia: '',
        dataFinal: '',
        diasSemana: [],
        diaMes: 1,
        diaAnual: 1,
        mesAnual: new Date().getMonth() + 1
      },
      nfce: {
        qrcode: ''
      },
      userSearch: '',
      availableUsers: [
        { id: 1, name: 'João Dias' },
        { id: 2, name: 'Maria Silva' },
        { id: 3, name: 'Luiz Santos' },
        { id: 4, name: 'Ana Oliveira' },
        { id: 5, name: 'Carlos Souza' }
      ],
      diasDaSemana: [
        { value: 'seg', label: 'Segunda-feira' },
        { value: 'ter', label: 'Terça-feira' },
        { value: 'qua', label: 'Quarta-feira' },
        { value: 'qui', label: 'Quinta-feira' },
        { value: 'sex', label: 'Sexta-feira' },
        { value: 'sab', label: 'Sábado' },
        { value: 'dom', label: 'Domingo' }
      ],
      meses: [
        'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
        'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
      ],
      qrScannerActive: false,
      qrScanner: null
    };
  },

  computed: {
    isFormValid() {
      const requiredFields = [
        'banco', 'categoria', 'tipo', 'forma', 'valor', 'descricao', 'data'
      ];
      
      const basicValid = requiredFields.every(field => 
        this.transaction[field] && this.transaction[field].toString().trim()
      );
      
      const valueValid = this.transaction.valor && 
        !isNaN(parseFloat(this.transaction.valor.replace(/\./g, '').replace(',', '.')));
      
      return basicValid && valueValid;
    },
    
    filteredUsers() {
      return this.availableUsers.filter(user =>
        user.name.toLowerCase().includes(this.userSearch.toLowerCase())
      );
    },
    
    totalSharedPercentage() {
      return this.compartilhamento.usuarios.reduce((sum, user) => sum + user.porcentagem, 0);
    }
  },

  methods: {
      getToken() {
  // Sempre usar a mesma chave 'token' em todo o código
  return localStorage.getItem('token');
},
   async submitTransaction() {
  const token = localStorage.getItem('token');
  if (!token) {
    this.showToast('error', 'Erro', 'Faça login novamente');
    this.$router.push('/painel');
    return;
  }

  this.isSaving = true;
  
  try {
    // Validação do status_pagamento
    if (this.transaction.forma !== 'Crédito') {
      this.transaction.status_pagamento = 'Pago';
    }

    const transactionData = {
      ...this.transaction,
      valor: parseFloat(this.transaction.valor.replace(/\./g, '').replace(',', '.'))
    };

    // DEBUG: Mostra os dados que estão sendo enviados
    console.log('Enviando dados:', transactionData);
    console.log('Token usado:', token);

    const response = await axios.post(`${this.apiUrl}/api/transactions/`, transactionData, {
      headers: {
        'Authorization': `Token ${token}`,
        'Content-Type': 'application/json'
      }
    });

    // DEBUG: Mostra a resposta do servidor
    console.log('Resposta do servidor:', response.data);
    
    this.showToast('success', 'Sucesso', 'Transação salva com sucesso!');
    this.resetForm();
    
  } catch (error) {
    // DEBUG: Mostra o erro completo
    console.error('Erro completo:', error);
    
    if (error.response?.status === 401) {
      localStorage.removeItem('token');
      this.showToast('error', 'Sessão expirada', 'Faça login novamente');
      this.$router.push('/painel');
    } else {
      const errorMsg = error.response?.data?.detail || 
                      error.message || 
                      'Erro ao salvar transação';
      this.showToast('error', 'Erro', errorMsg);
    }
  } finally {
    this.isSaving = false;
  }
},
   handleError(error) {
  let errorMessage = 'Erro ao processar a requisição';
  
  if (error.response) {
    console.error('Detalhes do erro:', {
      status: error.response.status,
      data: error.response.data,
      headers: error.response.headers
    });

    switch (error.response.status) {
      case 401:
        errorMessage = 'Sessão expirada. Por favor, faça login novamente.';
        localStorage.removeItem('token');
        this.$router.push('/painel');
        break;
      case 403:
        errorMessage = 'Você não tem permissão para esta ação.';
        break;
      case 400:
        errorMessage = 'Dados inválidos: ';
        if (error.response.data) {
          errorMessage += JSON.stringify(error.response.data);
        }
        break;
      default:
        errorMessage = this.parseBackendError(error.response.data);
    }
  } else if (error.request) {
    errorMessage = 'Sem resposta do servidor';
  } else {
    errorMessage = error.message;
  }
  
  this.showToast('error', 'Erro', errorMessage);
},

parseBackendError(data) {
  if (typeof data === 'string') return data;
  if (data.detail) return data.detail;
  if (data.non_field_errors) return data.non_field_errors.join(', ');
  
  let messages = [];
  for (const [key, value] of Object.entries(data)) {
    messages.push(`${key}: ${Array.isArray(value) ? value.join(', ') : value}`);
  }
  
  return messages.join('; ');
},
  async fetchChoices() {
  this.loadingChoices = true;
  const token = this.getToken();
  
  if (!token) {
    console.error('Token não disponível');
    this.loadingChoices = false;
    return;
  }
  
  try {
    const response = await axios.get(`${this.apiUrl}/api/transaction-choices/`, {
      headers: {
        'Authorization': `Token ${token}`
      }
    });
    
    console.log('Dados recebidos:', response.data);
    
    // Atribui os dados corretamente
    this.bancoChoices = response.data.bancos || {};
    this.categoriaChoices = response.data.categorias || {};
    this.tipoChoices = response.data.tipos || {};
    this.formaChoices = response.data.formas || {};
    this.statusPagamentoChoices = response.data.status_pagamento || {};
    
    console.log('Choices após atribuição:', {
      bancos: this.bancoChoices,
      categorias: this.categoriaChoices,
      tipos: this.tipoChoices,
      formas: this.formaChoices,
      status: this.statusPagamentoChoices
    });
    
  } catch (error) {
    console.error('Erro ao buscar choices:', error);
    this.handleError(error);
  } finally {
    this.loadingChoices = false;
  }
},
    resetForm() {
      this.transaction = {
        banco: '',
        categoria: '',
        tipo: '',
        forma: '',
        valor: '',
        parcelas: 1,
        descricao: '',
        data: this.getCurrentDate(),
        status_pagamento: 'Pendente'
      };
      this.compartilhamento.usuarios = [];
      this.compartilhamento.porcentagemTotal = 50;
    },

    showToast(icon, title, text = '') {
      const Toast = Swal.mixin({
        toast: true,
        position: 'top-end',
        showConfirmButton: false,
        timer: 3000,
        timerProgressBar: true,
        didOpen: (toast) => {
          toast.addEventListener('mouseenter', Swal.stopTimer);
          toast.addEventListener('mouseleave', Swal.resumeTimer);
        }
      });
      
      Toast.fire({
        icon,
        title,
        text: text.length > 100 ? text.substring(0, 100) + '...' : text
      });
    },

    addNotification(type, title, message) {
      const notification = { 
        type, 
        title, 
        message,
        id: Date.now() 
      };
      
      this.notifications.push(notification);
      
      setTimeout(() => {
        this.notifications = this.notifications.filter(n => n.id !== notification.id);
      }, 5000);
    },

    getCurrentDate() {
      const today = new Date();
      const year = today.getFullYear();
      const month = String(today.getMonth() + 1).padStart(2, '0');
      const day = String(today.getDate()).padStart(2, '0');
      return `${year}-${month}-${day}`;
    },

    formatDate(dateString) {
      if (!dateString) return '--/--/----';
      const [year, month, day] = dateString.split('-');
      return `${day}/${month}/${year}`;
    },

    formatCurrency(event) {
      let value = event.target.value.replace(/\D/g, '');
      value = (value / 100).toFixed(2) + '';
      value = value.replace('.', ',');
      value = value.replace(/(\d)(?=(\d{3})+(?!\d))/g, '$1.');

      if (value === '0,00') {
        this.transaction.valor = '';
      } else {
        this.transaction.valor = value;
      }
    },

formatCurrencyValue(value) {
  if (!value) return 'R$ 0,00';
  
  // Se já for número, formata diretamente
  if (typeof value === 'number') {
    return 'R$ ' + value.toLocaleString('pt-BR', {
      minimumFractionDigits: 2,
      maximumFractionDigits: 2
    });
  }
  
  // Se for string, converte para número primeiro
  const numericValue = typeof value === 'string' 
    ? parseFloat(value.replace(/\./g, '').replace(',', '.')) 
    : value;
    
  return 'R$ ' + numericValue.toLocaleString('pt-BR', {
    minimumFractionDigits: 2,
    maximumFractionDigits: 2
  });
},

    getInitials(name) {
      if (!name || typeof name !== 'string') return '';
      return name.split(' ').map(n => n[0]).join('').toUpperCase();
    },

    calculateIndividualValue() {
      if (!this.transaction.valor) return 0;
      const numericValue = parseFloat(this.transaction.valor.replace(/\./g, '').replace(',', '.'));

      if (this.compartilhamento.usuarios.length > 0) {
        const sharedAmount = numericValue * (this.compartilhamento.porcentagemTotal / 100);
        return numericValue - sharedAmount;
      }
      return numericValue;
    },

    calculateSharedAmount() {
      if (!this.transaction.valor || this.compartilhamento.usuarios.length === 0) {
        return 0;
      }
      const numericValue = parseFloat(this.transaction.valor.replace(/\./g, '').replace(',', '.'));
      return numericValue * (this.compartilhamento.porcentagemTotal / 100);
    },

    calculateUserShare(user) {
      if (!this.transaction.valor) return 0;
      const numericValue = parseFloat(this.transaction.valor.replace(/\./g, '').replace(',', '.'));
      const sharedAmount = numericValue * (this.compartilhamento.porcentagemTotal / 100);
      const userPercentage = user.porcentagem / this.totalSharedPercentage;
      return sharedAmount * userPercentage;
    },

    calculateInstallmentValueForUser(user) {
      const share = this.calculateUserShare(user);
      return share / user.parcelas;
    },

    calculateInstallmentValue(installmentNumber) {
      if (!this.transaction.valor) return 0;
      const numericValue = parseFloat(this.transaction.valor.replace(/\./g, '').replace(',', '.'));
      const totalParcels = parseInt(this.transaction.parcelas) || 1;
      return numericValue / totalParcels;
    },

    toggleUserSelection(user) {
      const index = this.compartilhamento.usuarios.findIndex(u => u.id === user.id);

      if (index === -1) {
        const newUser = {
          id: user.id,
          name: user.name,
          porcentagem: 0,
          parcelas: 1
        };
        this.compartilhamento.usuarios.push(newUser);
        this.distributePercentages();
      } else {
        this.compartilhamento.usuarios.splice(index, 1);
      }
    },

    distributePercentages() {
      const userCount = this.compartilhamento.usuarios.length;
      if (userCount === 0) return;
      const equalShare = 100 / userCount;
      this.compartilhamento.usuarios.forEach(user => {
        user.porcentagem = equalShare;
      });
    },

    updateUserPercentage(index, value) {
      const numericValue = parseFloat(value) || 0;
      this.compartilhamento.usuarios[index].porcentagem = numericValue;
      this.normalizePercentages();
    },

    normalizePercentages() {
      const total = this.totalSharedPercentage;
      if (total > 100) {
        const ratio = 100 / total;
        this.compartilhamento.usuarios.forEach(user => {
          user.porcentagem = user.porcentagem * ratio;
        });
      }
    },

    toggleUserDropdown(event) {
      if (event.target.open) {
        this.userSearch = '';
      }
    },

    toggleQRScanner() {
      if (this.qrScannerActive) {
        this.stopQRScanner();
      } else {
        this.startQRScanner();
      }
    },

    startQRScanner() {
      this.qrScannerActive = true;
      this.$nextTick(() => {
        const config = {
          fps: 10,
          qrbox: { width: 250, height: 250 },
          aspectRatio: 1.0
        };

        this.qrScanner = new Html5Qrcode("qr-reader");
        this.qrScanner.start(
          { facingMode: "environment" },
          config,
          this.onQRScanSuccess,
          this.onQRScanError
        ).catch(err => {
          console.error("Erro ao iniciar scanner:", err);
          this.showToast('error', 'Erro', 'Não foi possível acessar a câmera');
          this.qrScannerActive = false;
        });
      });
    },

    stopQRScanner() {
      if (this.qrScanner) {
        this.qrScanner.stop().then(() => {
          this.qrScannerActive = false;
          this.qrScanner = null;
        }).catch(err => {
          console.error("Erro ao parar scanner:", err);
        });
      }
    },

    onQRScanSuccess(decodedText) {
      this.nfce.qrcode = decodedText;
      this.parseQRCodeData(decodedText);
      this.stopQRScanner();
    },

    onQRScanError(errorMessage) {
      console.log("Erro na leitura QR:", errorMessage);
    },

    parseQRCodeData(qrData) {
      try {
        if (qrData.includes('|')) {
          const valorMatch = qrData.match(/[vV]alorTotal=([0-9,]+)/);
          if (valorMatch && valorMatch[1]) {
            this.transaction.valor = parseFloat(valorMatch[1].replace(',', '.')).toFixed(2).replace('.', ',');
          }

          const dataMatch = qrData.match(/[dD]ata=(\d{8})/);
          if (dataMatch && dataMatch[1]) {
            const dataStr = dataMatch[1];
            this.transaction.data = `${dataStr.substring(0, 4)}-${dataStr.substring(4, 6)}-${dataStr.substring(6, 8)}`;
          }

          // Categorias automáticas
          if (qrData.toLowerCase().includes('supermercado') || qrData.toLowerCase().includes('mercado')) {
            this.transaction.categoria = 'Alimentação';
          } else if (qrData.toLowerCase().includes('posto') || qrData.toLowerCase().includes('combustível')) {
            this.transaction.categoria = 'Transporte';
          } else if (qrData.toLowerCase().includes('farmacia') || qrData.toLowerCase().includes('drogaria')) {
            this.transaction.categoria = 'Saúde';
          }

          this.transaction.forma = 'Débito';

          const cnpjMatch = qrData.match(/\d{14}/);
          const nomeMatch = qrData.match(/nome=([^|]+)/i);
          if (cnpjMatch || nomeMatch) {
            let descricao = 'Compra NFC-e';
            if (nomeMatch && nomeMatch[1]) descricao += ` em ${nomeMatch[1]}`;
            if (cnpjMatch) descricao += ` (CNPJ: ${cnpjMatch[0]})`;
            this.transaction.descricao = descricao.substring(0, 300);
          }
        }
      } catch (error) {
        console.error("Erro ao processar QR Code:", error);
      }
    }
  },

async created() {
  // Verificação do token
  if (!localStorage.getItem('authToken')) {
    const token = this.getToken();
    if (token) {
      localStorage.setItem('authToken', token);
      
      if (window.location.search.includes('token')) {
        window.history.replaceState({}, document.title, window.location.pathname);
      }
    }
  }
  
  // Carrega as choices
  try {
    await this.fetchChoices();
  } catch (error) {
    console.error('Erro ao carregar opções:', error);
    this.showToast('error', 'Erro', 'Não foi possível carregar as opções');
  }
  
  console.log('Token atual:', this.getToken());
},

  beforeUnmount() {
    if (this.qrScannerActive && this.qrScanner) {
      this.stopQRScanner();
    }
  }
};
</script>
<style scoped>
@import url(https://fonts.googleapis.com/css2?family=Open+Sans&display=swap);
@import url(https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200);



.swal2-toast {
  font-family: 'Open Sans', sans-serif;
  border-radius: 8px !important;
}

.swal2-toast.swal2-success {
  background: #615c8e !important;
  color: white !important;
}

.swal2-toast.swal2-error {
  background: #ff4444 !important;
  color: white !important;
}

#root .flex {
  display: flex;
}

#root .flex-col {
  flex-direction: column;
}

#root .flex-row {
  flex-direction: row;
}

#root .items-center {
  align-items: center;
}

#root .justify-center {
  justify-content: center;
}

#root .justify-between {
  justify-content: space-between;
}

#root .justify-end {
  justify-content: flex-end;
}

#root .gap-4 {
  gap: 16px;
}

#root .space-y-2> :not([hidden])~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-bottom: calc(8px * var(--tw-space-y-reverse));
  margin-top: calc(8px * (1 - var(--tw-space-y-reverse)));
}

#root .space-x-4> :not([hidden])~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-left: calc(16px * (1 - var(--tw-space-x-reverse)));
  margin-right: calc(16px * var(--tw-space-x-reverse));
}

#root .grid {
  display: grid;
}

#root .grid-cols-1 {
  grid-template-columns: repeat(1, minmax(0, 1fr));
}

#root .grid-cols-3 {
  grid-template-columns: repeat(3, minmax(0, 1fr));
}

#root .relative {
  position: relative;
}

#root .absolute {
  position: absolute;
}

#root .top-1\/2 {
  top: 50%;
}

#root .top-full {
  top: 100%;
}

#root .left-0 {
  left: 0;
}

#root .left-3 {
  left: 12px;
}

#root .right-2 {
  right: 8px;
}

#root .right-3 {
  right: 12px;
}

#root .z-10 {
  z-index: 10;
}

#root .h-2 {
  height: 8px;
}

#root .h-6 {
  height: 24px;
}

#root .h-8 {
  height: 32px;
}

#root .max-h-60 {
  max-height: 240px;
}

#root .w-11 {
  width: 44px;
}

#root .w-48 {
  width: 192px;
}

#root .w-8 {
  width: 32px;
}

#root .w-\[1200px\] {
  width: 1200px;
}

#root .w-full {
  width: 100%;
}

#root .min-h-screen {
  min-height: 100vh;
}

#root .flex-1 {
  flex: 1 1 0%;
}

#root .transform {
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

#root .-translate-y-1\/2 {
  --tw-translate-y: -50%;
}

#root .cursor-pointer {
  cursor: pointer;
}

#root .list-none {
  list-style-type: none;
}

#root .overflow-hidden {
  overflow: hidden;
}

#root .overflow-y-auto {
  overflow-y: auto;
}

#root .rounded-lg {
  border-radius: 24px;
}

#root .rounded-full {
  border-radius: 9999px;
}

#root .border {
  border-width: 1px;
}

#root .border-t {
  border-top-width: 1px;
}

#root .border-gray-100 {
  border-color: rgb(243 244 246);
}

#root .border-gray-200 {
  border-color: rgb(229 231 235);
}

#root .border-gray-300 {
  border-color: rgb(209 213 219);
}

#root .border-\[\#615c8e\] {
  border-color: rgb(97 92 142);
}

#root .bg-white {
  background-color: rgb(255 255 255);
}

#root .bg-\[\#282641\] {
  background-color: rgb(40 38 65);
}

#root .bg-\[\#615c8e\] {
  background-color: rgb(97 92 142);
}

#root .bg-\[\#a79de9\] {
  background-color: rgb(167 157 233);
}

#root .bg-\[\#eed4ed\] {
  background-color: rgb(238 212 237);
}

#root .bg-gray-200 {
  background-color: rgb(229 231 235);
}

#root .bg-opacity-20 {
  background-opacity: 0.2;
}

#root .bg-opacity-30 {
  background-opacity: 0.3;
}

#root .bg-opacity-50 {
  background-opacity: 0.5;
}

#root .p-2 {
  padding: 8px;
}

#root .p-3 {
  padding: 12px;
}

#root .p-4 {
  padding: 16px;
}

#root .p-6 {
  padding: 24px;
}

#root .px-3 {
  padding-left: 12px;
  padding-right: 12px;
}

#root .px-4 {
  padding-left: 16px;
  padding-right: 16px;
}

#root .px-6 {
  padding-left: 24px;
  padding-right: 24px;
}

#root .py-1 {
  padding-top: 4px;
  padding-bottom: 4px;
}

#root .py-2 {
  padding-top: 8px;
  padding-bottom: 8px;
}

#root .py-2\.5 {
  padding-top: 10px;
  padding-bottom: 10px;
}

#root .pl-8 {
  padding-left: 32px;
}

#root .pt-4 {
  padding-top: 16px;
}

#root .text-center {
  text-align: center;
}

#root .text-right {
  text-align: right;
}

#root .font-sans {
  font-family: Open Sans, ui-sans-serif, system-ui, sans-serif;
}

#root .text-xs {
  font-size: 12px;
  line-height: 1.6;
}

#root .text-sm {
  font-size: 14px;
  line-height: 1.5;
}

#root .text-lg {
  font-size: 18px;
  line-height: 1.5;
}

#root .text-xl {
  font-size: 20px;
  line-height: 1.4;
}

#root .text-3xl {
  font-size: 30px;
  line-height: 1.2;
}

#root .font-medium {
  font-weight: 500;
}

#root .font-semibold {
  font-weight: 600;
}

#root .font-bold {
  font-weight: 700;
}

#root .text-\[\#282641\] {
  color: rgb(40 38 65);
}

#root .text-\[\#615c8e\] {
  color: rgb(97 92 142);
}

#root .text-gray-500 {
  color: rgb(107 114 128);
}

#root .text-red-500 {
  color: rgb(239 68 68);
}

#root .text-white {
  color: rgb(255 255 255);
}

#root .accent-\[\#615c8e\] {
  accent-color: #615c8e;
}

#root .opacity-70 {
  opacity: 0.7;
}

#root .opacity-80 {
  opacity: 0.8;
}

#root .shadow {
  box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px -1px rgba(0, 0, 0, 0.1);
}

#root .shadow-lg {
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.1);
}

#root .transition-all {
  transition: all 0.15s cubic-bezier(0.4, 0, 0.2, 1);
}

#root .transition-colors {
  transition: color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1);
}

#root .transition-transform {
  transition: transform 0.15s cubic-bezier(0.4, 0, 0.2, 1);
}

#root .resize-none {
  resize: none;
}

#root .mb-0 {
  margin-bottom: 0;
}

#root .mb-1 {
  margin-bottom: 4px;
}

#root .mb-2 {
  margin-bottom: 8px;
}

#root .mb-3 {
  margin-bottom: 12px;
}

#root .mb-4 {
  margin-bottom: 16px;
}

#root .mb-6 {
  margin-bottom: 24px;
}

#root .ml-1 {
  margin-left: 4px;
}

#root .ml-3 {
  margin-left: 12px;
}

#root .mr-2 {
  margin-right: 8px;
}

#root .mt-1 {
  margin-top: 4px;
}

#root .mt-2 {
  margin-top: 8px;
}

#root .mt-4 {
  margin-top: 16px;
}

#root .mt-6 {
  margin-top: 24px;
}

#root .pointer-events-none {
  pointer-events: none;
}

/* Hover states */
#root .hover\:border-\[\#a79de9\]:hover {
  border-color: rgb(167 157 233);
}

#root .hover\:bg-\[\#282641\]:hover {
  background-color: rgb(40 38 65);
}

#root .hover\:bg-\[\#615c8e\]:hover {
  background-color: rgb(97 92 142);
}

#root .hover\:bg-\[\#6d68a0\]:hover {
  background-color: rgb(109 104 160);
}

#root .hover\:bg-\[\#eed4ed\]:hover {
  background-color: rgb(238 212 237);
}

#root .hover\:bg-opacity-30:hover {
  background-opacity: 0.3;
}

#root .hover\:bg-opacity-70:hover {
  background-opacity: 0.7;
}

/* Focus states */
#root .focus\:border-transparent:focus {
  border-color: transparent;
}

#root .focus\:outline-none:focus {
  outline: 2px solid transparent;
  outline-offset: 2px;
}

#root .focus\:ring-1:focus {
  box-shadow: 0 0 0 1px var(--tw-ring-color);
}

#root .focus\:ring-2:focus {
  box-shadow: 0 0 0 2px var(--tw-ring-color);
}

#root .focus\:ring-\[\#a79de9\]:focus {
  --tw-ring-color: rgb(167 157 233);
}

/* Group states */
#root .group-open\:rotate-180[open] {
  transform: rotate(180deg);
}

/* Peer states */
#root .peer:checked~.peer-checked\:bg-\[\#615c8e\] {
  background-color: rgb(97 92 142);
}

#root .peer:checked~.peer-checked\:after\:translate-x-full:after {
  transform: translateX(100%);
}

#root .peer:checked~.peer-checked\:after\:border-white:after {
  border-color: rgb(255 255 255);
}

#root .peer:focus~.peer-focus\:ring-2 {
  box-shadow: 0 0 0 2px var(--tw-ring-color);
}

#root .peer:focus~.peer-focus\:ring-\[\#a79de9\] {
  --tw-ring-color: rgb(167 157 233);
}

/* Responsive */
@media (min-width: 768px) {
  #root .md\:flex-row {
    flex-direction: row;
  }

  #root .md\:w-1\/4 {
    width: 25%;
  }

  #root .md\:w-3\/4 {
    width: 75%;
  }

  #root .md\:grid-cols-2 {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  #root .md\:grid-cols-3 {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }

  #root .md\:col-span-2 {
    grid-column: span 2;
  }
}

/* Base styles */
#root {
  font-family: Open Sans !important;
  font-size: 16px !important;
}

/* Estilos específicos para o scanner de QR code */
#qr-reader {
  position: relative;
}

#qr-reader video {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

#qr-reader canvas {
  display: none;
}

/* Estilos para o preview dos dados do QR code */
pre {
  background-color: #f8f8f8;
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #e1e1e1;
  white-space: pre-wrap;
  word-wrap: break-word;
}
</style>