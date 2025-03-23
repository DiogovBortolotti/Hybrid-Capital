<template>
    <div id="painel" class="min-h-screen flex flex-col">
        <!-- Efeito de Fundo Animado -->
        <ul class="background">
            <li v-for="i in 30" :key="i"></li>
        </ul>
        <Header />

        <main class="flex-grow flex items-center justify-center p-4">
            <div
                class="w-[400px] flex flex-col rounded-xl shadow-xl bg-[#282641] overflow-hidden border border-[#615c8e]">
                <div class="p-8 text-center">
                    <h1 class="text-3xl font-bold mb-2 text-[#eed4ed]">Painel</h1>
                    <p class="text-[#a79de9] text-sm mb-4">Junte-se a nós hoje ou entre na sua conta existente</p>

                    <!-- Botões de Alternância (Logar/Registrar) -->
                    <div class="flex justify-center mb-6">
                        <div class="flex p-1 bg-[#615c8e] rounded-lg">
                            <button class="py-2 px-6 rounded-md transition-all duration-300"
                                :class="{ 'active-form': isLogin, 'disable-form': !isLogin }" @click="toggleLogin">
                                Logar
                            </button>
                            <button class="py-2 px-6 rounded-md transition-all duration-300"
                                :class="{ 'active-form': !isLogin, 'disable-form': isLogin }" @click="toggleRegister">
                                Registrar
                            </button>
                        </div>
                    </div>

                    <!-- Formulário de Login -->
                    <form v-if="isLogin" class="space-y-4" @submit.prevent="handleLogin">
                        <div class="relative">
                            <input v-model="loginForm.email" type="email" placeholder="Email"
                                class="w-full bg-[#3a375c] border border-[#615c8e] rounded-lg py-3 px-4 text-[#eed4ed] placeholder:text-[#a79de9]/70 focus:outline-none focus:ring-2 focus:ring-[#a79de9] transition-all duration-300" />
                            <span class="material-symbols-outlined absolute right-3 top-3 text-[#a79de9]">mail</span>
                        </div>

                        <div class="relative">
                            <input v-model="loginForm.password" :type="showPassword ? 'text' : 'password'"
                                placeholder="Senha"
                                class="w-full bg-[#3a375c] border border-[#615c8e] rounded-lg py-3 px-4 text-[#eed4ed] placeholder:text-[#a79de9]/70 focus:outline-none focus:ring-2 focus:ring-[#a79de9] transition-all duration-300" />
                            <span
                                class="material-symbols-outlined absolute right-3 top-3 text-[#a79de9] cursor-pointer hover:text-[#eed4ed] transition-colors"
                                @click="togglePasswordVisibility">
                                {{ showPassword ? 'visibility_off' : 'visibility' }}
                            </span>
                        </div>

                        <button type="submit"
                            class="w-full bg-gradient-to-r from-[#615c8e] to-[#a79de9] text-white py-3 rounded-lg font-medium hover:shadow-lg hover:shadow-[#a79de9]/20 transition-all duration-300 transform hover:-translate-y-1">
                            Entrar
                        </button>
                    </form>

                    <!-- Formulário de Registro -->
                    <form v-else class="space-y-4" @submit.prevent="handleRegister">
                        <div class="relative">
                            <input v-model="registerForm.full_name" type="text" placeholder="Nome Completo"
                                class="w-full bg-[#3a375c] border border-[#615c8e] rounded-lg py-3 px-4 text-[#eed4ed] placeholder:text-[#a79de9]/70 focus:outline-none focus:ring-2 focus:ring-[#a79de9] transition-all duration-300" />
                            <span class="material-symbols-outlined absolute right-3 top-3 text-[#a79de9]">person</span>
                        </div>

                        <div class="relative">
                            <input v-model="registerForm.email" type="email" placeholder="Email"
                                class="w-full bg-[#3a375c] border border-[#615c8e] rounded-lg py-3 px-4 text-[#eed4ed] placeholder:text-[#a79de9]/70 focus:outline-none focus:ring-2 focus:ring-[#a79de9] transition-all duration-300" />
                            <span class="material-symbols-outlined absolute right-3 top-3 text-[#a79de9]">mail</span>
                        </div>

                        <div class="relative">
                            <input v-model="registerForm.password" :type="showRegisterPassword ? 'text' : 'password'"
                                placeholder="Senha"
                                class="w-full bg-[#3a375c] border border-[#615c8e] rounded-lg py-3 px-4 text-[#eed4ed] placeholder:text-[#a79de9]/70 focus:outline-none focus:ring-2 focus:ring-[#a79de9] transition-all duration-300" />
                            <span
                                class="material-symbols-outlined absolute right-3 top-3 text-[#a79de9] cursor-pointer hover:text-[#eed4ed] transition-colors"
                                @click="toggleRegisterPasswordVisibility">
                                {{ showRegisterPassword ? 'visibility_off' : 'visibility' }}
                            </span>
                        </div>

                        <div class="relative">
                            <input v-model="registerForm.confirm_password"
                                :type="showConfirmPassword ? 'text' : 'password'" placeholder="Confirmar Senha"
                                class="w-full bg-[#3a375c] border border-[#615c8e] rounded-lg py-3 px-4 text-[#eed4ed] placeholder:text-[#a79de9]/70 focus:outline-none focus:ring-2 focus:ring-[#a79de9] transition-all duration-300" />
                            <span
                                class="material-symbols-outlined absolute right-3 top-3 text-[#a79de9] cursor-pointer hover:text-[#eed4ed] transition-colors"
                                @click="toggleConfirmPasswordVisibility">
                                {{ showConfirmPassword ? 'visibility_off' : 'visibility' }}
                            </span>
                        </div>

                        <div class="flex items-center space-x-2 cursor-pointer group">
                            <div class="relative w-4 h-4">
                                <label class="cursor-pointer">
                                    <input type="checkbox" v-model="termsAccepted"
                                        class="peer opacity-0 w-4 h-4 absolute" />
                                    <div
                                        class="w-4 h-4 border border-[#a79de9] rounded-sm peer-checked:bg-[#a79de9] peer-checked:border-0 transition-all">
                                    </div>
                                    <span
                                        class="material-symbols-outlined absolute top-0 left-0 scale-0 peer-checked:scale-100 text-[12px] text-[#282641] transition-transform duration-200"></span>
                                </label>
                            </div>
                            <router-link to="/termos-e-condicoes" target="_blank"
                                class="text-sm text-[#a79de9] group-hover:text-[#eed4ed] transition-colors">
                                Eu concordo com os Termos e Condições
                            </router-link>

                        </div>

                        <button type="submit"
                            class="w-full bg-gradient-to-r from-[#615c8e] to-[#a79de9] text-white py-3 rounded-lg font-medium hover:shadow-lg hover:shadow-[#a79de9]/20 transition-all duration-300 transform hover:-translate-y-1">
                            Criar Conta
                        </button>
                    </form>
                </div>
            </div>
        </main>

        <Footer />
    </div>
</template>

<script>
import axios from 'axios';
import Header from '../components/Header.vue';
import Footer from '../components/Footer.vue';

export default {
    components: {
        Header,
        Footer,
    },
    data() {
        return {
            isLogin: true,
            showPassword: false,
            showRegisterPassword: false,
            showConfirmPassword: false,
            termsAccepted: false,
            loginForm: {
                email: '',
                password: '',
            },
            registerForm: {
                full_name: '',
                email: '',
                password: '',
                confirm_password: '',
            },
        };
    },
    methods: {
        toggleLogin() {
            this.isLogin = true;
        },
        toggleRegister() {
            this.isLogin = false;
        },
        togglePasswordVisibility() {
            this.showPassword = !this.showPassword;
        },
        toggleRegisterPasswordVisibility() {
            this.showRegisterPassword = !this.showRegisterPassword;
        },
        toggleConfirmPasswordVisibility() {
            this.showConfirmPassword = !this.showConfirmPassword;
        },
        async handleLogin() {
            try {
                const response = await axios.post('http://localhost:8000/account/login/', {
                    email: this.loginForm.email,
                    password: this.loginForm.password,
                });

                if (response.status === 200) {
                    // Armazena o token no localStorage
                    localStorage.setItem('token', response.data.token);

                    // Armazena os dados do usuário no localStorage (opcional)
                    localStorage.setItem('user', JSON.stringify(response.data.user));

                    // Configura o token no cabeçalho das requisições do Axios
                    axios.defaults.headers.common['Authorization'] = `Token ${response.data.token}`;

                    alert('Login realizado com sucesso!');
                    // Redireciona para a página inicial ou painel do usuário
                    this.$router.push('/');
                } else {
                    alert('Erro ao fazer login: ' + response.data.error);
                }
            } catch (error) {
                alert('Erro ao fazer login: ' + (error.response?.data?.error || 'Credenciais inválidas'));
            }
        },
        async handleRegister() {
            if (!this.termsAccepted) {
                alert('Você deve aceitar os Termos e Condições para registrar.');
                return;
            }
            if (this.registerForm.password !== this.registerForm.confirm_password) {
                alert('As senhas não coincidem.');
                return;
            }
            try {
                const response = await axios.post('http://localhost:8000/account/register/', {
                    full_name: this.registerForm.full_name,
                    email: this.registerForm.email,
                    password: this.registerForm.password,
                    confirm_password: this.registerForm.confirm_password, // Certifique-se de enviar este campo
                });
                alert('Conta criada com sucesso!');
                this.isLogin = true; // Redireciona para o formulário de login
            } catch (error) {
                if (error.response && error.response.status === 400) {
                    const errors = error.response.data;

                    // Exibe mensagens de erro para todos os campos
                    let errorMessage = '';
                    for (const field in errors) {
                        errorMessage += `${field.charAt(0).toUpperCase() + field.slice(1)}: ${errors[field].join(', ')}\n`;
                    }

                    alert(errorMessage || 'Erro desconhecido');
                } else {
                    alert('Erro ao criar conta: Erro desconhecido');
                }
            }
        },
    }
}
</script>


<style scoped>
@import url(https://fonts.googleapis.com/css2?family=Lato&display=swap);
@import url(https://fonts.googleapis.com/css2?family=Open+Sans&display=swap);
@import url(https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200);
@import url(https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css);

/*! tailwindcss v3.4.11 | MIT License | https://tailwindcss.com*/
/* Estilos globais */
#painel {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
}

/* Estilos do painel */
main {
    flex-grow: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 1rem;
    /* Espaçamento interno */
}

/* Bordas e estilos do painel */
.w-\[400px\] {
    width: 400px;
    border: 1px solid #615c8e;
    /* Borda do painel */
    border-radius: 12px;
    /* Bordas arredondadas */
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    /* Sombra suave */
}

/* Estilos dos botões de alternância */
.active-form {
    background-color: #eed4ed;
    color: #282641;
    font-weight: bold;
}

.disable-form {
    background-color: transparent;
    color: #eed4ed;
    font-weight: bold;
}

/* Estilos do footer */
footer {
    flex-shrink: 0;
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

[role="button"],
button {
    cursor: pointer;
}

:disabled {
    cursor: default;
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
    --tw-scroll-snap-strictness: proximity;
    --tw-gradient-from-position: ;
    --tw-gradient-to-position: ;
    --tw-ring-offset-width: 0px;
    --tw-ring-offset-color: #fff;
    --tw-ring-color: rgba(59, 130, 246, 0.5);
    --tw-ring-offset-shadow: 0 0 #0000;
    --tw-ring-shadow: 0 0 #0000;
    --tw-shadow: 0 0 #0000;
    --tw-shadow-colored: 0 0 #0000;


}



#painel .absolute {
    position: absolute;
}

#painel .relative {
    position: relative;
}

#painel .left-0 {
    left: 0;
}

#painel .right-3 {
    right: 12px;
}

#painel .top-0 {
    top: 0;
}

#painel .top-3 {
    top: 12px;
}

#painel .mb-2 {
    margin-bottom: 8px;
}

#painel .mb-4 {
    margin-bottom: 16px;
}

#painel .mb-6 {
    margin-bottom: 24px;
}

#painel .ml-1 {
    margin-left: 4px;
}

#painel .mt-4 {
    margin-top: 16px;
}

#painel .mt-6 {
    margin-top: 24px;
}

#painel .flex {
    display: flex;
}

#painel .h-4 {
    height: 16px;
}

#painel .w-4 {
    width: 16px;
}

#painel .w-\[400px\] {
    width: 400px;
}

#painel .w-full {
    width: 100%;
}

#painel .flex-grow {
    flex-grow: 1;
}

#painel .scale-0 {
    --tw-scale-x: 0;
    --tw-scale-y: 0;
}



#painel .flex-row {
    flex-direction: row;
}

#painel .flex-col {
    flex-direction: column;
}

#painel .items-center {
    align-items: center;
}

#painel .justify-center {
    justify-content: center;
}


#painel :is(.space-x-2 > :not([hidden]) ~ :not([hidden])) {
    --tw-space-x-reverse: 0;
    margin-left: calc(8px * (1 - var(--tw-space-x-reverse)));
    margin-right: calc(8px * var(--tw-space-x-reverse));
}

#painel :is(.space-y-4 > :not([hidden]) ~ :not([hidden])) {
    --tw-space-y-reverse: 0;
    margin-bottom: calc(16px * var(--tw-space-y-reverse));
    margin-top: calc(16px * (1 - var(--tw-space-y-reverse)));
}


#painel .rounded-lg {
    border-radius: 24px;
}

#painel .rounded-md {
    border-radius: 18px;
}

#painel .rounded-sm {
    border-radius: 6px;
}

#painel .rounded-xl {
    border-radius: 36px;
}

#painel .border {
    border-width: 1px;
}

#painel .border-t {
    border-top-width: 1px;
}

#painel .border-\[\#615c8e\] {
    --tw-border-opacity: 1;
    border-color: rgb(97 92 142 / var(--tw-border-opacity));
}

#painel .border-\[\#a79de9\] {
    --tw-border-opacity: 1;
    border-color: rgb(167 157 233 / var(--tw-border-opacity));
}

#painel .bg-\[\#282641\] {
    --tw-bg-opacity: 1;
    background-color: rgb(40 38 65 / var(--tw-bg-opacity));
}

#painel .bg-\[\#3a375c\] {
    --tw-bg-opacity: 1;
    background-color: rgb(58 55 92 / var(--tw-bg-opacity));
}

#painel .bg-\[\#615c8e\] {
    --tw-bg-opacity: 1;
    background-color: rgb(97 92 142 / var(--tw-bg-opacity));
}

#painel .bg-\[\#eed4ed\] {
    --tw-bg-opacity: 1;
    background-color: rgb(238 212 237 / var(--tw-bg-opacity));
}

#painel .bg-gradient-to-r {
    background-image: linear-gradient(to right, var(--tw-gradient-stops));
}

#painel .from-\[\#615c8e\] {
    --tw-gradient-from: #615c8e var(--tw-gradient-from-position);
    --tw-gradient-to: rgba(97, 92, 142, 0) var(--tw-gradient-to-position);
    --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to);
}

#painel .to-\[\#a79de9\] {
    --tw-gradient-to: #a79de9 var(--tw-gradient-to-position);
}

#painel .p-1 {
    padding: 4px;
}

#painel .p-3 {
    padding: 12px;
}

#painel .p-8 {
    padding: 32px;
}

#painel .px-3 {
    padding-left: 12px;
    padding-right: 12px;
}

#painel .px-4 {
    padding-left: 16px;
    padding-right: 16px;
}

#painel .px-6 {
    padding-left: 24px;
    padding-right: 24px;
}

#painel .py-2 {
    padding-bottom: 8px;
    padding-top: 8px;
}

#painel .py-3 {
    padding-bottom: 12px;
    padding-top: 12px;
}

#painel .text-center {
    text-align: center;
}

#painel .text-3xl {
    font-size: 30px;
    line-height: 36px;
}

#painel .text-\[10px\] {
    font-size: 10px;
}

#painel .text-sm {
    font-size: 14px;
    line-height: 21px;
}

#painel .font-bold {
    font-weight: 700;
}

#painel .font-medium {
    font-weight: 500;
}

#painel .font-semibold {
    font-weight: 600;
}

#painel .text-\[\#282641\] {
    --tw-text-opacity: 1;
    color: rgb(40 38 65 / var(--tw-text-opacity));
}

#painel .text-\[\#a79de9\] {
    --tw-text-opacity: 1;
    color: rgb(167 157 233 / var(--tw-text-opacity));
}

#painel .text-\[\#eed4ed\] {
    --tw-text-opacity: 1;
    color: rgb(238 212 237 / var(--tw-text-opacity));
}

#painel .text-white {
    --tw-text-opacity: 1;
    color: rgb(255 255 255 / var(--tw-text-opacity));
}

#painel .opacity-0 {
    opacity: 0;
}

#painel .shadow-xl {
    --tw-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1);
    --tw-shadow-colored: 0 20px 25px -5px var(--tw-shadow-color), 0 8px 10px -6px var(--tw-shadow-color);
    box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
}

#painel .transition-all {
    transition-duration: 0.15s;
    transition-property: all;
    transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
}

#painel .transition-colors {
    transition-duration: 0.15s;
    transition-property: color, background-color, border-color, text-decoration-color, fill, stroke;
    transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
}

#painel .transition-transform {
    transition-duration: 0.15s;
    transition-property: transform;
    transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
}

#painel .duration-300 {
    transition-duration: 0.3s;
}

#painel {
    font-family: Open Sans !important;
    font-size: 16px !important;
}

#painel .placeholder\:text-\[\#a79de9\]\/70::placeholder {
    color: rgba(167, 157, 233, 0.7);
}

#painel .hover\:-translate-y-1:hover {
    --tw-translate-y: -4px;
}

#painel .hover\:-translate-y-1:hover,
#painel .hover\:scale-105:hover {
    transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

#painel .hover\:scale-105:hover {
    --tw-scale-x: 1.05;
    --tw-scale-y: 1.05;
}

#painel .hover\:bg-\[\#615c8e\]:hover {
    --tw-bg-opacity: 1;
    background-color: rgb(97 92 142 / var(--tw-bg-opacity));
}

#painel .hover\:bg-\[\#615c8e\]\/50:hover {
    background-color: rgba(97, 92, 142, 0.5);
}

#painel .hover\:text-\[\#eed4ed\]:hover {
    --tw-text-opacity: 1;
    color: rgb(238 212 237 / var(--tw-text-opacity));
}

#painel .hover\:underline:hover {
    text-decoration-line: underline;
}

#painel .hover\:shadow-lg:hover {
    --tw-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.1);
    --tw-shadow-colored: 0 10px 15px -3px var(--tw-shadow-color), 0 4px 6px -4px var(--tw-shadow-color);
    box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
}

#painel .hover\:shadow-\[\#a79de9\]\/20:hover {
    --tw-shadow-color: rgba(167, 157, 233, 0.2);
    --tw-shadow: var(--tw-shadow-colored);
}

#painel .focus\:outline-none:focus {
    outline: 2px solid transparent;
    outline-offset: 2px;
}

#painel .focus\:ring-2:focus {
    --tw-ring-offset-shadow: var(--tw-ring-inset) 0 0 0 var(--tw-ring-offset-width) var(--tw-ring-offset-color);
    --tw-ring-shadow: var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color);
    box-shadow: var(--tw-ring-offset-shadow), var(--tw-ring-shadow), var(--tw-shadow, 0 0 #0000);
}

#painel .focus\:ring-\[\#a79de9\]:focus {
    --tw-ring-opacity: 1;
    --tw-ring-color: rgb(167 157 233 / var(--tw-ring-opacity));
}

#painel :is(.group:hover .group-hover\:text-\[\#eed4ed\]) {
    --tw-text-opacity: 1;
    color: rgb(238 212 237 / var(--tw-text-opacity));
}

#painel :is(.peer:checked ~ .peer-checked\:scale-75) {
    --tw-scale-x: 0.75;
    --tw-scale-y: 0.75;
    transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

#painel :is(.peer:checked ~ .peer-checked\:border-0) {
    border-width: 0;
}

#painel :is(.peer:checked ~ .peer-checked\:bg-\[\#a79de9\]) {
    --tw-bg-opacity: 1;
    background-color: rgb(167 157 233 / var(--tw-bg-opacity));
}


.active-form {
    background-color: #282641;
    color: #282641;
    background: #eed4ed;
    font-weight: bold;
    font-family: font-semibold;
}

.disable-form {
    background-color: #eed4ed;
    color: #eed4ed;
    background: #282641;
    font-weight: bold;
    font-family: font-semibold;
}


.form-toggle button:hover {
    background-color: #eed4ed;
}


body {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
    margin: 0;
    padding: 10px;
}

.painelbody {
    padding-top: 35%;
    width: 20%;
    position: relative;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}

#painel {
    flex: 1;
}


footer {
    text-align: center;
    padding: 40%;
    margin-top: -25%;
}

.hidden {
    display: none;
}

#painel {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
    position: relative;
}


.background {
    position: fixed;
    width: 100vw;
    height: 100vh;
    top: 0;
    left: 0;
    margin: 0;
    padding: 0;
    background: #d4d4d4;
    overflow: hidden;
    z-index: -1;
    /* Garante que o fundo fique atrás do conteúdo */
}

.background li {
    position: absolute;
    display: block;
    list-style: none;
    width: 20px;
    height: 20px;
    background: rgba(255, 255, 255, 0.2);
    animation: animate 10s linear infinite;
}

@keyframes animate {
    0% {
        transform: translateY(0) rotate(0deg);
        opacity: 1;
        border-radius: 0;
    }

    100% {
        transform: translateY(-1000px) rotate(720deg);
        opacity: 0;
        border-radius: 50%;
    }
}

.background li:nth-child(0) {
    left: 20%;
    width: 154px;
    height: 154px;
    bottom: -154px;
    animation-delay: 1s;
}

.background li:nth-child(1) {
    left: 86%;
    width: 133px;
    height: 133px;
    bottom: -133px;
    animation-delay: 4s;
}

.background li:nth-child(2) {
    left: 86%;
    width: 163px;
    height: 163px;
    bottom: -163px;
    animation-delay: 5s;
}

.background li:nth-child(3) {
    left: 68%;
    width: 97px;
    height: 97px;
    bottom: -97px;
    animation-delay: 14s;
}

.background li:nth-child(4) {
    left: 2%;
    width: 160px;
    height: 160px;
    bottom: -160px;
    animation-delay: 11s;
}

.background li:nth-child(5) {
    left: 36%;
    width: 113px;
    height: 113px;
    bottom: -113px;
    animation-delay: 13s;
}

.background li:nth-child(6) {
    left: 40%;
    width: 92px;
    height: 92px;
    bottom: -92px;
    animation-delay: 18s;
}

.background li:nth-child(7) {
    left: 66%;
    width: 129px;
    height: 129px;
    bottom: -129px;
    animation-delay: 16s;
}

.background li:nth-child(8) {
    left: 7%;
    width: 104px;
    height: 104px;
    bottom: -104px;
    animation-delay: 9s;
}

.background li:nth-child(9) {
    left: 25%;
    width: 149px;
    height: 149px;
    bottom: -149px;
    animation-delay: 29s;
}

.background li:nth-child(10) {
    left: 51%;
    width: 120px;
    height: 120px;
    bottom: -120px;
    animation-delay: 6s;
}

.background li:nth-child(11) {
    left: 87%;
    width: 84px;
    height: 84px;
    bottom: -84px;
    animation-delay: 1s;
}

.background li:nth-child(12) {
    left: 53%;
    width: 90px;
    height: 90px;
    bottom: -90px;
    animation-delay: 39s;
}

.background li:nth-child(13) {
    left: 77%;
    width: 83px;
    height: 83px;
    bottom: -83px;
    animation-delay: 54s;
}

.background li:nth-child(14) {
    left: 6%;
    width: 90px;
    height: 90px;
    bottom: -90px;
    animation-delay: 64s;
}

.background li:nth-child(15) {
    left: 27%;
    width: 180px;
    height: 180px;
    bottom: -180px;
    animation-delay: 24s;
}

.background li:nth-child(16) {
    left: 87%;
    width: 182px;
    height: 182px;
    bottom: -182px;
    animation-delay: 47s;
}

.background li:nth-child(17) {
    left: 53%;
    width: 98px;
    height: 98px;
    bottom: -98px;
    animation-delay: 76s;
}

.background li:nth-child(18) {
    left: 30%;
    width: 77px;
    height: 77px;
    bottom: -77px;
    animation-delay: 76s;
}

.background li:nth-child(19) {
    left: 9%;
    width: 133px;
    height: 133px;
    bottom: -133px;
    animation-delay: 47s;
}

.background li:nth-child(20) {
    left: 42%;
    width: 117px;
    height: 117px;
    bottom: -117px;
    animation-delay: 100s;
}

.background li:nth-child(21) {
    left: 64%;
    width: 169px;
    height: 169px;
    bottom: -169px;
    animation-delay: 103s;
}

.background li:nth-child(22) {
    left: 64%;
    width: 106px;
    height: 106px;
    bottom: -106px;
    animation-delay: 88s;
}

.background li:nth-child(23) {
    left: 69%;
    width: 110px;
    height: 110px;
    bottom: -110px;
    animation-delay: 37s;
}

.background li:nth-child(24) {
    left: 76%;
    width: 126px;
    height: 126px;
    bottom: -126px;
    animation-delay: 62s;
}

.background li:nth-child(25) {
    left: 50%;
    width: 181px;
    height: 181px;
    bottom: -181px;
    animation-delay: 82s;
}

.background li:nth-child(26) {
    left: 50%;
    width: 93px;
    height: 93px;
    bottom: -93px;
    animation-delay: 121s;
}

.background li:nth-child(27) {
    left: 38%;
    width: 177px;
    height: 177px;
    bottom: -177px;
    animation-delay: 101s;
}

.background li:nth-child(28) {
    left: 85%;
    width: 81px;
    height: 81px;
    bottom: -81px;
    animation-delay: 71s;
}

.background li:nth-child(29) {
    left: 29%;
    width: 79px;
    height: 79px;
    bottom: -79px;
    animation-delay: 124s;
}
</style>