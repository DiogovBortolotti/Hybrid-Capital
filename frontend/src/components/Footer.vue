<template>
    <div class="min-h-screen flex flex-col">
        <main class="flex-grow">

        </main>
        <footer class="bg-[#282641] text-white py-12 px-8">
            <div class="grid grid-cols-4 gap-10 mb-9">
                <div>
                    <div class="flex items-center space-x-2 mb-5">
                        <svg class="w-6 h-6 text-[#a79de9]" viewBox="0 0 24 24" fill="none"
                            xmlns="http://www.w3.org/2000/svg">
                            <path d="M12 2L2 7L12 12L22 7L12 2Z" fill="currentColor"></path>
                            <path d="M2 17L12 22L22 17" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                stroke-linejoin="round"></path>
                            <path d="M2 12L12 17L22 12" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                stroke-linejoin="round"></path>
                        </svg>
                        <h3 class="text-xl font-bold tracking-tight">Hybrid Capital</h3>
                    </div>
                    <p class="text-[#a79de9] mb-5 leading-relaxed">
                        Sua plataforma completa para gestão financeira e investimentos.
                    </p>
                    <div class="flex space-x-5">
                        <a href="https://github.com/DiogovBortolotti" target="_blank" rel="noopener noreferrer"
                            class="text-white hover:text-[#a79de9] transition-colors transform hover:scale-110 duration-300">
                            <i class="fa-brands fa-github text-2xl"></i>
                        </a>
                        <a href="https://www.instagram.com/diogovbortolotti" target="_blank" rel="noopener noreferrer"
                            class="text-white hover:text-[#a79de9] transition-colors transform hover:scale-110 duration-300">
                            <i class="fa-brands fa-instagram text-2xl"></i>
                        </a>
                        <a href="https://www.linkedin.com/in/diogobortolotti" target="_blank" rel="noopener noreferrer"
                            class="text-white hover:text-[#a79de9] transition-colors transform hover:scale-110 duration-300">
                            <i class="fa-brands fa-linkedin text-2xl"></i>
                        </a>
                    </div>
                </div>
                <div>
                    <h3 class="text-lg font-bold mb-2 tracking-tight">Serviços</h3>
                    <ul class="space-y-3">
                        <li>
                            <a href="#"
                                class="text-[#a79de9] hover:text-white transition-colors inline-block hover:translate-x-1 duration-200">Gestão
                                Financeira</a>
                        </li>
                        <li>
                            <a href="#"
                                class="text-[#a79de9] hover:text-white transition-colors inline-block hover:translate-x-1 duration-200">Investimentos</a>
                        </li>
                        <li>
                            <a href="#"
                                class="text-[#a79de9] hover:text-white transition-colors inline-block hover:translate-x-1 duration-200">Trading
                                Bot</a>
                        </li>
                        <li>
                            <a href="#"
                                class="text-[#a79de9] hover:text-white transition-colors inline-block hover:translate-x-1 duration-200">Calendário
                                de Dividendos</a>
                        </li>
                    </ul>
                </div>
                <div>
                    <h3 class="text-lg font-bold mb-2 tracking-tight">Suporte</h3>
                    <ul class="space-y-3">
                        <li>
                            <a href="#"
                                class="text-[#a79de9] hover:text-white transition-colors inline-block hover:translate-x-1 duration-200">FAQ</a>
                        </li>
                        <li>
                            <a href="#"
                                class="text-[#a79de9] hover:text-white transition-colors inline-block hover:translate-x-1 duration-200">Centro
                                de Ajuda</a>
                        </li>
                        <li>
                            <a href="#"
                                class="text-[#a79de9] hover:text-white transition-colors inline-block hover:translate-x-1 duration-200">Contato</a>
                        </li>
                        <li>
                            <a href="#"
                                class="text-[#a79de9] hover:text-white transition-colors inline-block hover:translate-x-1 duration-200">Tutoriais</a>
                        </li>
                    </ul>
                </div>
            </div>
            <div class="border-t border-[#615c8e] pt-2 flex justify-between items-center">
                <p class="text-[#a79de9]">© 2025 Hybrid Capital. Todos os direitos reservados.</p>
                <div class="flex space-x-6">
                    <a href="#" class="text-[#a79de9] hover:text-white transition-colors">Termos</a>
                    <a href="#" class="text-[#a79de9] hover:text-white transition-colors">Privacidade</a>
                </div>
            </div>
        </footer>
    </div>
</template>
<style scoped>
footer {
    bottom: 0;
    left: 0;
    width: 100%;
    background-color: #282641;
    color: #eed4ed;
    text-align: center;
    padding: 16px;
}

.footer-content {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 40px;
    margin-bottom: 40px;
}

.footer-logo {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 20px;
}

.footer-logo svg {
    width: 24px;
    height: 24px;
    color: #a79de9;
}

.footer-logo h3 {
    font-size: 20px;
    font-weight: 700;
}

.footer-description {
    color: #a79de9;
    margin-bottom: 20px;
    line-height: 1.625;
}

.footer-social {
    display: flex;
    gap: 20px;
}

.footer-social a {
    color: white;
    transition: color 0.3s, transform 0.3s;
}

.footer-social a:hover {
    color: #a79de9;
    transform: scale(1.1);
}

.footer-section h3 {
    font-size: 18px;
    font-weight: 700;
    margin-bottom: 20px;
}

.footer-section ul {
    display: flex;
    flex-direction: column;
    gap: 12px;
}

.footer-section ul li a {
    color: #a79de9;
    transition: color 0.3s, transform 0.3s;
}

.footer-section ul li a:hover {
    color: white;
    transform: translateX(4px);
}

.footer-bottom {
    border-top: 1px solid #615c8e;
    padding-top: 24px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.footer-bottom p {
    color: #a79de9;
}

.footer-bottom a {
    color: #a79de9;
    transition: color 0.3s;
}

.footer-bottom a:hover {
    color: white;
}

/* Efeitos de hover específicos */
.footer-social a:hover {
    color: #a79de9;
    transform: scale(1.1);
}

.footer-section ul li a:hover {
    color: white;
    transform: translateX(4px);
}

.footer-bottom a:hover {
    color: white;
}
</style>
<script>
export default {
    name: "FooterComponent"
};
</script>