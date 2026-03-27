# 🗄️ Configuration Supabase pour AgroConnect

## 📋 Table des matières

1. [Création du projet Supabase](#création-du-projet-supabase)
2. [Configuration de la base de données](#configuration-de-la-base-de-données)
3. [Migration des données](#migration-des-données)
4. [Configuration Django](#configuration-django)
5. [Variables d'environnement](#variables-denvironnement)
6. [Test de connexion](#test-de-connexion)

---

## 🚀 Création du projet Supabase

### Étape 1: Inscription sur Supabase
1. Allez sur [https://supabase.com](https://supabase.com)
2. Cliquez sur "Start your project"
3. Connectez-vous avec GitHub ou Google

### Étape 2: Création du projet
1. **Nom du projet**: `agroconnect-db`
2. **Mot de passe de la base**: Choisissez un mot de passe sécurisé
3. **Région**: Choisissez la région la plus proche (ex: Europe West)
4. **Prix**: Gratuit (Free Tier)

### Étape 3: Attendre le déploiement
- Le projet prend 1-2 minutes pour se déployer
- Vous recevrez les clés de configuration

---

## 🔧 Configuration de la base de données

### Informations de connexion Supabase
Une fois le projet créé, notez ces informations :

```
🔑 Project URL: https://xxxxxxxx.supabase.co
🗄️ Database URL: postgresql://postgres:[PASSWORD]@db.xxxxxxxx.supabase.co:5432/postgres
🔐 Anon Key: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
🔐 Service Role Key: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

### Structure de la base de données
Notre projet AgroConnect utilise ces tables :

#### 📦 Products
```sql
CREATE TABLE products_product (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    category VARCHAR(50),
    price DECIMAL(10, 2),
    quantity INTEGER,
    image VARCHAR(255),
    farmer_id INTEGER REFERENCES users_user(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### 🛒 Orders
```sql
CREATE TABLE products_order (
    id SERIAL PRIMARY KEY,
    product_id INTEGER REFERENCES products_product(id),
    quantity INTEGER,
    buyer_id INTEGER REFERENCES users_user(id),
    status VARCHAR(50) DEFAULT 'pending',
    image VARCHAR(255),
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### 🛗 Cart
```sql
CREATE TABLE products_cart (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users_user(id),
    product_id INTEGER REFERENCES products_product(id),
    quantity INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### 💬 Messages
```sql
CREATE TABLE products_message (
    id SERIAL PRIMARY KEY,
    sender_id INTEGER REFERENCES users_user(id),
    receiver_id INTEGER REFERENCES users_user(id),
    content TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### 💡 Agricultural Advice
```sql
CREATE TABLE products_agriculturaladvice (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT,
    advice_type VARCHAR(50),
    crop_type VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### 🌾 Cultures
```sql
CREATE TABLE products_culture (
    id SERIAL PRIMARY KEY,
    farmer_id INTEGER REFERENCES users_user(id),
    name VARCHAR(255),
    description TEXT,
    crop_type VARCHAR(50),
    planting_date DATE,
    expected_harvest DATE,
    area DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### 👥 Users
```sql
CREATE TABLE users_user (
    id SERIAL PRIMARY KEY,
    username VARCHAR(150) UNIQUE NOT NULL,
    email VARCHAR(254) UNIQUE NOT NULL,
    password VARCHAR(128) NOT NULL,
    role VARCHAR(50) DEFAULT 'buyer',
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    phone VARCHAR(20),
    address TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    date_joined TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 📤 Migration des données

### Option 1: Via Supabase SQL Editor
1. Allez dans votre projet Supabase
2. Cliquez sur "SQL Editor"
3. Exécutez les scripts SQL ci-dessus

### Option 2: Via Django Migrations
```bash
# Installer psycopg2
pip install psycopg2-binary

# Exécuter les migrations
python manage.py migrate
```

---

## ⚙️ Configuration Django

### 1. Installer les dépendances
```bash
pip install psycopg2-binary python-decouple
```

### 2. Mettre à jour settings.py
```python
import os
from decouple import config

# Configuration Supabase
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME', default='postgres'),
        'USER': config('DB_USER', default='postgres'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST', default='db.xxxxxxxx.supabase.co'),
        'PORT': config('DB_PORT', default='5432'),
        'OPTIONS': {
            'sslmode': 'require',
        },
    }
}
```

### 3. Créer le fichier .env
```env
# Supabase Configuration
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=votre_mot_de_passe_supabase
DB_HOST=db.xxxxxxxx.supabase.co
DB_PORT=5432

# Django Configuration
SECRET_KEY=votre_secret_key_django
DEBUG=False
ALLOWED_HOSTS=votre_domaine,www.votre_domaine,localhost,127.0.0.1
```

---

## 🔐 Variables d'environnement

### Créer le fichier .env
```bash
# Dans le dossier AgroConnectBackend
touch .env
```

### Contenu du fichier .env
```env
# Supabase Database
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=votre_mot_de_passe_supabase
DB_HOST=db.votre_projet_id.supabase.co
DB_PORT=5432

# Django Settings
SECRET_KEY=django-insecure-votre-secret-key-unique
DEBUG=False
ALLOWED_HOSTS=agroconnect.herokuapp.com,www.agroconnect.herokuapp.com,localhost,127.0.0.1

# Supabase API Keys (pour le futur)
SUPABASE_URL=https://votre_projet_id.supabase.co
SUPABASE_ANON_KEY=votre_anon_key
SUPABASE_SERVICE_KEY=votre_service_role_key
```

---

## 🧪 Test de connexion

### 1. Script de test
Créez `test_supabase_connection.py`:

```python
import os
import django
from decouple import config

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.db import connection

def test_supabase_connection():
    """Tester la connexion à Supabase"""
    try:
        # Test de connexion
        with connection.cursor() as cursor:
            cursor.execute("SELECT version();")
            db_version = cursor.fetchone()
            print("✅ Connexion à Supabase réussie!")
            print(f"📊 Version PostgreSQL: {db_version[0]}")
            
            # Test des tables
            cursor.execute("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public'
                ORDER BY table_name;
            """)
            tables = cursor.fetchall()
            print(f"📋 Tables trouvées: {len(tables)}")
            for table in tables:
                print(f"   - {table[0]}")
                
        return True
        
    except Exception as e:
        print(f"❌ Erreur de connexion: {e}")
        return False

if __name__ == '__main__':
    test_supabase_connection()
```

### 2. Exécuter le test
```bash
python test_supabase_connection.py
```

---

## 🚀 Déploiement

### 1. Mettre à jour requirements.txt
```txt
Django==4.2.7
djangorestframework==3.14.0
django-cors-headers==4.3.1
djangofilters==23.2
drf-yasg==1.21.7
psycopg2-binary==2.9.7
python-decouple==3.8
Pillow==10.0.1
django-filter==23.2
```

### 2. Pousser sur Heroku (optionnel)
```bash
# Installer Heroku CLI
heroku login

# Créer l'application
heroku create agroconnect-backend

# Configurer les variables d'environnement
heroku config:set DB_NAME=postgres
heroku config:set DB_USER=postgres
heroku config:set DB_PASSWORD=votre_mot_de_passe
heroku config:set DB_HOST=db.votre_projet_id.supabase.co
heroku config:set DB_PORT=5432

# Déployer
git push heroku main
```

---

## 📊 Monitoring Supabase

### Tableau de bord Supabase
1. **Database**: Voir les tables et les requêtes
2. **Authentication**: Gestion des utilisateurs (pour le futur)
3. **Storage**: Fichiers et images
4. **Functions**: Fonctions SQL personnalisées

### Métriques importantes
- 📈 **Connexions actives**: Nombre de connexions simultanées
- 💾 **Stockage utilisé**: Espace de la base de données
- ⚡ **Performance**: Temps de réponse des requêtes
- 🔒 **Sécurité**: Logs d'accès et erreurs

---

## 🔧 Dépannage

### Problèmes courants

#### 1. Erreur SSL
```
Error: connection to server at "db.xxx.supabase.co", port 5432 failed: SSL error
```
**Solution**: Assurez-vous que `sslmode='require'` est dans les options de la base de données.

#### 2. Timeout de connexion
```
Error: connection to server timed out
```
**Solution**: Vérifiez votre connexion internet et les identifiants Supabase.

#### 3. Permission refusée
```
Error: permission denied for table products_product
```
**Solution**: Exécutez les migrations Django pour créer les tables.

---

## 📝 Checklist finale

- [ ] ✅ Projet Supabase créé
- [ ] ✅ Base de données configurée
- [ ] ✅ Tables créées
- [ ] ✅ Django configuré
- [ ] ✅ Variables d'environnement définies
- [ ] ✅ Connexion testée
- [ ] ✅ Migrations exécutées
- [ ] ✅ Application déployée

---

## 🎯 Prochaines étapes

1. **Synchroniser les données**: Migrer les données existantes
2. **Backup régulier**: Configurer les sauvegardes automatiques
3. **Monitoring**: Mettre en place les alertes de performance
4. **Sécurité**: Configurer les RLS (Row Level Security)
5. **Scaling**: Optimiser pour la production

---

*🗄️ Supabase offre une solution PostgreSQL robuste et scalable pour AgroConnect*
