FROM python:3.12.5-slim-bullseye


WORKDIR /app

RUN apt-get update && apt-get install -y libpq-dev gcc


COPY requirements.txt .

RUN --mount=type=cache,target=/root/.cache/pip pip install --no-cache-dir -r requirements.txt


COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--workers=3", "--bind=0.0.0.0:8000", "app.wsgi:application"]
