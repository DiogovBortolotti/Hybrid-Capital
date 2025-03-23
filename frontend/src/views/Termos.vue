<template>
    <div class="termo">
        <h1>TERMO DE RESPONSABILIDADE</h1>

        <div class="section">
            <h2 class="section-title">1. DAS DISPOSIÇÕES GERAIS</h2>
            <p>Ao utilizar o site {{ siteName }}, você declara estar ciente e concorda com os termos abaixo,
                responsabilizando-se integralmente pelas informações fornecidas e pelo uso das funcionalidades
                disponibilizadas.</p>
        </div>

        <div class="section">
            <h2 class="section-title">2. DA COLETA E USO DE DADOS PESSOAIS</h2>
            <p><strong>2.1.</strong> Para acesso e utilização de determinadas funcionalidades, poderão ser
                solicitadas informações pessoais, tais como nome e e-mail.</p>
            <p><strong>2.2.</strong> O usuário é responsável pela veracidade e atualização dos dados informados,
                isentando o {{ siteName }} de qualquer responsabilidade por informações incorretas ou
                desatualizadas.</p>
            <p><strong>2.3.</strong> Os dados coletados serão utilizados exclusivamente para os fins de
                gerenciamento financeiro e investimentos dentro da plataforma, respeitando a legislação vigente
                sobre proteção de dados.</p>
        </div>

        <div class="section">
            <h2 class="section-title">3. DAS FUNCIONALIDADES DISPONIBILIZADAS</h2>
            <p><strong>3.1.</strong> O site oferece ferramentas para controle financeiro e investimentos, incluindo,
                mas não se limitando a:</p>
            <ul>
                <li>Gráficos de desempenho financeiro;</li>
                <li>Acompanhamento de valores investidos;</li>
                <li>Lançamentos de investimentos e finanças;</li>
                <li>Ferramenta de automação (bot) para suporte e análise;</li>
                <li>Cálculo e acompanhamento de dividendos de ações.</li>
            </ul>
            <p><strong>3.2.</strong> As informações disponibilizadas pelo site são meramente informativas e não
                configuram recomendações financeiras, cabendo ao usuário a tomada de decisões com base em sua
                própria análise.</p>
        </div>

        <div class="section">
            <h2 class="section-title">4. DA ISENÇÃO DE RESPONSABILIDADE</h2>
            <p><strong>4.1.</strong> O {{ siteName }} não se responsabiliza por quaisquer perdas financeiras,
                prejuízos ou decisões tomadas com base nas informações fornecidas pela plataforma.</p>
            <p><strong>4.2.</strong> O usuário reconhece que investimentos, incluindo criptomoedas, ações e renda
                variável, possuem riscos e que a responsabilidade por eventuais perdas é exclusivamente sua.</p>
        </div>

        <div class="section">
            <h2 class="section-title">5. DA SEGURANÇA E PRIVACIDADE</h2>
            <p><strong>5.1.</strong> O {{ siteName }} adota medidas de segurança para proteger os dados dos
                usuários, porém não se responsabiliza por acessos indevidos decorrentes de falhas externas, como
                ataques cibernéticos ou negligência do usuário na proteção de suas credenciais.</p>
            <p><strong>5.2.</strong> O usuário concorda em manter a confidencialidade de suas credenciais de acesso
                e reconhece que é o único responsável por atividades realizadas em sua conta.</p>
        </div>

        <div class="section">
            <h2 class="section-title">6. DA ACEITAÇÃO DOS TERMOS</h2>
            <p><strong>6.1.</strong> Ao utilizar o site, o usuário concorda com os termos aqui descritos,
                reconhecendo sua responsabilidade sobre as informações fornecidas e as decisões financeiras tomadas
                com base na plataforma.</p>
            <p><strong>6.2.</strong> O {{ siteName }} se reserva o direito de modificar este termo a qualquer
                momento, sendo responsabilidade do usuário manter-se atualizado quanto às alterações.</p>
            <p><strong>6.3.</strong> A aceitação deste termo será registrada eletronicamente no momento do cadastro
                do usuário na plataforma e poderá ser confirmada via e-mail.</p>
        </div>

        <div class="section">
            <h2 class="section-title">7. DO FORO COMPETENTE</h2>
            <p><strong>7.1.</strong> Em caso de litígios oriundos deste termo, as comunicações e tentativas de
                resolução serão feitas via e-mail cadastrado pelo usuário.</p>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            siteName: process.env.VUE_APP_SITE_NAME || "[Nome do Site]",
            supportEmail: process.env.VUE_APP_SUPPORT_EMAIL || "suporte@site.com",
            aceitou: false // Estado do checkbox
        };
    }
};
</script>

<style scoped>
.termo {
    font-family: Arial, sans-serif;
    max-width: 800px;
    margin: auto;
    padding: 20px;
}

.section {
    margin-bottom: 20px;
}

.section-title {
    font-weight: bold;
    margin-bottom: 10px;
}

.termo-rodape {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 20px;
}

button {
    margin-top: 10px;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
}

button:disabled {
    background-color: #ccc;
    cursor: not-allowed;
}
</style>