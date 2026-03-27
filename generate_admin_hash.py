#!/usr/bin/env python
"""
Script pour générer le hash du mot de passe admin pour Supabase
"""

import os
import django
from django.contrib.auth.hashers import make_password

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

def generate_admin_password_hash():
    """Générer le hash pour le mot de passe admin"""
    password = "admin123"
    hashed_password = make_password(password)
    
    print("🔐 HASH DU MOT DE PASSE ADMIN")
    print("=" * 40)
    print(f"Mot de passe: {password}")
    print(f"Hash généré: {hashed_password}")
    print("=" * 40)
    print("\n📝 Copiez ce hash dans le script SQL:")
    print(f"'{hashed_password}'")
    print("\n💡 Ou utilisez la commande Django:")
    print("python manage.py shell")
    print(">>> from django.contrib.auth.hashers import make_password")
    print(">>> make_password('admin123')")
    
    return hashed_password

if __name__ == '__main__':
    generate_admin_password_hash()
