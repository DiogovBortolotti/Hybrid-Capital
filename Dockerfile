FROM python:3.12.5-slim-bullseye

# Definir diretório de trabalho
WORKDIR /app

# Instalar dependências do sistema necessárias para o PostgreSQL e compilar pacotes Python
RUN apt-get update && apt-get install -y libpq-dev gcc

# Copiar arquivos necessários
COPY requirements.txt .

# Instalar dependências com cache para otimizar builds
RUN --mount=type=cache,target=/root/.cache/pip pip install --no-cache-dir -r requirements.txt

# Copiar o código do projeto para o container
COPY . .

# Rodar o collectstatic para coletar arquivos estáticos
RUN python manage.py collectstatic --noinput

# Expor a porta do Django
EXPOSE 8000

# Iniciar Gunicorn em produção
CMD ["gunicorn", "--workers=3", "--bind=0.0.0.0:8000", "app.wsgi:application"]
