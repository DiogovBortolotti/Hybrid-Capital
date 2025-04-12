<template>
    <!-- Cabeçalho quando não está logado -->
    <header v-if="!isLoggedIn" class="header">
        <div class="header-container">
            <div class="logo-container">
                <svg class="icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M12 2L2 7L12 12L22 7L12 2Z" fill="currentColor"></path>
                    <path d="M2 17L12 22L22 17" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                        stroke-linejoin="round"></path>
                    <path d="M2 12L12 17L22 12" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                        stroke-linejoin="round"></path>
                </svg>
                <h1 class="title">Hybrid Capital</h1>
            </div>
            <div class="buttons-container">
                <button class="btn-home" @click="$router.push('/')">
                    Home
                </button>
                <button class="btn-painel" @click="$router.push('/painel')">
                    Painel
                </button>
            </div>
        </div>
    </header>

    <!-- Cabeçalho quando está logado -->
    <header v-else class="bg-[#282641] text-white p-4 md:p-6 shadow-lg z-50">
        <div class="header-container">
            <div class="logo-container">
                <svg class="icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M12 2L2 7L12 12L22 7L12 2Z" fill="currentColor"></path>
                    <path d="M2 17L12 22L22 17" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                        stroke-linejoin="round"></path>
                    <path d="M2 12L12 17L22 12" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                        stroke-linejoin="round"></path>
                </svg>
                <h1 class="title">Hybrid Capital</h1>
            </div>
            <div class="flex items-center space-x-6">
                <details class="relative group">
                    <summary
                        class="flex items-center space-x-1 cursor-pointer list-none focus:outline-none hover:text-[#a79de9] transition-colors duration-300 transform hover:scale-105">
                        <span class="material-symbols-outlined relative">
                            notifications
                            <!-- Indicador de notificação não lida -->
                            <span v-if="unreadNotifications > 0"
                                class="absolute -top-1 -right-1 w-2 h-2 bg-red-500 rounded-full"></span>
                        </span>
                        <span class="text-sm">Notificações</span>
                    </summary>
                    <div
                        class="absolute right-0 mt-2 w-72 bg-white rounded-md shadow-lg text-[#120907] z-50 max-h-96 overflow-y-auto">
                        <div class="py-1">
                            <!-- Quando há notificações -->
                            <template v-if="notifications.length > 0">
                                <div v-for="notification in notifications" :key="notification.id"
                                    class="block px-4 py-3 hover:bg-[#eed4ed] transition-colors border-b border-gray-100 last:border-b-0">
                                    <div class="flex items-start space-x-3">
                                        <span
                                            class="material-symbols-outlined text-[#615c8e] mt-0.5">notifications</span>
                                        <div>
                                            <p class="font-medium">{{ notification.title }}</p>
                                            <p class="text-sm text-gray-500">{{ notification.message }}</p>
                                            <p class="text-xs text-[#615c8e] mt-1">{{ formatDate(notification.date) }}
                                            </p>
                                        </div>
                                    </div>
                                </div>
                            </template>

                            <!-- Quando não há notificações -->
                            <div v-else class="px-4 py-6 text-center">
                                <span
                                    class="material-symbols-outlined text-[#a79de9] text-4xl mx-auto">notifications_off</span>
                                <p class="mt-2 text-[#615c8e]">Sem notificações</p>
                            </div>
                        </div>

                        <div v-if="notifications.length > 0"
                            class="bg-gray-50 px-4 py-2 text-center border-t border-gray-100">
                            <button @click="markAllAsRead" class="text-sm text-[#615c8e] hover:text-[#a79de9]">
                                Marcar todas como lidas
                            </button>
                        </div>
                    </div>
                </details>
                <details class="relative group">
                    <summary
                        class="flex items-center space-x-1 cursor-pointer list-none focus:outline-none hover:text-[#a79de9] transition-colors duration-300">
                        <span class="material-symbols-outlined">Robot</span>
                        <span class="text-sm">Bots</span>
                    </summary>
                    <div class="absolute right-0 mt-2 w-48 bg-white rounded-md shadow-lg text-[#120907] z-50">
                        <div class="py-1">
                            <a href="#"
                                class="block px-4 py-2 hover:bg-[#eed4ed] transition-colors flex items-center space-x-2">
                                <span class="material-symbols-outlined text-sm">home</span>
                                <span>Início</span>
                            </a>
                            <a href="#"
                                class="block px-4 py-2 hover:bg-[#eed4ed] transition-colors flex items-center space-x-2">
                                <span class="material-symbols-outlined text-sm">receipt</span>
                                <span>Transações</span>
                            </a>
                            <a href="#"
                                class="block px-4 py-2 hover:bg-[#eed4ed] transition-colors flex items-center space-x-2">
                                <span class="material-symbols-outlined text-sm">analytics</span>
                                <span>Relatórios</span>
                            </a>
                        </div>
                    </div>
                </details>
                <details class="relative group">
                    <summary
                        class="flex items-center space-x-1 cursor-pointer list-none focus:outline-none hover:text-[#a79de9] transition-colors duration-300">
                        <span class="material-symbols-outlined">Payments</span>
                        <span class="text-sm">Investimentos</span>
                    </summary>
                    <div class="absolute right-0 mt-2 w-48 bg-white rounded-md shadow-lg text-[#120907] z-50">
                        <div class="py-1">
                            <a href="#"
                                class="block px-4 py-2 hover:bg-[#eed4ed] transition-colors flex items-center space-x-2">
                                <span class="material-symbols-outlined text-sm">home</span>
                                <span>Início</span>
                            </a>
                            <a href="#"
                                class="block px-4 py-2 hover:bg-[#eed4ed] transition-colors flex items-center space-x-2">
                                <span class="material-symbols-outlined text-sm">receipt</span>
                                <span>Transações</span>
                            </a>
                            <a href="#"
                                class="block px-4 py-2 hover:bg-[#eed4ed] transition-colors flex items-center space-x-2">
                                <span class="material-symbols-outlined text-sm">analytics</span>
                                <span>Relatórios</span>
                            </a>
                        </div>
                    </div>
                </details>
                <details class="relative group">
                    <summary
                        class="flex items-center space-x-1 cursor-pointer list-none focus:outline-none hover:text-[#a79de9] transition-colors duration-300">
                        <span class="material-symbols-outlined">Finance</span>
                        <span class="text-sm">Financas</span>
                    </summary>
                    <div class="absolute right-0 mt-2 w-48 bg-white rounded-md shadow-lg text-[#120907] z-50">
                        <div class="py-1">
                            <a href="#"
                                class="block px-4 py-2 hover:bg-[#eed4ed] transition-colors flex items-center space-x-2">
                                <span class="material-symbols-outlined text-sm">home</span>
                                <span>Início</span>
                            </a>
                            <a href="#"
                                class="block px-4 py-2 hover:bg-[#eed4ed] transition-colors flex items-center space-x-2">
                                <span class="material-symbols-outlined text-sm">receipt</span>
                                <span>Transações</span>
                            </a>
                            <a href="#"
                                class="block px-4 py-2 hover:bg-[#eed4ed] transition-colors flex items-center space-x-2">
                                <span class="material-symbols-outlined text-sm">analytics</span>
                                <span>Relatórios</span>
                            </a>
                        </div>
                    </div>
                </details>
                <details class="relative group">
                    <summary class="flex items-center space-x-2 cursor-pointer list-none focus:outline-none">
                        <div
                            class="w-10 h-10 rounded-full bg-[#615c8e] overflow-hidden flex items-center justify-center hover:ring-2 hover:ring-[#a79de9] transition-all duration-300">
                            <span class="material-symbols-outlined">person</span>
                        </div>
                        <span class="group-hover:text-[#a79de9] transition-colors">Meu Perfil</span>
                    </summary>
                    <div class="absolute right-0 mt-2 w-48 bg-white rounded-md shadow-lg text-[#120907] z-[1000]">
                        <div class="py-1">
                            <a href="https://webcrumbs.cloud/placeholder"
                                class="block px-4 py-2 hover:bg-[#eed4ed] transition-colors flex items-center space-x-2">
                                <span class="material-symbols-outlined text-sm">person</span>
                                <span>Ver Perfil</span>
                            </a>
                            <a href="https://webcrumbs.cloud/placeholder"
                                class="block px-4 py-2 hover:bg-[#eed4ed] transition-colors flex items-center space-x-2">
                                <span class="material-symbols-outlined text-sm">settings</span>
                                <span>Preferências</span>
                            </a>
                            <button @click="logout"
                                class="block w-full px-4 py-2 hover:bg-[#eed4ed] transition-colors duration-200 flex items-center space-x-2 text-left">
                                <span class="material-symbols-outlined text-sm">logout</span>
                                <span>Logout</span>
                            </button>
                        </div>
                    </div>
                </details>
            </div>
        </div>
    </header>
</template>

<script>
export default {
    name: 'DynamicHeader',
    data() {
        return {
            isLoggedIn: false,
            apiUrl: process.env.VUE_APP_API_URL,
            notifications: [],
            unreadNotifications: 0,
            isLoadingNotifications: false
        };
    },
    async created() {
        await this.checkAuth();
        if (this.isLoggedIn) {
            await this.fetchNotifications();
        }
    },
    methods: {
        async checkAuth() {
            const token = localStorage.getItem('token');

            if (!token) {
                this.isLoggedIn = false;
                return;
            }

            try {
                const response = await fetch(`${this.apiUrl}/account/check_auth/`, {
                    method: 'GET',
                    headers: {
                        'Authorization': `Token ${token}`,
                    },
                });

                this.isLoggedIn = response.ok;
            } catch (error) {
                console.error('Erro ao verificar autenticação:', error);
                this.isLoggedIn = false;
            }
        },

        async fetchNotifications() {
            try {
                this.isLoadingNotifications = true;
                const token = localStorage.getItem('token');

                if (!token) {
                    this.notifications = [];
                    return;
                }

                const response = await fetch(`${this.apiUrl}/notifications/`, {
                    headers: {
                        'Authorization': `Token ${token}`
                    }
                });

                const data = await response.json();
                this.notifications = data || []; // Garante que seja array
                this.unreadNotifications = this.notifications.filter(n => !n.read).length;
            } catch (error) {
                console.error('Erro ao buscar notificações:', error);
                this.notifications = []; // Garante array vazio em caso de erro
            } finally {
                this.isLoadingNotifications = false;
            }
        },

        formatDate(dateString) {
            if (!dateString) return '';
            const options = {
                year: 'numeric',
                month: 'short',
                day: 'numeric',
                hour: '2-digit',
                minute: '2-digit'
            };
            return new Date(dateString).toLocaleDateString('pt-BR', options);
        },

        async markAllAsRead() {
            try {
                const token = localStorage.getItem('token');

                if (!token) return;

                await fetch(`${this.apiUrl}/notifications/mark-all-as-read/`, {
                    method: 'POST',
                    headers: {
                        'Authorization': `Token ${token}`
                    }
                });

                this.notifications = this.notifications.map(n => ({ ...n, read: true }));
                this.unreadNotifications = 0;
            } catch (error) {
                console.error('Erro ao marcar notificações como lidas:', error);
            }
        },

        logout() {
            localStorage.removeItem('token');
            this.isLoggedIn = false;
            this.notifications = [];
            this.$router.push('/painel');
        }
    }
};
</script>
<style scoped>
@import url(https://fonts.googleapis.com/css2?family=Open+Sans&display=swap);
@import url(https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200);

/* Estilos do cabeçalho */
header.bg-\[\#282641\] {
    background-color: #282641;
    color: white;
    padding: 1rem;
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.1);
    z-index: 50;
}

.absolute.right-0.mt-2 {
    position: absolute;
    right: 0;
    margin-top: 0.5rem;
    z-index: 1000;
}

.z-\[1000\] {
    z-index: 1000;
}

/* Container flex */
.flex {
    display: flex;
}

.justify-between {
    justify-content: space-between;
}

.items-center {
    align-items: center;
}

.items-center.space-x-2>svg {
    width: 2rem;
    height: 2rem;
    color: #a79de9;
}

.text-xl {
    font-size: 1.25rem;
    line-height: 1.75rem;
}

.font-bold {
    font-weight: 700;
}

.tracking-tight {
    letter-spacing: -0.025em;
}

/* Botões e itens de navegação */
.space-x-6>*+* {
    margin-left: 1.5rem;
}

button.flex.items-center.space-x-1 {
    display: flex;
    align-items: center;
    gap: 0.25rem;
}

.hover\:text-\[\#a79de9\]:hover {
    color: #a79de9;
}

.transition-colors {
    transition-property: color, background-color, border-color, text-decoration-color, fill, stroke;
    transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
    transition-duration: 150ms;
}

.transform {
    transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.hover\:scale-105:hover {
    --tw-scale-x: 1.05;
    --tw-scale-y: 1.05;
}

/* Dropdown do perfil */
details.relative {
    position: relative;
}

summary {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    cursor: pointer;
    list-style: none;
}

.w-10.h-10.rounded-full {
    width: 2.5rem;
    height: 2.5rem;
    border-radius: 9999px;
    background-color: #615c8e;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
}

.hover\:ring-2:hover {
    box-shadow: 0 0 0 2px #a79de9;
}

.transition-all {
    transition-property: all;
    transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
    transition-duration: 150ms;
}

/* Menu dropdown */
.absolute.right-0.mt-2 {
    position: absolute;
    right: 0;
    margin-top: 0.5rem;
}

.w-48 {
    width: 12rem;
}

.bg-white {
    background-color: white;
}

.rounded-md {
    border-radius: 0.375rem;
}

.shadow-lg {
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.1);
}

.text-\[\#120907\] {
    color: #120907;
}

.py-1>* {
    padding-top: 0.25rem;
    padding-bottom: 0.25rem;
}

.block.px-4.py-2 {
    display: block;
    padding-left: 1rem;
    padding-right: 1rem;
    padding-top: 0.5rem;
    padding-bottom: 0.5rem;
}

.hover\:bg-\[\#eed4ed\]:hover {
    background-color: #eed4ed;
}

.text-sm {
    font-size: 0.875rem;
    line-height: 1.25rem;
}

/* Responsividade */
@media (min-width: 768px) {
    .md\:p-6 {
        padding: 1.5rem;
    }

    .md\:text-2xl {
        font-size: 1.5rem;
        line-height: 2rem;
    }
}

/* Estilos específicos para o header */
.header {
    background-color: #282641;
    color: white;
    padding: 24px 32px;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.1);
}

.header-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo-container {
    display: flex;
    align-items: center;
    gap: 12px;
}

.icon {
    width: 32px;
    height: 32px;
    color: #a79de9;
}

.title {
    font-size: 24px;
    font-weight: 700;
    letter-spacing: -0.025em;
}

.buttons-container {
    display: flex;
    gap: 16px;
}

button {
    padding: 8px 24px;
    border-radius: 8px;
    font-weight: 500;
    box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
    transition: background-color 0.3s ease;
}

.btn-home {
    background-color: #615c8e;
}

.btn-home:hover {
    background-color: #4e4a7a;
}

.btn-painel {
    background-color: #a79de9;
}

.btn-painel:hover {
    background-color: #8a7fd0;
}
</style>
