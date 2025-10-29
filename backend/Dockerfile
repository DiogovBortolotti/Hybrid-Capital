FROM python:3.12.5-slim-bullseye

# Dependências do sistema
RUN apt-get update && apt-get install -y \
    gcc \
    libffi-dev \
    libpq-dev \
    bash \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copiar requirements e instalar
COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt gunicorn psycopg2-binary

# Copiar backend
COPY . .

EXPOSE 8000


CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && gunicorn settings.wsgi:application --bind 0.0.0.0:8000"]
