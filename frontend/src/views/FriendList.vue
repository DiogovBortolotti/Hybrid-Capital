<template>
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <title>My Webcrumbs Plugin</title>
        </head>
        <body>
            <div id="webcrumbs">
                <div class="bg-[#282641] min-h-screen text-[#eed4ed] font-sans">
                    <header class="bg-[#120907] py-4 px-6 shadow-lg">
                        <div class="flex justify-between items-center">
                            <h1 class="text-2xl font-bold text-[#a79de9]">FinanceTracker</h1>
                            <nav class="hidden md:flex space-x-6">
                                <a href="#investments" class="hover:text-[#a79de9] transition-colors duration-200">
                                    Investimentos
                                </a>
                                <a href="#finances" class="hover:text-[#a79de9] transition-colors duration-200">
                                    Finanças
                                </a>
                                <a href="#dividends" class="hover:text-[#a79de9] transition-colors duration-200">
                                    Dividendos
                                </a>
                                <a href="#bots" class="hover:text-[#a79de9] transition-colors duration-200"> Bots </a>
                                <a
                                    href="#friends"
                                    class="hover:text-[#a79de9] transition-colors duration-200 border-b-2 border-[#a79de9]"
                                >
                                    Amigos
                                </a>
                            </nav>
                            <details class="md:hidden relative">
                                <summary class="list-none cursor-pointer">
                                    <span class="material-symbols-outlined text-2xl">menu</span>
                                </summary>
                                <div
                                    class="absolute right-0 mt-2 w-48 bg-[#282641] rounded-md shadow-lg z-10 border border-[#615c8e]"
                                >
                                    <nav class="flex flex-col py-2">
                                        <a
                                            href="#investments"
                                            class="px-4 py-2 hover:bg-[#615c8e] transition-colors duration-200"
                                        >
                                            Investimentos
                                        </a>
                                        <a
                                            href="#finances"
                                            class="px-4 py-2 hover:bg-[#615c8e] transition-colors duration-200"
                                        >
                                            Finanças
                                        </a>
                                        <a
                                            href="#dividends"
                                            class="px-4 py-2 hover:bg-[#615c8e] transition-colors duration-200"
                                        >
                                            Dividendos
                                        </a>
                                        <a href="#bots" class="px-4 py-2 hover:bg-[#615c8e] transition-colors duration-200">
                                            Bots
                                        </a>
                                        <a
                                            href="#friends"
                                            class="px-4 py-2 bg-[#615c8e] text-white transition-colors duration-200"
                                        >
                                            Amigos
                                        </a>
                                    </nav>
                                </div>
                            </details>
                        </div>
                    </header>
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
                                            <span class="material-symbols-outlined absolute left-3 top-2.5 text-[#615c8e]"
                                                >search</span
                                            >
                                        </div>
                                    </div>
                                    <div
                                        class="space-y-3 max-h-[calc(100vh-250px)] overflow-y-auto scrollbar-thin scrollbar-thumb-[#615c8e] pr-1"
                                    >
                                        <div
                                            class="flex justify-between items-center hover:bg-[#282641] p-2 rounded-md transition-colors duration-200 cursor-pointer bg-[#615c8e] border-l-4 border-[#a79de9]"
                                        >
                                            <div class="flex items-center">
                                                <div
                                                    class="w-10 h-10 rounded-full bg-[#a79de9] flex items-center justify-center text-white font-bold"
                                                >
                                                    JR
                                                </div>
                                                <div class="ml-3">
                                                    <p class="font-semibold">João Ribeiro</p>
                                                    <div class="flex items-center">
                                                        <span class="w-2 h-2 bg-green-500 rounded-full"></span>
                                                        <p class="text-xs text-[#a79de9] ml-1.5">Online</p>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div
                                            class="flex justify-between items-center hover:bg-[#282641] p-2 rounded-md transition-colors duration-200 cursor-pointer"
                                        >
                                            <div class="flex items-center">
                                                <div
                                                    class="w-10 h-10 rounded-full bg-[#615c8e] flex items-center justify-center text-white font-bold"
                                                >
                                                    MC
                                                </div>
                                                <div class="ml-3">
                                                    <p class="font-semibold">Mariana Costa</p>
                                                    <div class="flex items-center">
                                                        <span class="w-2 h-2 bg-gray-400 rounded-full"></span>
                                                        <p class="text-xs text-[#a79de9] ml-1.5">Offline • 2h atrás</p>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div
                                            class="flex justify-between items-center hover:bg-[#282641] p-2 rounded-md transition-colors duration-200 cursor-pointer"
                                        >
                                            <div class="flex items-center">
                                                <div
                                                    class="w-10 h-10 rounded-full bg-[#615c8e] flex items-center justify-center text-white font-bold"
                                                >
                                                    LS
                                                </div>
                                                <div class="ml-3">
                                                    <p class="font-semibold">Lucas Santos</p>
                                                    <div class="flex items-center">
                                                        <span class="w-2 h-2 bg-green-500 rounded-full"></span>
                                                        <p class="text-xs text-[#a79de9] ml-1.5">Online</p>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div
                                            class="flex justify-between items-center hover:bg-[#282641] p-2 rounded-md transition-colors duration-200 cursor-pointer"
                                        >
                                            <div class="flex items-center">
                                                <div
                                                    class="w-10 h-10 rounded-full bg-[#615c8e] flex items-center justify-center text-white font-bold"
                                                >
                                                    GN
                                                </div>
                                                <div class="ml-3">
                                                    <p class="font-semibold">Gabriela Nogueira</p>
                                                    <div class="flex items-center">
                                                        <span class="w-2 h-2 bg-gray-400 rounded-full"></span>
                                                        <p class="text-xs text-[#a79de9] ml-1.5">Offline • 1d atrás</p>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div
                                            class="flex justify-between items-center hover:bg-[#282641] p-2 rounded-md transition-colors duration-200 cursor-pointer"
                                        >
                                            <div class="flex items-center">
                                                <div
                                                    class="w-10 h-10 rounded-full bg-[#615c8e] flex items-center justify-center text-white font-bold"
                                                >
                                                    AP
                                                </div>
                                                <div class="ml-3">
                                                    <p class="font-semibold">Amanda Pereira</p>
                                                    <div class="flex items-center">
                                                        <span class="w-2 h-2 bg-green-500 rounded-full"></span>
                                                        <p class="text-xs text-[#a79de9] ml-1.5">Online</p>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div
                                            class="flex justify-between items-center hover:bg-[#282641] p-2 rounded-md transition-colors duration-200 cursor-pointer"
                                        >
                                            <div class="flex items-center">
                                                <div
                                                    class="w-10 h-10 rounded-full bg-[#615c8e] flex items-center justify-center text-white font-bold"
                                                >
                                                    RF
                                                </div>
                                                <div class="ml-3">
                                                    <p class="font-semibold">Rafael Ferreira</p>
                                                    <div class="flex items-center">
                                                        <span class="w-2 h-2 bg-gray-400 rounded-full"></span>
                                                        <p class="text-xs text-[#a79de9] ml-1.5">Offline • 3d atrás</p>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <button
                                        id="addFriendBtn"
                                        class="w-full mt-4 bg-[#615c8e] hover:bg-[#a79de9] text-white font-semibold py-2 px-4 rounded-md transition-colors duration-300 flex items-center justify-center"
                                    >
                                        <span class="material-symbols-outlined mr-2">group_add</span> Adicionar Amigos
                                    </button>
                                </div>
                                <div class="w-full md:w-3/4 lg:w-4/5 p-6 bg-[#282641]">
                                    <div class="flex items-center mb-6">
                                        <div
                                            class="w-12 h-12 rounded-full bg-[#a79de9] flex items-center justify-center text-white text-xl font-bold mr-4"
                                        >
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
                                                <summary
                                                    class="list-none cursor-pointer bg-[#615c8e] hover:bg-[#a79de9] text-white p-2 rounded-md transition-colors duration-300"
                                                >
                                                    <span class="material-symbols-outlined">more_vert</span>
                                                </summary>
                                                <div
                                                    class="absolute right-0 mt-2 w-48 bg-[#1e1d32] border border-[#615c8e] rounded-md shadow-lg z-10"
                                                >
                                                    <div class="py-1">
                                                        <a
                                                            href="#"
                                                            class="flex items-center px-4 py-2 hover:bg-[#615c8e] transition-colors duration-200"
                                                        >
                                                            <span class="material-symbols-outlined mr-2">person_off</span>
                                                            Bloquear Amigo
                                                        </a>
                                                        <a
                                                            href="#"
                                                            class="flex items-center px-4 py-2 hover:bg-[#615c8e] transition-colors duration-200"
                                                        >
                                                            <span class="material-symbols-outlined mr-2"
                                                                >person_remove</span
                                                            >
                                                            Remover Amigo
                                                        </a>
                                                        <a
                                                            href="#"
                                                            class="flex items-center px-4 py-2 hover:bg-red-700 text-red-400 transition-colors duration-200"
                                                        >
                                                            <span class="material-symbols-outlined mr-2">report</span>
                                                            Denunciar
                                                        </a>
                                                    </div>
                                                </div>
                                            </details>
                                        </div>
                                    </div>
                                    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                                        <div
                                            class="bg-[#1e1d32] rounded-lg shadow-md hover:shadow-xl transition-all duration-300 p-5 transform hover:-translate-y-1"
                                        >
                                            <div class="flex justify-between items-center mb-4">
                                                <h3 class="text-lg font-semibold text-[#a79de9]">Informações Pessoais</h3>
                                                <span class="material-symbols-outlined text-[#615c8e]">person</span>
                                            </div>
                                            <ul class="space-y-3">
                                                <li class="flex items-start">
                                                    <span class="material-symbols-outlined text-[#615c8e] mr-2 mt-0.5"
                                                        >mail</span
                                                    >
                                                    <div>
                                                        <p class="text-sm text-[#a79de9]">Email</p>
                                                        <p>joao.ribeiro@email.com</p>
                                                    </div>
                                                </li>
                                                <li class="flex items-start">
                                                    <span class="material-symbols-outlined text-[#615c8e] mr-2 mt-0.5"
                                                        >today</span
                                                    >
                                                    <div>
                                                        <p class="text-sm text-[#a79de9]">Membro desde</p>
                                                        <p>01/01/2023</p>
                                                    </div>
                                                </li>
                                                <li class="flex items-start">
                                                    <span class="material-symbols-outlined text-[#615c8e] mr-2 mt-0.5"
                                                        >today</span
                                                    >
                                                    <div>
                                                        <p class="text-sm text-[#a79de9]">Ultimo Acesso</p>
                                                        <p>01/01/2024</p>
                                                    </div>
                                                </li>
                                            </ul>
                                        </div>
                                        <div
                                            class="bg-[#1e1d32] rounded-lg shadow-md hover:shadow-xl transition-all duration-300 p-5 transform hover:-translate-y-1"
                                        >
                                            <div class="flex justify-between items-center mb-4">
                                                <h3 class="text-lg font-semibold text-[#a79de9]">
                                                    Preferências de Investimento
                                                </h3>
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
                                                            <div
                                                                class="bg-[#a79de9] h-2 rounded-full"
                                                                style="width: 65%"
                                                            ></div>
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
                                                            <div
                                                                class="bg-[#a79de9] h-2 rounded-full"
                                                                style="width: 25%"
                                                            ></div>
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
                                                            <div
                                                                class="bg-[#a79de9] h-2 rounded-full"
                                                                style="width: 10%"
                                                            ></div>
                                                        </div>
                                                    </div>
                                                </li>
                                            </ul>
                                        </div>
                                        <div
                                            class="bg-[#1e1d32] rounded-lg shadow-md hover:shadow-xl transition-all duration-300 p-5 transform hover:-translate-y-1"
                                        >
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
                                                    <div
                                                        class="bg-gradient-to-r from-[#615c8e] to-[#a79de9] h-2 rounded-full w-full"
                                                    ></div>
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
                                                <div
                                                    class="flex items-center justify-between p-2 hover:bg-[#282641] rounded-md transition-colors duration-200"
                                                >
                                                    <div class="flex items-center">
                                                        <div
                                                            class="w-8 h-8 rounded bg-blue-600 flex items-center justify-center text-white font-bold text-xs mr-3"
                                                        >
                                                            VALE3
                                                        </div>
                                                        <span>Vale S.A.</span>
                                                    </div>
                                                    <div class="text-right">
                                                        <p class="font-semibold">R$ 14.823,45</p>
                                                        <p class="text-green-400 text-sm">+2.3%</p>
                                                    </div>
                                                </div>
                                                <div
                                                    class="flex items-center justify-between p-2 hover:bg-[#282641] rounded-md transition-colors duration-200"
                                                >
                                                    <div class="flex items-center">
                                                        <div
                                                            class="w-8 h-8 rounded bg-red-600 flex items-center justify-center text-white font-bold text-xs mr-3"
                                                        >
                                                            PETR4
                                                        </div>
                                                        <span>Petrobras</span>
                                                    </div>
                                                    <div class="text-right">
                                                        <p class="font-semibold">R$ 11.547,32</p>
                                                        <p class="text-red-400 text-sm">-0.8%</p>
                                                    </div>
                                                </div>
                                                <div
                                                    class="flex items-center justify-between p-2 hover:bg-[#282641] rounded-md transition-colors duration-200"
                                                >
                                                    <div class="flex items-center">
                                                        <div
                                                            class="w-8 h-8 rounded bg-green-600 flex items-center justify-center text-white font-bold text-xs mr-3"
                                                        >
                                                            WEGE3
                                                        </div>
                                                        <span>WEG S.A.</span>
                                                    </div>
                                                    <div class="text-right">
                                                        <p class="font-semibold">R$ 9.876,21</p>
                                                        <p class="text-green-400 text-sm">+1.5%</p>
                                                    </div>
                                                </div>
                                                <div
                                                    class="flex items-center justify-between p-2 hover:bg-[#282641] rounded-md transition-colors duration-200"
                                                >
                                                    <div class="flex items-center">
                                                        <div
                                                            class="w-8 h-8 rounded bg-purple-600 flex items-center justify-center text-white font-bold text-xs mr-3"
                                                        >
                                                            ITUB4
                                                        </div>
                                                        <span>Itaú Unibanco</span>
                                                    </div>
                                                    <div class="text-right">
                                                        <p class="font-semibold">R$ 8.543,62</p>
                                                        <p class="text-green-400 text-sm">+0.7%</p>
                                                    </div>
                                                </div>
                                                <div
                                                    class="flex items-center justify-between p-2 hover:bg-[#282641] rounded-md transition-colors duration-200"
                                                >
                                                    <div class="flex items-center">
                                                        <div
                                                            class="w-8 h-8 rounded bg-yellow-600 flex items-center justify-center text-white font-bold text-xs mr-3"
                                                        >
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
    
                <!-- Modal para convidar por e-mail -->
                <div id="inviteByEmailModal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 hidden backdrop-blur-sm">
                    <div class="bg-[#1e1d32] rounded-lg shadow-xl w-full max-w-md border border-[#615c8e]">
                        <div class="p-6">
                            <div class="flex justify-between items-center mb-4">
                                <h3 class="text-xl font-bold text-[#a79de9]">Convidar por E-mail</h3>
                                <button id="closeInviteModal" class="text-[#a79de9] hover:text-white">
                                    <span class="material-symbols-outlined">close</span>
                                </button>
                            </div>
                            <div class="mb-4">
                                <label class="block text-[#a79de9] mb-2">E-mail do amigo:</label>
                                <div class="relative">
                                    <input
                                        id="emailInput"
                                        type="email"
                                        class="w-full bg-[#282641] border border-[#615c8e] rounded-md p-2 pl-10 focus:outline-none focus:ring-2 focus:ring-[#a79de9] transition-all duration-300"
                                        placeholder="exemplo@email.com"
                                    />
                                    <span class="material-symbols-outlined absolute left-3 top-2.5 text-[#615c8e]">mail</span>
                                </div>
                            </div>
                            <div class="flex space-x-3">
                                <button
                                    id="cancelInvite"
                                    class="flex-1 bg-[#282641] hover:bg-[#615c8e] text-[#a79de9] font-semibold py-2 px-4 rounded-md transition-colors duration-300 flex items-center justify-center"
                                >
                                    <span class="material-symbols-outlined mr-2">close</span> Cancelar
                                </button>
                                <button
                                    id="sendInvite"
                                    class="flex-1 bg-[#615c8e] hover:bg-[#a79de9] text-white font-semibold py-2 px-4 rounded-md transition-colors duration-300 flex items-center justify-center disabled:opacity-50"
                                    disabled
                                >
                                    <span class="material-symbols-outlined mr-2">send</span> Enviar
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
    
                <!-- Modal para adicionar amigos (busca) -->
                <div id="addFriendModal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 hidden">
                    <div class="bg-[#1e1d32] rounded-lg shadow-xl w-full max-w-md border border-[#615c8e]">
                        <div class="p-6">
                            <div class="flex justify-between items-center mb-4">
                                <h3 class="text-xl font-bold text-[#a79de9]">Adicionar Amigo</h3>
                                <button id="closeModal" class="text-[#a79de9] hover:text-white">
                                    <span class="material-symbols-outlined">close</span>
                                </button>
                            </div>
                            <div class="mb-4">
                                <label class="block text-[#a79de9] mb-2">Buscar por:</label>
                                <div class="flex space-x-2 mb-4">
                                    <button id="searchByName" class="px-4 py-2 bg-[#615c8e] text-white rounded-md transition-colors duration-300">Nome</button>
                                    <button id="searchByEmail" class="px-4 py-2 bg-[#282641] text-[#a79de9] rounded-md transition-colors duration-300">E-mail</button>
                                </div>
                                <div class="relative">
                                    <input
                                        id="friendSearchInput"
                                        type="text"
                                        class="w-full bg-[#282641] border border-[#615c8e] rounded-md p-2 pl-10 focus:outline-none focus:ring-2 focus:ring-[#a79de9] transition-all duration-300"
                                        placeholder="Digite o nome completo"
                                    />
                                    <span class="material-symbols-outlined absolute left-3 top-2.5 text-[#615c8e]">search</span>
                                </div>
                            </div>
                            <div class="max-h-64 overflow-y-auto mb-4 scrollbar-thin scrollbar-thumb-[#615c8e]">
                                <div id="searchResults" class="space-y-2">
                                    <!-- Resultados aparecerão aqui -->
                                    <div class="text-center py-4 text-[#a79de9]">
                                        Digite para buscar amigos
                                    </div>
                                </div>
                            </div>
                            <button
                                id="sendFriendRequest"
                                class="w-full bg-[#615c8e] hover:bg-[#a79de9] text-white font-semibold py-2 px-4 rounded-md transition-colors duration-300 flex items-center justify-center disabled:opacity-50"
                                disabled
                            >
                                <span class="material-symbols-outlined mr-2">person_add</span> Enviar Solicitação
                            </button>
                        </div>
                    </div>
                </div>
            </div>
    
        </body>
    </html>
    </template>
    <script>
    import axios from 'axios';
    
    export default {
        mounted() {
            // Elementos do modal de convite por e-mail
            const inviteByEmailModal = document.getElementById('inviteByEmailModal');
            const closeInviteModal = document.getElementById('closeInviteModal');
            const cancelInvite = document.getElementById('cancelInvite');
            const sendInvite = document.getElementById('sendInvite');
            const emailInput = document.getElementById('emailInput');
            
            // Elementos do modal de busca por amigos
            const addFriendBtn = document.getElementById('addFriendBtn');
            const addFriendModal = document.getElementById('addFriendModal');
            const closeModal = document.getElementById('closeModal');
            const searchByNameBtn = document.getElementById('searchByName');
            const searchByEmailBtn = document.getElementById('searchByEmail');
            const friendSearchInput = document.getElementById('friendSearchInput');
            const searchResults = document.getElementById('searchResults');
            const sendFriendRequestBtn = document.getElementById('sendFriendRequest');
            
            let currentSearchType = 'name';
            let selectedFriend = null;
            
            // Abrir modal de convite por e-mail
            addFriendBtn.addEventListener('click', function() {
                inviteByEmailModal.classList.remove('hidden');
            });
            
            // Fechar modal de convite por e-mail
            closeInviteModal.addEventListener('click', function() {
                inviteByEmailModal.classList.add('hidden');
                emailInput.value = '';
                sendInvite.disabled = true;
            });
            
            cancelInvite.addEventListener('click', function() {
                inviteByEmailModal.classList.add('hidden');
                emailInput.value = '';
                sendInvite.disabled = true;
            });
            
            // Validar e-mail enquanto digita
            emailInput.addEventListener('input', function() {
                const email = this.value.trim();
                const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                
                if (emailRegex.test(email)) {
                    sendInvite.disabled = false;
                } else {
                    sendInvite.disabled = true;
                }
            });
            
            sendInvite.addEventListener('click', async function() {
    const email = emailInput.value.trim();
    
    try {
        // Estado de loading
        sendInvite.innerHTML = '<span class="material-symbols-outlined animate-spin mr-2">refresh</span> Enviando...';
        sendInvite.disabled = true;

        // DEBUG: Verificar token
        const token = localStorage.getItem('token') || localStorage.getItem('authToken');
        console.log('Token sendo usado:', token ? '****' + token.slice(-4) : 'Nenhum token encontrado');
        
        if (!token) {
            throw new Error('Autenticação necessária');
        }

        // DEBUG: Verificar URL
        const apiUrl = 'http://localhost:8000/account/invitations/send/';
        console.log('Endpoint:', apiUrl);

        // DEBUG: Verificar dados
        const requestData = { recipient_email: email };
        console.log('Dados enviados:', JSON.stringify(requestData));

        const response = await axios.post(apiUrl, requestData, {
            headers: {
                'Authorization': `Token ${token}`,
                'Content-Type': 'application/json'
            }
        });

        // Sucesso
        console.log('Resposta completa:', response.data);
        alert('Convite enviado para ' + email);
        inviteByEmailModal.classList.add('hidden');
        emailInput.value = '';

    } catch (error) {
        // DEBUG COMPLETO
        console.group('Erro detalhado');
        console.log('Mensagem:', error.message);
        console.log('Status:', error.response?.status);
        console.log('Dados da resposta:', error.response?.data);
        console.log('Headers:', error.response?.headers);
        console.log('Config:', error.config);
        console.groupEnd();

        // Tratamento específico para seu serializer
        let errorMsg = 'Erro ao enviar convite';
        
        if (error.response?.data?.recipient_email) {
            errorMsg = error.response.data.recipient_email[0];
        } 
        else if (error.response?.status === 400) {
            errorMsg = 'Verifique o e-mail digitado';
        }
        else if (error.response?.status === 401) {
            errorMsg = 'Faça login novamente';
            window.location.href = '/login';
        }

        alert(errorMsg);

    } finally {
        sendInvite.innerHTML = '<span class="material-symbols-outlined mr-2">send</span> Enviar';
        sendInvite.disabled = false;
    }
});
            
            // Abrir modal de busca por amigos (alternativo)
            addFriendBtn.addEventListener('contextmenu', function(e) {
                e.preventDefault();
                addFriendModal.classList.remove('hidden');
            });
            
            // Fechar modal de busca por amigos
            closeModal.addEventListener('click', function() {
                addFriendModal.classList.add('hidden');
                resetSearch();
            });
            
            // Selecionar tipo de busca
            searchByNameBtn.addEventListener('click', function() {
                currentSearchType = 'name';
                searchByNameBtn.classList.add('bg-[#615c8e]', 'text-white');
                searchByNameBtn.classList.remove('bg-[#282641]', 'text-[#a79de9]');
                searchByEmailBtn.classList.add('bg-[#282641]', 'text-[#a79de9]');
                searchByEmailBtn.classList.remove('bg-[#615c8e]', 'text-white');
                friendSearchInput.placeholder = "Digite o nome completo";
                resetSearch();
            });
            
            searchByEmailBtn.addEventListener('click', function() {
                currentSearchType = 'email';
                searchByEmailBtn.classList.add('bg-[#615c8e]', 'text-white');
                searchByEmailBtn.classList.remove('bg-[#282641]', 'text-[#a79de9]');
                searchByNameBtn.classList.add('bg-[#282641]', 'text-[#a79de9]');
                searchByNameBtn.classList.remove('bg-[#615c8e]', 'text-white');
                friendSearchInput.placeholder = "Digite o e-mail";
                resetSearch();
            });
            
            // Buscar amigos (agora com Axios)
            friendSearchInput.addEventListener('input', async function() {
                const searchTerm = this.value.trim();
                
                if (searchTerm.length < 3) {
                    searchResults.innerHTML = '<div class="text-center py-4 text-[#a79de9]">Digite pelo menos 3 caracteres</div>';
                    sendFriendRequestBtn.disabled = true;
                    selectedFriend = null;
                    return;
                }
                
                try {
                    const token = localStorage.getItem('authToken');
                    const response = await axios.post(`${window.apiUrl}/api/friends/search/`, {
                        type: currentSearchType,
                        query: searchTerm
                    }, {
                        headers: {
                            'Authorization': `Bearer ${token}`
                        }
                    });
                    
                    displaySearchResults(response.data);
                } catch (error) {
                    console.error('Erro na busca:', error);
                    searchResults.innerHTML = '<div class="text-center py-4 text-[#a79de9]">Erro na busca</div>';
                }
            });
            
            // Função para mostrar resultados da busca
            function displaySearchResults(users) {
                if (users.length === 0) {
                    searchResults.innerHTML = '<div class="text-center py-4 text-[#a79de9]">Nenhum resultado encontrado</div>';
                    sendFriendRequestBtn.disabled = true;
                    selectedFriend = null;
                    return;
                }
                
                let resultsHTML = '';
                users.forEach(user => {
                    resultsHTML += `
                        <div class="flex items-center p-3 hover:bg-[#282641] rounded-md cursor-pointer friend-result" data-id="${user.id}">
                            <div class="w-10 h-10 rounded-full bg-[#615c8e] flex items-center justify-center text-white font-bold mr-3">
                                ${user.avatar || user.name.substring(0, 2)}
                            </div>
                            <div>
                                <p class="font-semibold">${user.name}</p>
                                <p class="text-sm text-[#a79de9]">${user.email}</p>
                            </div>
                        </div>
                    `;
                });
                
                searchResults.innerHTML = resultsHTML;
                
                // Adicionar evento de clique nos resultados
                document.querySelectorAll('.friend-result').forEach(item => {
                    item.addEventListener('click', function() {
                        document.querySelectorAll('.friend-result').forEach(el => {
                            el.classList.remove('bg-[#615c8e]', 'border-l-4', 'border-[#a79de9]');
                        });
                        
                        this.classList.add('bg-[#615c8e]', 'border-l-4', 'border-[#a79de9]');
                        sendFriendRequestBtn.disabled = false;
                        selectedFriend = users.find(u => u.id == this.dataset.id);
                    });
                });
            }
            
            // Enviar solicitação de amizade (agora com Axios)
            sendFriendRequestBtn.addEventListener('click', async function() {
                if (!selectedFriend) return;
                
                try {
                    const token = localStorage.getItem('token');
                    await axios.post(`${window.apiUrl}/account/invitations/send/`, {
                        friend_id: selectedFriend.id
                    }, {
                        headers: {
                            'Authorization': `Bearer ${token}`,
                            'Content-Type': 'application/json'
                        }
                    });
                    
                    alert(`Solicitação enviada para ${selectedFriend.name}!`);
                    resetSearch();
                    addFriendModal.classList.add('hidden');
                } catch (error) {
                    console.error('Erro ao enviar solicitação:', error);
                    alert('Erro: ' + (error.response?.data?.message || error.message));
                }
            });
            
            // Resetar busca
            function resetSearch() {
                friendSearchInput.value = '';
                searchResults.innerHTML = '<div class="text-center py-4 text-[#a79de9]">Digite para buscar amigos</div>';
                sendFriendRequestBtn.disabled = true;
                selectedFriend = null;
            }
         // Certifique-se que a URL da API está disponível
        window.apiUrl = process.env.VUE_APP_API_URL;
        }
    };
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