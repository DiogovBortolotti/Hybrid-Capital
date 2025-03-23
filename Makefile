# Variáveis
PYTHON = python3
DJANGO_MANAGE = $(PYTHON) backend/manage.py
VENV = venv
FRONTEND_DIR = frontend
BACKEND_DIR = backend


.PHONY: venv
venv:
	$(PYTHON) -m venv $(VENV)
	$(VENV)/bin/pip install -r $(BACKEND_DIR)/requirements.txt


.PHONY: backend
backend:
	$(DJANGO_MANAGE) runserver

# Rodar o frontend Vue.js
.PHONY: frontend
frontend:
	cd $(FRONTEND_DIR) && npm install && npm run serve


.PHONY: run
run: backend frontend

.PHONY: migrations
migrations:
	$(DJANGO_MANAGE) makemigrations
	$(DJANGO_MANAGE) migrate


.PHONY: superuser
superuser:
	$(DJANGO_MANAGE) createsuperuser


.PHONY: clean
clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete