# 🚀 Déploiement Heroku + Supabase pour AgroConnect

## 📋 Prérequis

- ✅ Compte Heroku créé
- ✅ CLI Heroku installée
- ✅ Projet Supabase configuré
- ✅ Tables créées dans Supabase
- ✅ Fichier `.env` configuré

---

## 🛠️ Étapes de Déploiement

### 1️⃣ **Installation des dépendances**
```bash
pip install -r requirements.txt
```

### 2️⃣ **Configuration Heroku**
```bash
# Installation Heroku CLI
npm install -g heroku

# Connexion à Heroku
heroku login

# Création de l'application
heroku create agroconnect-backend

# Configuration des variables d'environnement
heroku config:set DB_NAME=postgres
heroku config:set DB_USER=postgres
heroku config:set DB_PASSWORD=AGOCONECT@12345678
heroku config:set DB_HOST=db.ugbmqxlrgwxihlgmcuuj.supabase.co
heroku config:set DB_PORT=5432
heroku config:set SECRET_KEY=django-insecure-agroconnect-production-key-2024
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS=agroconnect-backend.herokuapp.com,www.agroconnect-backend.herokuapp.com
```

### 3️⃣ **Configuration CORS pour Heroku**
```bash
heroku config:set CORS_ALLOWED_ORIGINS=https://agroconnect-backend.herokuapp.com,https://agroconnect-gold.vercel.app
heroku config:set CORS_ALLOW_CREDENTIALS=True
heroku config:set CORS_ALLOW_ALL_ORIGINS=False
```

### 4️⃣ **Configuration Supabase**
```bash
heroku config:set SUPABASE_URL=https://ugbmqxlrgwxihlgmcuuj.supabase.co
heroku config:set SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVnYm1xeGxyZ3d4aWhsZ21jdXVqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzQ2MDE4NDYsImV4cCI6MjA5MDE3Nzg0Nn0.EHZOjfLw67jx9OsqUfv-leqTW06V40_K5btFEHfeOF0
heroku config:set SUPABASE_SERVICE_KEY=sb_publishable_oVGHcXWF0fjgormVxfPyWw_ci3ysgk3
```

### 5️⃣ **Création du Procfile**
Créer un fichier `Procfile` à la racine :
```procfile
web: gunicorn config.wsgi:application --bind 0.0.0.0:$PORT --workers 3
```

### 6️⃣ **Initialisation Git**
```bash
git init
git add .
git commit -m "Initial commit - AgroConnect with Supabase"
heroku git:remote -a agroconnect-backend heroku
```

### 7️⃣ **Déploiement**
```bash
git push heroku main
```

---

## 🔧 Configuration Supplémentaire

### **Runtime.txt**
Créer un fichier `runtime.txt` :
```
python-3.11.0
```

### **Static Files**
```bash
# Collecter les fichiers statiques
heroku run python manage.py collectstatic --noinput

# Déployer les fichiers statiques
heroku run python manage.py collectstatic --noinput --clear
```

---

## 🧪 Tests de Déploiement

### **Vérifier les logs**
```bash
heroku logs --tail
```

### **Tester l'API**
```bash
# Test de connexion à la base
heroku run python test_supabase_connection.py

# Test des endpoints
curl https://agroconnect-backend.herokuapp.com/api/products/
```

### **Vérifier l'administration**
- URL : `https://agroconnect-backend.herokuapp.com/admin/`
- Username : admin
- Password : admin123

---

## 📊 Monitoring Heroku

### **Métriques importantes**
- 📈 **Performance** : Temps de réponse
- 💾 **Usage** : CPU et mémoire
- 📊 **Requêtes** : Nombre et erreurs
- 🔒 **Sécurité** : Logs d'accès

### **Commandes utiles**
```bash
# Statistiques de l'application
heroku ps

# Utilisation des ressources
heroku apps:info

# Redémarrer l'application
heroku restart

# Mise à jour des dépendances
heroku buildpacks
```

---

## 🔄 Mises à jour

### **Pour déployer des modifications**
```bash
git add .
git commit -m "Description des modifications"
git push heroku main
```

### **Rollback en cas de problème**
```bash
# Voir les déploiements précédents
heroku releases

# Revenir à une version précédente
heroku rollback v1
```

---

## 🚨 Dépannage

### **Erreurs courantes**

#### **Application Error H14**
```bash
# Vérifier les logs
heroku logs --tail

# Redémarrer les dynos
heroku restart
```

#### **Database Connection Error**
```bash
# Vérifier les variables d'environnement
heroku config

# Tester la connexion à Supabase
heroku run python test_supabase_connection.py
```

#### **Static Files Not Found**
```bash
# Forcer la collecte des fichiers statiques
heroku run python manage.py collectstatic --noinput --clear
```

---

## 📱 URLs de Production

### **API Endpoints**
- 🏠 **Base URL** : `https://agroconnect-backend.herokuapp.com`
- 📦 **Produits** : `/api/products/`
- 🛒 **Commandes** : `/api/orders/`
- 💬 **Messages** : `/api/messages/`
- 👥 **Utilisateurs** : `/api/users/`
- 🏛️ **Admin** : `/admin/`

### **Configuration Flutter**
Mettre à jour les URLs dans l'application Flutter :
```dart
// lib/core/services/api_service.dart
static const String baseUrl = 'https://agroconnect-backend.herokuapp.com/api';
```

---

## 🎯 Checklist de Déploiement

- [ ] ✅ Dépendances installées
- [ ] ✅ Variables Heroku configurées
- [ ] ✅ Procfile créé
- [ ] ✅ Runtime.txt configuré
- [ ] ✅ Git initialisé
- [ ] ✅ Déployé sur Heroku
- [ ] ✅ Base de données connectée
- [ ] ✅ API fonctionnelle
- [ ] ✅ Administration accessible

---

## 📞 Support

### **Heroku**
- 📧 **Documentation** : https://devcenter.heroku.com/
- 📊 **Dashboard** : https://dashboard.heroku.com/
- 🆘 **Support** : https://help.heroku.com/

### **Supabase**
- 📧 **Documentation** : https://supabase.com/docs
- 📊 **Dashboard** : https://app.supabase.com/
- 🆘 **Support** : https://support.supabase.com/

---

*🚀 AgroConnect prêt pour le déploiement Heroku + Supabase !*
