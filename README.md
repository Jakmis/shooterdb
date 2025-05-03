# Shooterdb

Informační systém pro záznam výsledků střelby

## Instalace

- Vytvoření vyrtuálního prostředí
  - `python -m venv .venv`
- Instalace balíčků
  - `pip install -r requirements.txt`

## První spuštění

- Vytvoření admina
  - `python manage.py createsuperuser`
- Migrace databáze
  - `python manage.py makemigrations`
  - `python manage.py migrate`

## Spuštění

`python manage.py runserver`

- Stránka bude přístupná na http://127.0.0.1:8000
