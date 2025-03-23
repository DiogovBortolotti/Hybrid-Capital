<template>
    <header class="header">
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
</template>

<script>
export default {
    name: "HeaderComponent"
};
</script>

<style scoped>
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
