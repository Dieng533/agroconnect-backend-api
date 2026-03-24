#!/bin/bash

# Installation des dépendances
pip install -r requirements.txt

# Appliquer les migrations
python manage.py makemigrations
python manage.py migrate

# Collecter les fichiers statiques
python manage.py collectstatic --noinput

# Créer un superutilisateur si nécessaire (optionnel)
# python manage.py shell < create_superuser.py

echo "Build completed successfully!"
