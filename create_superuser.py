import os
import django

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Créer le superutilisateur s'il n'existe pas
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser(
        username='admin',
        email='admin@agroconnect.local',
        password='admin123'
    )
    print("✅ Superutilisateur créé avec succès!")
    print("📝 Identifiants:")
    print("   Username: admin")
    print("   Password: admin123")
    print("   Email: admin@agroconnect.local")
else:
    print("ℹ️  Le superutilisateur 'admin' existe déjà.")
