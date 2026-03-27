# 🚀 Déploiement Render + Supabase pour AgroConnect

## 📋 Table des matières

1. [Configuration Render](#configuration-render)
2. [Préparation du code](#préparation-du-code)
3. [Déploiement](#déploiement)
4. [Configuration DNS](#configuration-dns)
5. [Monitoring](#monitoring)
6. [Dépannage](#dépannage)

---

## 🌐 Configuration Render

### 1. Création du compte Render
1. Allez sur [https://render.com](https://render.com)
2. Créez un compte (GitHub/Google/Email)
3. Vérifiez votre email pour activer le compte

### 2. Création du Web Service
1. Cliquez sur **"New +"**
2. Choisissez **"Web Service"**
3. Configuration du service :
   - **Name**: `agroconnect-backend`
   - **Region**: Choisissez la plus proche
   - **Branch**: `main`
   - **Root Directory**: `/`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn config.wsgi:application --bind 0.0.0.0:$PORT`

---

## 📦 Préparation du code

### 1. Créer le fichier render.yaml
Créez le fichier `render.yaml` à la racine du projet :

```yaml
services:
  # Service API Django
  - type: web
    name: agroconnect-backend
    env: python
    repo: https://github.com/VOTRE_USERNAME/agroconnect-backend.git
    rootDir: /
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn config.wsgi:application --bind 0.0.0.0:$PORT
    envVars:
      - key: DATABASE_URL
        value: postgresql://postgres:[VOTRE_PASSWORD]@db.ugbmqxlrgwxihlgmcuuj.supabase.co:5432/postgres
      - key: SECRET_KEY
        value: django-insecure-agroconnect-production-key-2024
      - key: DEBUG
        value: false
      - key: ALLOWED_HOSTS
        value: agroconnect-backend.onrender.com,www.agroconnect-backend.onrender.com
      - key: CORS_ALLOWED_ORIGINS
        value: https://agroconnect-backend.onrender.com,https://agroconnect-gold.vercel.app
      - key: CORS_ALLOW_CREDENTIALS
        value: true
      - key: CORS_ALLOW_ALL_ORIGINS
        value: false
      - key: SUPABASE_URL
        value: https://ugbmqxlrgwxihlgmcuuj.supabase.co
      - key: SUPABASE_ANON_KEY
        value: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVnYm1xeGxyZ3d4aWhsZ21jdXVqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzQ2MDE4NDYsImV4cCI6MjA5MDE3Nzg0Nn0.EHZOjfLw67jx9OsqUfv-leqTW06V40_K5btFEHfeOF0
      - key: SUPABASE_SERVICE_KEY
        value: sb_publishable_oVGHcXWF0fjgormVxfPyWw_ci3ysgk3
```

### 2. Créer le fichier Procfile
Créez un fichier `Procfile` à la racine :

```procfile
web: gunicorn config.wsgi:application --bind 0.0.0.0:$PORT --workers 3
```

### 3. Mettre à jour requirements.txt
```txt
# Django Core
Django==4.2.7
djangorestframework==3.14.0
django-cors-headers==4.3.1
django-filter==23.2
django-decouple==3.8

# Database
psycopg2-binary==2.9.7

# API
drf-yasg==1.21.7
djangorestframework-simplejwt==5.3.0

# Image Processing
Pillow==10.0.1

# Production
gunicorn==21.2.0
whitenoise==6.6.0
```

---

## 🚀 Déploiement

### Option 1: Via GitHub (Recommandé)
1. **Pousser le code sur GitHub** :
   ```bash
   git init
   git add .
   git commit -m "Initial commit - AgroConnect Backend"
   git branch -M main
   git remote add origin https://github.com/VOTRE_USERNAME/agroconnect-backend.git
   git push -u origin main
   ```

2. **Connecter Render à GitHub** :
   - Dans Render → Services → Votre service
   - Cliquez sur **"Connect Repo"**
   - Autorisez Render à accéder à votre GitHub
   - Sélectionnez votre dépôt `agroconnect-backend`
   - Branche : `main`

3. **Déployer automatiquement** :
   - Render va détecter le `render.yaml`
   - Le déploiement commence automatiquement
   - Attendez 2-3 minutes pour le déploiement

### Option 2: Via CLI Render
1. **Installer Render CLI** :
   ```bash
   npm install -g @render/cli
   ```

2. **Se connecter** :
   ```bash
   render login
   ```

3. **Déployer** :
   ```bash
   render deploy
   ```

---

## 🌍 Configuration DNS

### 1. URL de production
Une fois déployé, votre API sera accessible à :
```
https://agroconnect-backend.onrender.com
```

### 2. Configuration du domaine personnalisé (optionnel)
1. Dans Render → Services → Votre service
2. Cliquez sur **"Custom Domains"**
3. Ajoutez votre domaine : `api.agroconnect.com`
4. Configurez les enregistrements DNS :
   ```
   Type: CNAME
   Name: api
   Value: agroconnect-backend.onrender.com
   TTL: 300
   ```

---

## 📊 Monitoring et Logs

### 1. Logs en temps réel
```bash
render logs agroconnect-backend
```

### 2. Métriques
- CPU et mémoire utilisés
- Nombre de requêtes par minute
- Temps de réponse moyen
- Erreurs 4xx/5xx

### 3. Alertes
Configurez les alertes pour :
- Erreurs 5xx
- Temps de réponse > 2 secondes
- Taux d'erreur > 5%

---

## 🔧 Configuration Production

### 1. Variables d'environnement critiques
```yaml
DATABASE_URL: postgresql://postgres:[PASSWORD]@db.ugbmqxlrgwxihlgmcuuj.supabase.co:5432/postgres
SECRET_KEY: django-insecure-agroconnect-production-key-2024
DEBUG: false
ALLOWED_HOSTS: agroconnect-backend.onrender.com,www.agroconnect-backend.onrender.com
```

### 2. Sécurité
- HTTPS obligatoire (automatique sur Render)
- WAF (Web Application Firewall) activé
- Headers de sécurité automatiques
- Isolation réseau

### 3. Performance
- Auto-scaling automatique
- CDN intégré
- Load balancing
- Health checks

---

## 📱 Configuration Flutter

### 1. Mettre à jour l'URL de l'API
Dans `lib/core/services/api_service.dart` :

```dart
// En développement
static const String baseUrl = 'http://127.0.0.1:8000/api';

// En production
static const String baseUrl = 'https://agroconnect-backend.onrender.com/api';
```

### 2. Configuration conditionnelle
```dart
import 'package:flutter/foundation.dart';

class ApiService {
  static String get baseUrl {
    if (kReleaseMode) {
      return 'https://agroconnect-backend.onrender.com/api';
    } else {
      return 'http://127.0.0.1:8000/api';
    }
  }
  
  // ... reste du code
}
```

---

## 🧪 Tests de production

### 1. Test de l'API
```bash
# Test de connexion
curl -X POST https://agroconnect-backend.onrender.com/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"admin123"}'

# Test des produits
curl -H "Authorization: Bearer VOTRE_TOKEN" \
  https://agroconnect-backend.onrender.com/api/products/
```

### 2. Test de l'application Flutter
1. Build en mode release :
   ```bash
   flutter build web --release
   ```
2. Testez l'application avec l'URL de production

---

## 🔄 Mises à jour

### 1. Déploiement automatique
```bash
git add .
git commit -m "Update: nouvelle fonctionnalité"
git push origin main
# Render déploie automatiquement
```

### 2. Rollback si nécessaire
1. Dans Render → Services → Votre service
2. Cliquez sur **"Deploy"**
3. Choisissez une version précédente
4. Confirmez le rollback

---

## 📝 Checklist de déploiement

- [ ] **Préparation**
  - [ ] GitHub repository créé
  - [ ] render.yaml configuré
  - [ ] Procfile créé
  - [ ] requirements.txt à jour
  - [ ] Variables d'environnement vérifiées

- [ ] **Déploiement**
  - [ ] Code poussé sur GitHub
  - [ ] Render connecté au repo
  - [ ] Service déployé
  - [ ] URL de production accessible

- [ ] **Post-déploiement**
  - [ ] API testée
  - [ ] Base de données connectée
  - [ ] Logs vérifiés
  - [ ] Monitoring configuré
  - [ ] Flutter mis à jour

---

## 🚨 Dépannage courant

### Erreur "Build failed"
1. Vérifiez `requirements.txt`
2. Vérifiez `render.yaml`
3. Consultez les logs de build

### Erreur "Database connection failed"
1. Vérifiez `DATABASE_URL`
2. Vérifiez les identifiants Supabase
3. Testez la connexion manuellement

### Erreur "502 Bad Gateway"
1. Attendez la fin du déploiement
2. Vérifiez les health checks
3. Redémarrez le service

---

## 📞 Support Render

### Documentation
- 📚 [Render Docs](https://render.com/docs)
- 🎥 [Render YouTube](https://youtube.com/c/Render)
- 💬 [Render Community](https://community.render.com)

### Support
- 📧 [Email Support](mailto:support@render.com)
- 🐛 [Issue Tracker](https://github.com/render-inc/render)
- 💬 [Discord Community](https://discord.gg/render)

---

## 🎯 URLs de production

### Services
- 🌐 **API Backend** : `https://agroconnect-backend.onrender.com`
- 📊 **Dashboard Render** : `https://dashboard.render.com`
- 📋 **Swagger** : `https://agroconnect-backend.onrender.com/swagger/`
- 🏛️ **Admin Django** : `https://agroconnect-backend.onrender.com/admin/`

### Endpoints API
- 🔐 **Authentification** : `/api/token/`
- 📦 **Produits** : `/api/products/`
- 🛒 **Commandes** : `/api/orders/`
- 💬 **Messages** : `/api/messages/`
- 👥 **Utilisateurs** : `/api/users/`
- 💡 **Conseils** : `/api/advice/`
- 🌾 **Cultures** : `/api/cultures/`

---

## 🔄 Workflow de développement

### 1. Développement local
```bash
# Base de données locale
python manage.py runserver

# Tests
python test_api.py
```

### 2. Tests de staging
```bash
# Déployer sur branche de test
git checkout staging
git push origin staging
```

### 3. Production
```bash
# Fusionner et déployer
git checkout main
git merge staging
git push origin main
```

---

*🚀 AgroConnect prêt pour le déploiement sur Render avec Supabase !*
