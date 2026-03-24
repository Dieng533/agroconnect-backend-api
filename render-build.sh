#!/bin/bash

set -e  # Arrêter le script si une commande échoue

echo "🚀 Starting build process..."

# Installation des dépendances
echo "📦 Installing requirements..."
pip install -r requirements.txt

# Appliquer les migrations
echo "🗄️ Running migrations..."
python manage.py migrate

# Collecter les fichiers statiques
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

echo "✅ Build completed successfully!"
