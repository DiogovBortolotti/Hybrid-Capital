<template>
    <main>
        <section class="py-16 px-8 bg-gradient-to-b from-[#282641] to-[#615c8e] text-white">
            <div class="grid grid-cols-2 gap-12 items-center">
                <div>
                    <h2 class="text-4xl font-bold mb-6 leading-tight tracking-tight">
                        Gerencie suas finanças e investimentos em um só lugar
                    </h2>
                    <p class="text-lg mb-8 opacity-90 leading-relaxed">
                        Acompanhe seus gastos, investimentos em criptomoedas, ações, imóveis e muito mais
                        com gráficos detalhados e análises inteligentes.
                    </p>
                    <div class="flex space-x-4">
                        <button
                            class="bg-[#a79de9] hover:bg-[#8a7fd0] transition-all duration-300 py-3 px-8 rounded-md font-medium text-lg flex items-center shadow-lg hover:shadow-xl transform hover:-translate-y-1">
                            <span class="material-symbols-outlined mr-2">rocket_launch</span> Começar Agora
                        </button>
                        <button
                            class="border-2 border-[#a79de9] hover:bg-[#a79de9]/20 transition-all duration-300 py-3 px-8 rounded-md font-medium text-lg flex items-center shadow-lg hover:shadow-xl transform hover:-translate-y-1">
                            <span class="material-symbols-outlined mr-2">play_circle</span> Ver Demo
                        </button>
                    </div>
                </div>
                <div class="relative">
                    <div
                        class="bg-[#282641]/60 backdrop-blur-md p-8 rounded-lg shadow-2xl transform hover:scale-[1.01] transition-transform duration-300">
                        <div class="bg-[#615c8e]/90 rounded-md p-5 mb-6 shadow-inner">
                            <h3 class="text-xl font-bold mb-4 tracking-tight">Resumo Financeiro</h3>
                            <div class="flex justify-between mb-3">
                                <span class="font-medium">Saldo Total</span>
                                <span class="font-bold">R$ 142.567,00</span>
                            </div>
                            <div class="flex justify-between mb-3">
                                <span class="font-medium">Investimentos</span>
                                <span class="text-[#a79de9] font-bold">R$ 87.902,30</span>
                            </div>
                            <div class="flex justify-between">
                                <span class="font-medium">Despesas Mensais</span>
                                <span class="text-[#eed4ed] font-bold">R$ 5.432,10</span>
                            </div>
                        </div>
                        <div class="bg-[#615c8e]/90 rounded-md h-[200px] mb-6 p-5 shadow-inner">
                            <div class="flex justify-between mb-4">
                                <h3 class="text-xl font-bold tracking-tight">
                                    Distribuição de Investimentos
                                </h3>
                            </div>
                            <div class="flex justify-between h-[140px] items-end">
                                <div
                                    class="w-1/4 bg-[#a79de9] rounded-t-md self-end h-[30%] flex items-center justify-center hover:h-[35%] transition-all duration-300 px-1">
                                    <span class="text-xs font-bold">Cripto</span>
                                </div>
                                <div
                                    class="w-1/4 bg-[#615c8e] rounded-t-md self-end h-[60%] flex items-center justify-center hover:h-[65%] transition-all duration-300 px-1">
                                    <span class="text-xs font-bold">Ações</span>
                                </div>
                                <div
                                    class="w-1/4 bg-[#282641] rounded-t-md self-end h-[80%] flex items-center justify-center hover:h-[85%] transition-all duration-300 px-1">
                                    <span class="text-xs font-bold">Imóveis</span>
                                </div>
                                <div
                                    class="w-1/4 bg-[#eed4ed] text-[#120907] rounded-t-md self-end h-[40%] flex items-center justify-center hover:h-[45%] transition-all duration-300 px-1">
                                    <span class="text-xs font-bold">Poupança</span>
                                </div>
                            </div>
                        </div>
                        <div class="flex space-x-4">
                            <button
                                class="flex-1 bg-[#a79de9] hover:bg-[#8a7fd0] transition-all duration-300 py-3 rounded-md font-medium flex items-center justify-center shadow-md hover:shadow-lg">
                                <span class="material-symbols-outlined mr-1">add_circle</span> Novo
                                Lançamento
                            </button>
                            <button
                                class="flex-1 bg-[#615c8e] hover:bg-[#4e4a7a] transition-all duration-300 py-3 rounded-md font-medium flex items-center justify-center shadow-md hover:shadow-lg">
                                <span class="material-symbols-outlined mr-1">insights</span> Ver Relatórios
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <section class="py-20 px-8 bg-white">
            <h2 class="text-3xl font-bold text-[#282641] text-center mb-14 tracking-tight">
                Nossos Serviços
            </h2>
            <div class="grid grid-cols-4 gap-8">
                <div
                    class="bg-white p-7 rounded-lg shadow-md hover:shadow-xl transition-all duration-300 border-t-4 border-[#615c8e] group">
                    <div
                        class="bg-[#eed4ed]/30 p-3 rounded-full w-16 h-16 flex items-center justify-center mb-5 group-hover:bg-[#a79de9]/30 transition-colors duration-300">
                        <span class="material-symbols-outlined text-3xl text-[#615c8e]">savings</span>
                    </div>
                    <h3 class="text-xl font-bold text-[#282641] mb-3 tracking-tight">Gestão Financeira</h3>
                    <p class="text-[#615c8e] leading-relaxed">
                        Acompanhe seus gastos e crie orçamentos para controlar suas finanças pessoais.
                    </p>
                </div>
                <div
                    class="bg-white p-7 rounded-lg shadow-md hover:shadow-xl transition-all duration-300 border-t-4 border-[#615c8e] group">
                    <div
                        class="bg-[#eed4ed]/30 p-3 rounded-full w-16 h-16 flex items-center justify-center mb-5 group-hover:bg-[#a79de9]/30 transition-colors duration-300">
                        <span class="material-symbols-outlined text-3xl text-[#615c8e]">currency_bitcoin</span>
                    </div>
                    <h3 class="text-xl font-bold text-[#282641] mb-3 tracking-tight">
                        Cripto Investimentos
                    </h3>
                    <p class="text-[#615c8e] leading-relaxed">
                        Acompanhe e gerencie seus investimentos em criptomoedas em tempo real.
                    </p>
                </div>
                <div
                    class="bg-white p-7 rounded-lg shadow-md hover:shadow-xl transition-all duration-300 border-t-4 border-[#615c8e] group">
                    <div
                        class="bg-[#eed4ed]/30 p-3 rounded-full w-16 h-16 flex items-center justify-center mb-5 group-hover:bg-[#a79de9]/30 transition-colors duration-300">
                        <span class="material-symbols-outlined text-3xl text-[#615c8e]">monitoring</span>
                    </div>
                    <h3 class="text-xl font-bold text-[#282641] mb-3 tracking-tight">Bolsa de Valores</h3>
                    <p class="text-[#615c8e] leading-relaxed">
                        Gerencie sua carteira de ações e acompanhe dividendos e rendimentos.
                    </p>
                </div>
                <div
                    class="bg-white p-7 rounded-lg shadow-md hover:shadow-xl transition-all duration-300 border-t-4 border-[#615c8e] group">
                    <div
                        class="bg-[#eed4ed]/30 p-3 rounded-full w-16 h-16 flex items-center justify-center mb-5 group-hover:bg-[#a79de9]/30 transition-colors duration-300">
                        <span class="material-symbols-outlined text-3xl text-[#615c8e]">smart_toy</span>
                    </div>
                    <h3 class="text-xl font-bold text-[#282641] mb-3 tracking-tight">Trading Bot</h3>
                    <p class="text-[#615c8e] leading-relaxed">
                        Configure bots de negociação automatizada para maximizar seus investimentos.
                    </p>
                </div>
            </div>
        </section>
        <section class="py-20 px-8 bg-gray-50">
            <div class="max-w-3xl mx-auto text-center">
                <h2 class="text-3xl font-bold text-[#282641] mb-6 tracking-tight">
                    Por que escolher o Hybrid Capital?
                </h2>
                <p class="text-lg text-[#615c8e] mb-14 leading-relaxed">
                    Uma plataforma completa para gerenciar suas finanças e investimentos com facilidade,
                    segurança e análises detalhadas.
                </p>
                <div class="grid grid-cols-3 gap-10 mt-14">
                    <div class="flex flex-col items-center group">
                        <div
                            class="bg-[#a79de9] p-4 rounded-full w-20 h-20 flex items-center justify-center mb-5 shadow-md group-hover:shadow-lg transition-all duration-300 transform group-hover:-translate-y-1">
                            <span class="material-symbols-outlined text-4xl text-white">security</span>
                        </div>
                        <h3 class="text-xl font-bold text-[#282641] mb-3 tracking-tight">Segurança</h3>
                        <p class="text-[#615c8e] leading-relaxed">
                            Dados criptografados e proteção avançada para suas informações financeiras.
                        </p>
                    </div>
                    <div class="flex flex-col items-center group">
                        <div
                            class="bg-[#a79de9] p-4 rounded-full w-20 h-20 flex items-center justify-center mb-5 shadow-md group-hover:shadow-lg transition-all duration-300 transform group-hover:-translate-y-1">
                            <span class="material-symbols-outlined text-4xl text-white">analytics</span>
                        </div>
                        <h3 class="text-xl font-bold text-[#282641] mb-3 tracking-tight">Análises</h3>
                        <p class="text-[#615c8e] leading-relaxed">
                            Gráficos detalhados e relatórios personalizados para melhorar seus
                            investimentos.
                        </p>
                    </div>
                    <div class="flex flex-col items-center group">
                        <div
                            class="bg-[#a79de9] p-4 rounded-full w-20 h-20 flex items-center justify-center mb-5 shadow-md group-hover:shadow-lg transition-all duration-300 transform group-hover:-translate-y-1">
                            <span class="material-symbols-outlined text-4xl text-white">schedule</span>
                        </div>
                        <h3 class="text-xl font-bold text-[#282641] mb-3 tracking-tight">Tempo Real</h3>
                        <p class="text-[#615c8e] leading-relaxed">
                            Atualizações em tempo real sobre seus investimentos e movimentações financeiras.
                        </p>
                    </div>
                </div>
            </div>
        </section>
    </main>
</template>

<style scoped></style>

<script>
export default {
    name: "MainContent"
};
</script>