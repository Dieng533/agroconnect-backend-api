# 🚀 Instructions Supabase pour AgroConnect

## 📋 Étapes à suivre

### 1️⃣ **Connexion à Supabase**
1. Allez sur [https://supabase.com](https://supabase.com)
2. Connectez-vous avec votre compte
3. Sélectionnez votre projet `ugbmqxlrgwxihlgmcuuj`

### 2️⃣ **Exécuter le script SQL**
1. Dans le dashboard Supabase, cliquez sur **"SQL Editor"**
2. Copiez tout le contenu du fichier `create_supabase_tables.sql`
3. Collez dans l'éditeur SQL
4. Cliquez sur **"RUN"** pour exécuter

### 3️⃣ **Vérifier la création**
Après exécution, vous devriez voir :
```
✅ Toutes les tables AgroConnect créées avec succès!
```

### 4️⃣ **Configurer les variables d'environnement**
Créez/modifiez le fichier `.env` dans le dossier backend :

```env
# Configuration Supabase
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=AGOCONECT@12345678
DB_HOST=db.ugbmqxlrgwxihlgmcuuj.supabase.co
DB_PORT=5432

# Django Configuration
SECRET_KEY=django-insecure-change-this-in-production
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1,agroconnect.herokuapp.com
```

### 5️⃣ **Installer les dépendances**
```bash
pip install psycopg2-binary python-decouple
```

### 6️⃣ **Tester la connexion**
```bash
python test_supabase_connection.py
```

### 7️⃣ **Démarrer l'application**
```bash
python manage.py runserver
```

---

## 🔍 **Vérification dans Supabase**

### Tables créées :
- ✅ `users_user` - Utilisateurs
- ✅ `products_product` - Produits
- ✅ `products_order` - Commandes
- ✅ `products_cart` - Panier
- ✅ `products_message` - Messages
- ✅ `products_agriculturaladvice` - Conseils
- ✅ `products_culture` - Cultures

### Admin par défaut :
- 👤 **Username**: admin
- 🔑 **Password**: admin123
- 📧 **Email**: admin@agroconnect.local

---

## 🛠️ **Dépannage**

### Si erreur "relation does not exist" :
1. Vérifiez que le script SQL a été exécuté
2. Allez dans "Table Editor" dans Supabase
3. Vérifiez que les tables existent

### Si erreur de connexion :
1. Vérifiez les identifiants dans `.env`
2. Assurez-vous que le projet Supabase est actif
3. Testez avec `python test_supabase_connection.py`

### Si erreur de permissions :
1. Vérifiez les politiques RLS dans Supabase
2. Désactivez temporairement RLS pour tester
3. Réactivez RLS après tests

---

## 📊 **Monitoring Supabase**

### Dans le dashboard Supabase :
- 📈 **Database** : Requêtes et performance
- 👥 **Authentication** : Connexions utilisateurs
- 📁 **Storage** : Fichiers uploadés
- 🔔 **Functions** : Fonctions SQL personnalisées

---

## 🎯 **Prochaines étapes**

1. ✅ **Exécuter le script SQL** dans Supabase
2. ✅ **Configurer le fichier .env**
3. ✅ **Tester la connexion**
4. ✅ **Démarrer le serveur Django**
5. ✅ **Tester l'API Flutter**

---

## 📞 **Support**

- 📧 **Email Supabase** : support@supabase.com
- 📚 **Documentation** : https://supabase.com/docs
- 🌐 **Status** : https://status.supabase.com

---

*🗄️ Une fois ces étapes terminées, AgroConnect sera connecté à Supabase !*
