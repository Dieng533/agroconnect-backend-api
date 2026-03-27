import os
import django
from decouple import config, UndefinedValueError

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.db import connection
from django.core.management import execute_from_command_line

def test_supabase_connection():
    """Tester la connexion à Supabase"""
    print("🌾 TEST DE CONNEXION SUPABASE - AGROCONNECT")
    print("=" * 50)
    
    try:
        # Essayer de lire le fichier .env
        try:
            config('DB_NAME')
            print("✅ Fichier .env trouvé et lu avec succès!")
        except UndefinedValueError:
            print("❌ Fichier .env non trouvé ou mal configuré")
            print("\n🔧 Solutions possibles:")
            print("1. Vérifiez que le fichier .env existe dans le dossier backend")
            print("2. Vérifiez le contenu du fichier .env")
            print("3. Assurez-vous que python-decouple est installé")
            return False
        
        # Test de connexion
        with connection.cursor() as cursor:
            cursor.execute("SELECT version();")
            db_version = cursor.fetchone()
            print("✅ Connexion à Supabase réussie!")
            print(f"📊 Version PostgreSQL: {db_version[0][:50]}...")
            
            # Test des tables
            cursor.execute("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public'
                ORDER BY table_name;
            """)
            tables = cursor.fetchall()
            print(f"\n📋 Tables trouvées: {len(tables)}")
            for table in tables:
                print(f"   - {table[0]}")
            
            # Test des utilisateurs
            try:
                cursor.execute("SELECT COUNT(*) FROM users_user;")
                user_count = cursor.fetchone()[0]
                print(f"\n👥 Utilisateurs dans la base: {user_count}")
            except Exception as e:
                print(f"\n⚠️  Erreur table users_user: {e}")
            
            # Test des produits
            try:
                cursor.execute("SELECT COUNT(*) FROM products_product;")
                product_count = cursor.fetchone()[0]
                print(f"📦 Produits dans la base: {product_count}")
            except Exception as e:
                print(f"\n⚠️  Erreur table products_product: {e}")
            
            # Test des commandes
            try:
                cursor.execute("SELECT COUNT(*) FROM products_order;")
                order_count = cursor.fetchone()[0]
                print(f"🛒 Commandes dans la base: {order_count}")
            except Exception as e:
                print(f"\n⚠️  Erreur table products_order: {e}")
                
        print("\n" + "=" * 50)
        print("🎉 Tous les tests de connexion réussis!")
        return True
        
    except Exception as e:
        print(f"\n❌ Erreur de connexion: {e}")
        print("\n🔧 Solutions possibles:")
        print("1. Vérifiez les identifiants Supabase dans .env")
        print("2. Assurez-vous que le projet Supabase est actif")
        print("3. Vérifiez la configuration SSL")
        print("4. Testez la connexion avec psql directement")
        print("5. Exécutez d'abord le script SQL dans Supabase")
        return False

def check_environment():
    """Vérifier les variables d'environnement"""
    print("\n🔍 Vérification des variables d'environnement:")
    
    try:
        required_vars = [
            'DB_NAME', 
            'DB_USER', 
            'DB_PASSWORD',
            'DB_HOST',
            'DB_PORT'
        ]
        
        missing_vars = []
        
        for var in required_vars:
            try:
                value = config(var)
                if 'PASSWORD' in var:
                    print(f"   ✅ {var}: {'*' * len(value)}")
                else:
                    print(f"   ✅ {var}: {value}")
            except AutoConfigException:
                print(f"   ❌ {var}: NON DÉFINIE")
                missing_vars.append(var)
        
        if missing_vars:
            print(f"\n⚠️  Variables manquantes: {', '.join(missing_vars)}")
            print("📝 Créez un fichier .env avec ces variables:")
            print("\n# Configuration Supabase")
            print("DB_NAME=postgres")
            print("DB_USER=postgres") 
            print("DB_PASSWORD=AGOCONECT@12345678")
            print("DB_HOST=db.ugbmqxlrgwxihlgmcuuj.supabase.co")
            print("DB_PORT=5432")
            return False
        else:
            print("\n✅ Toutes les variables d'environnement sont définies!")
            return True
            
    except Exception as e:
        print(f"\n❌ Erreur lors de la vérification: {e}")
        return False

def run_migrations():
    """Exécuter les migrations Django"""
    print("\n🔄 Exécution des migrations Django...")
    try:
        execute_from_command_line(['manage.py', 'migrate'])
        print("✅ Migrations exécutées avec succès!")
        return True
    except Exception as e:
        print(f"❌ Erreur lors des migrations: {e}")
        return False

def main():
    """Fonction principale"""
    print("🌾 CONFIGURATION SUPABASE - AGROCONNECT")
    print("=" * 50)
    
    # 1. Vérifier les variables d'environnement
    if not check_environment():
        print("\n📝 Créez le fichier .env manuellement ou utilisez le template fourni.")
        return
    
    # 2. Tester la connexion
    if test_supabase_connection():
        # 3. Exécuter les migrations si nécessaire
        run_migrations()
        
        print("\n🎯 Prochaines étapes:")
        print("1. Démarrez le serveur: python manage.py runserver")
        print("2. Testez l'API: http://127.0.0.1:8000/api/products/")
        print("3. Accédez à l'admin: http://127.0.0.1:8000/admin/")
    else:
        print("\n📚 Documentation complète: SUPABASE_INSTRUCTIONS.md")

if __name__ == '__main__':
    main()
