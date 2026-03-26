# 🌾 Documentation Administration AgroConnect

## 📋 Table des matières

1. [Accès à l'administration](#accès-à-ladministration)
2. [Tableau de bord](#tableau-de-bord)
3. [Gestion des produits](#gestion-des-produits)
4. [Gestion des commandes](#gestion-des-commandes)
5. [Gestion des utilisateurs](#gestion-des-utilisateurs)
6. [Gestion des messages](#gestion-des-messages)
7. [Gestion des conseils agricoles](#gestion-des-conseils-agricoles)
8. [Fonctionnalités avancées](#fonctionnalités-avancées)

---

## 🔐 Accès à l'administration

### Identifiants par défaut
```
📧 Email: admin@agroconnect.local
👤 Username: admin
🔑 Password: admin123
```

### URLs d'accès
- **Administration standard**: `http://127.0.0.1:8000/admin/`
- **Tableau de bord personnalisé**: `http://127.0.0.1:8000/admin/dashboard/`
- **Login personnalisé**: `http://127.0.0.1:8000/admin/login/`

---

## 📊 Tableau de bord

### Statistiques en temps réel
- **📦 Produits**: Nombre total de produits actifs
- **🛒 Commandes**: Statut des commandes en cours
- **👥 Utilisateurs**: Total des utilisateurs inscrits
- **💡 Conseils**: Nombre de conseils agricoles publiés

### Activités récentes
- **Nouveaux produits** (7 derniers jours)
- **Nouvelles commandes** (7 derniers jours)
- **Messages récents** (7 derniers jours)

### Actions rapides
- ➕ Ajouter un produit
- ➕ Ajouter un conseil agricole
- ➕ Ajouter un utilisateur
- 📋 Voir tous les produits

### Graphiques analytiques
- 📈 Évolution des ventes mensuelles
- 🥧 Répartition des produits par catégorie

---

## 📦 Gestion des produits

### Fonctionnalités
- ✅ **CRUD complet**: Créer, Lire, Mettre à jour, Supprimer
- 🔍 **Recherche avancée**: Par nom, description, agriculteur
- 🏷️ **Filtrage**: Par catégorie et date de création
- 📸 **Gestion des images**: Upload et affichage

### Champs disponibles
- **Nom**: Titre du produit
- **Description**: Détails complets
- **Catégorie**: Céréales, Légumes, Fruits, Tubercules
- **Prix**: En FCFA
- **Quantité**: Stock disponible
- **Image**: Photo du produit
- **Agriculteur**: Propriétaire

### Actions administratives
- ✏️ Modifier les informations
- 🗑️ Supprimer un produit
- 👁️ Voir les détails complets

---

## 🛒 Gestion des commandes

### Statuts des commandes
- 🟡 **Pending**: En attente de validation
- 🟢 **Confirmed**: Commande confirmée
- 🔵 **Processing**: En préparation
- 🚚 **Shipped**: Expédiée
- ✅ **Delivered**: Livrée
- ❌ **Cancelled**: Annulée

### Informations gérées
- **ID commande**: Référence unique
- **Acheteur**: Utilisateur concerné
- **Produit**: Article commandé
- **Quantité**: Nombre d'unités
- **Date de commande**: Timestamp
- **Statut**: État actuel
- **Image**: Preuve de commande

### Fonctionnalités
- 🔄 **Mise à jour du statut**
- 📊 **Filtrage par statut**
- 🔍 **Recherche par acheteur**
- 📅 **Tri par date**

---

## 👥 Gestion des utilisateurs

### Types d'utilisateurs
- **Admin**: Accès complet à l'administration
- **Farmer**: Vendeur de produits
- **Buyer**: Acheteur de produits

### Actions disponibles
- 👤 **Création de nouveaux utilisateurs**
- ✏️ **Modification des profils**
- 🗑️ **Suppression de comptes**
- 🔒 **Gestion des permissions**

---

## 💬 Gestion des messages

### Fonctionnalités
- 📨 **Visualisation des conversations**
- 🔍 **Recherche par expéditeur/destinataire**
- 📅 **Tri par date**
- 👁️ **Aperçu du contenu** (50 premiers caractères)

### Informations affichées
- **Expéditeur**: Utilisateur qui envoie
- **Destinataire**: Utilisateur qui reçoit
- **Contenu**: Message complet
- **Timestamp**: Date et heure

---

## 💡 Gestion des conseils agricoles

### Types de conseils
- 🌱 **Plantation**: Techniques de semis
- 🧪 **Fertilisation**: Engrais et nutriments
- 🌾 **Récolte**: Périodes et méthodes
- 🐛 **Protection**: Lutte contre les ravageurs
- 💧 **Irrigation**: Gestion de l'eau

### Types de cultures
- **Céréales**: Riz, Maïs, Mil, Sorgho
- **Légumes**: Tomates, Oignons, Haricots
- **Fruits**: Mangues, Bananes, Oranges
- **Tubercules**: Pommes de terre, Ignames

### Fonctionnalités
- ➕ **Création de nouveaux conseils**
- ✏️ **Modification du contenu**
- 🏷️ **Catégorisation par type**
- 🔍 **Recherche par titre/contenu**

---

## 🎨 Personnalisation de l'interface

### Thème AgroConnect
- 🎨 **Couleurs**: Vert principal (#1B8E3E)
- 🖼️ **Logo**: Intégré dans l'en-tête
- 📱 **Design responsive**: Compatible mobile/desktop
- 🌟 **Animations**: Effets de transition modernes

### Navigation
- 📊 **Tableau de bord**: Vue d'ensemble
- 📦 **Produits**: Gestion catalogue
- 🛒 **Commandes**: Suivi des ventes
- 💬 **Messages**: Communication
- 💡 **Conseils**: Contenu agricole
- 👥 **Utilisateurs**: Gestion comptes

---

## 🔧 Configuration technique

### Architecture
- **Framework**: Django 4.x
- **Base de données**: SQLite (développement) / PostgreSQL (production)
- **Templates**: Bootstrap 5 + CSS personnalisé
- **Charts**: Chart.js pour les graphiques

### Sécurité
- 🔐 **Authentification**: Django Admin
- 🛡️ **Permissions**: Basées sur les rôles
- 🚫 **Protection**: CSRF et XSS
- 📝 **Logs**: Traçabilité des actions

### Performance
- ⚡ **Optimisation**: Requêtes efficaces
- 📊 **Pagination**: Grandes listes
- 🗄️ **Indexation**: Champs de recherche
- 🔄 **Cache**: Templates statiques

---

## 📱 Accès mobile

L'interface d'administration est **responsive** et fonctionne sur :
- 📱 **Smartphones** (iOS/Android)
- 📋 **Tablettes** (iPad/Android)
- 💻 **Ordinateurs** (Windows/Mac/Linux)

---

## 🔍 Fonctionnalités de recherche

### Recherche globale
- 🔍 **Texte libre**: Dans tous les champs
- 🏷️ **Filtres**: Par catégorie, date, statut
- 📊 **Tri**: Chronologique, alphabétique
- 📄 **Pagination**: Navigation efficace

### Filtres avancés
- 📅 **Plages de dates**
- 🏷️ **Catégories multiples**
- 📊 **Statuts combinés**
- 👥 **Utilisateurs spécifiques**

---

## 📈 Rapports et statistiques

### Tableau de bord
- 📊 **Graphiques dynamiques**
- 📈 **Tendances mensuelles**
- 🥧 **Répartitions**
- 📋 **Listes détaillées**

### Export de données
- 📄 **CSV**: Compatible Excel
- 📊 **PDF**: Rapports imprimables
- 🔄 **JSON**: Intégration API

---

## 🚀 Déploiement

### Environnement de développement
```bash
# Démarrer le serveur
python manage.py runserver

# Accéder à l'admin
http://127.0.0.1:8000/admin/
```

### Environnement de production
- 🌐 **HTTPS**: Sécurisation des connexions
- 🗄️ **PostgreSQL**: Base de données robuste
- 📊 **Monitoring**: Surveillance des performances
- 🔄 **Backups**: Sauvegarde automatique

---

## 🆘 Support et maintenance

### Actions courantes
- 👤 **Créer superutilisateur**: `python create_superuser.py`
- 🗄️ **Migrations**: `python manage.py migrate`
- 📊 **Collecte static**: `python manage.py collectstatic`
- 🔄 **Redémarrer serveur**: `python manage.py runserver`

### Dépannage
- 🔍 **Logs Django**: `django-admin.log`
- 🗄️ **Base de données**: `db.sqlite3`
- 📁 **Media files**: `media/`
- 🎨 **Templates**: `templates/admin/`

---

## 📞 Contact

Pour toute question sur l'administration AgroConnect :
- 📧 **Email**: admin@agroconnect.local
- 🌐 **Documentation**: `/admin/docs/`
- 📱 **Support**: 24/7 pour les admins

---

## 🔄 Mises à jour

L'administration AgroConnect évolue régulièrement :
- ✨ **Nouvelles fonctionnalités**
- 🐛 **Corrections de bugs**
- 🎨 **Améliorations UX**
- 🔒 **Mises à jour sécurité**

---

*🌾 AgroConnect - Administration moderne et intuitive*
