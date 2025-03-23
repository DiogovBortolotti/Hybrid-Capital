# Documentação do Projeto Django + Vue.js

Este projeto utiliza Django para o backend e Vue.js para o frontend. A documentação abaixo fornece instruções detalhadas para configurar e executar o projeto, incluindo as variáveis de ambiente necessárias.

## 🛠️ Configuração do Projeto

### Pré-requisitos

- Python 3.12.5 🐍
- Node.js (para o frontend Vue.js) 📦
- pip (gerenciador de pacotes do Python) 📦
- npm ou yarn (gerenciador de pacotes do Node.js) 📦
- PostgreSQL (banco de dados) 🐘

---

## 🐍 Backend (Django)

### Passos para Configuração

1. **Clone o repositório:**

    ```bash
    git clone https://github.com/DiogovBortolotti/Hybrid-Capital
    cd backend
    ```

2. **Crie e ative um ambiente virtual:**

    - Para Linux/macOS:

        ```bash
        python -m venv venv
        source venv/bin/activate
        ```

    - Para Windows:

        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```

3. **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure as variáveis de ambiente:**

    Crie um arquivo `.env` na raiz do backend e adicione as seguintes variáveis:

    | Variável               | Descrição                                             | Exemplo                    |
    |------------------------|-------------------------------------------------------|----------------------------|
    | `SECRET_KEY`           | Chave secreta do Django                               | `'sua_chave_secreta_aqui'` |
    | `DEBUG`                | Modo de depuração (True/False)                        | `'true'`                   |
    | `POSTGRES_DB`          | Nome do banco de dados PostgreSQL                      | `"meu_banco"`              |
    | `POSTGRES_USER`        | Usuário do PostgreSQL                                 | `"meu_usuario"`            |
    | `POSTGRES_PASSWORD`    | Senha do PostgreSQL                                   | `"minha_senha"`            |
    | `POSTGRES_HOST`        | Host do PostgreSQL                                    | `"localhost"`              |
    | `POSTGRES_PORT`        | Porta do PostgreSQL                                   | `"5432"`                   |
    | `ALLOWED_HOSTS`        | Hosts permitidos no Django                            | `localhost,127.0.0.1`      |
    | `CORS_ALLOWED_ORIGINS` | Origens permitidas para CORS                          | `"http://localhost:8080"`  |

    Exemplo de `.env`:

    ```env
    SECRET_KEY='sua_chave_secreta_aqui'
    DEBUG='true'
    POSTGRES_DB="meu_banco"
    POSTGRES_USER="meu_usuario"
    POSTGRES_PASSWORD="minha_senha"
    POSTGRES_HOST="localhost"
    POSTGRES_PORT="5432"
    ALLOWED_HOSTS=localhost,127.0.0.1
    CORS_ALLOWED_ORIGINS="http://localhost:8080"
    ```

5. **Execute as migrações:**

    ```bash
    python manage.py migrate
    ```

6. **Crie um superusuário (opcional):**

    ```bash
    python manage.py createsuperuser
    ```

7. **Inicie o servidor de desenvolvimento:**

    ```bash
    python manage.py runserver
    ```

O backend estará rodando em `http://127.0.0.1:8000/`.

---

## 🖥️ Frontend (Vue.js)

### Passos para Configuração

1. **Navegue até a pasta do frontend:**

    ```bash
    cd ../frontend
    ```

2. **Instale as dependências:**

    ```bash
    npm install
    ```

    ou, se estiver usando Yarn:

    ```bash
    yarn install
    ```

3. **Configure as variáveis de ambiente:**

    Crie um arquivo `.env` na raiz do frontend e adicione as seguintes variáveis:

    | Variável               | Descrição                                           | Exemplo                   |
    |------------------------|-----------------------------------------------------|---------------------------|
    | `VUE_APP_API_URL`       | URL da API do backend                               | `http://localhost:8000`    |
    | `VUE_APP_DEBUG`         | Modo de depuração (True/False)                      | `true`                    |
    | `VUE_APP_SITE_NAME`     | Nome do site                                        | `"Hybrid Capital"`        |
    | `VUE_APP_SUPPORT_EMAIL` | E-mail de suporte                                   | `"support@meusite.com"`    |

    Exemplo de `.env`:

    ```env
    VUE_APP_API_URL=http://localhost:8000
    VUE_APP_DEBUG=true
    VUE_APP_SITE_NAME=Hybrid Capital
    VUE_APP_SUPPORT_EMAIL=support@meusite.com
    ```

4. **Inicie o servidor de desenvolvimento:**

    ```bash
    npm run serve
    ```

    ou, se estiver usando Yarn:

    ```bash
    yarn serve
    ```

O frontend estará rodando em `http://localhost:8080`.

---

## 🔄 Integração Backend e Frontend

O frontend (Vue.js) já está configurado para se comunicar com o backend (Django) através da variável `VUE_APP_API_URL`.

Certifique-se de que o backend está rodando antes de iniciar o frontend.

---

## 🚀 Executando o Projeto

1. **Inicie o backend:**

    ```bash
    cd backend
    python manage.py runserver
    ```

2. **Inicie o frontend:**

    ```bash
    cd frontend
    npm run serve
    ```

3. **Acesse o frontend:**

    Abra o navegador e acesse `http://localhost:8080`.

---

## 📝 Observações

- Para produção, configure o Django para servir os arquivos estáticos do Vue.js ou utilize um servidor web como Nginx.
- Certifique-se de que as variáveis de ambiente estejam corretamente configuradas tanto no backend 
quanto no frontend.

## 😎 Extra
Se você estiver utilizando Linux, esses comandos iram facilitar na inicialização:

Criar a ativação o ambiente virtual e instala os requisitos com seguinte comando:
```bash
make venv
```

Para inicializar o backend do projeto, execute o seguinte comando:

```bash
make backend
```

Da mesma forma, para inicializar o frontend, execute:

```bash
make frontend
```

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

