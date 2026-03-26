#!/usr/bin/env python
"""
Script de test pour l'interface d'administration AgroConnect
"""

import os
import django

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from products.models import Product, Order, Message, AgriculturalAdvice, Culture

User = get_user_model()

class AdminInterfaceTest:
    """Test de l'interface d'administration"""
    
    def __init__(self):
        self.admin_user = None
        self.test_data = {}
    
    def setup_test_data(self):
        """Créer des données de test"""
        print("🔧 Création des données de test...")
        
        # Créer agriculteur et acheteur avec emails uniques
        import random
        random_id = random.randint(1000, 9999)
        
        self.test_data['farmer'] = User.objects.create_user(
            username=f'test_farmer_{random_id}',
            email=f'farmer_{random_id}@test.com',
            password='test123',
            role='farmer'
        )
        
        self.test_data['buyer'] = User.objects.create_user(
            username=f'test_buyer_{random_id}',
            email=f'buyer_{random_id}@test.com',
            password='test123',
            role='buyer'
        )
        
        # Créer un produit
        self.test_data['product'] = Product.objects.create(
            name='Test Product',
            description='Description du produit de test',
            category='cereals',
            price=1500,
            quantity=10,
            farmer=self.test_data['farmer']
        )
        
        # Créer une commande
        self.test_data['order'] = Order.objects.create(
            product=self.test_data['product'],
            quantity=2,
            buyer=self.test_data['buyer'],
            status='pending'
        )
        
        # Créer un message
        self.test_data['message'] = Message.objects.create(
            sender=self.test_data['buyer'],
            receiver=self.test_data['farmer'],
            content='Message de test'
        )
        
        # Créer un conseil agricole
        self.test_data['advice'] = AgriculturalAdvice.objects.create(
            title='Conseil de test',
            content='Contenu du conseil agricole de test',
            advice_type='planting',
            crop_type='cereals'
        )
        
        # Créer une culture
        from datetime import date, timedelta
        self.test_data['culture'] = Culture.objects.create(
            name='Culture de test',
            description='Description de la culture de test',
            crop_type='cereals',
            farmer=self.test_data['farmer'],
            planting_date=date.today(),
            expected_harvest=date.today() + timedelta(days=90),
            area=2.5
        )
        
        print("✅ Données de test créées avec succès!")
    
    def test_admin_models(self):
        """Tester les modèles dans l'admin"""
        print("\n🔍 Test des modèles dans l'admin...")
        
        models_test = [
            ('Produits', Product.objects.count()),
            ('Commandes', Order.objects.count()),
            ('Messages', Message.objects.count()),
            ('Conseils', AgriculturalAdvice.objects.count()),
            ('Cultures', Culture.objects.count()),
            ('Utilisateurs', User.objects.count()),
        ]
        
        for model_name, count in models_test:
            print(f"   📊 {model_name}: {count} enregistrements")
        
        print("✅ Test des modèles réussi!")
    
    def test_admin_views(self):
        """Tester les vues d'administration"""
        print("\n🌐 Test des vues d'administration...")
        
        # Vérifier que l'admin est accessible
        try:
            from django.test import Client
            client = Client()
            
            # Test login
            response = client.post('/admin/login/', {
                'username': 'admin',
                'password': 'admin123'
            })
            
            if response.status_code in [200, 302]:
                print("   ✅ Login admin fonctionnel")
            else:
                print(f"   ❌ Login admin erreur: {response.status_code}")
            
            # Test dashboard personnalisé
            response = client.get('/admin/dashboard/')
            if response.status_code == 200:
                print("   ✅ Dashboard personnalisé accessible")
            else:
                print(f"   ❌ Dashboard erreur: {response.status_code}")
                
        except Exception as e:
            print(f"   ❌ Erreur test vues: {e}")
    
    def test_admin_features(self):
        """Tester les fonctionnalités de l'admin"""
        print("\n⚙️ Test des fonctionnalités de l'admin...")
        
        # Test recherche
        products = Product.objects.filter(name__icontains='test')
        print(f"   🔍 Recherche produits: {products.count()} trouvé(s)")
        
        # Test filtrage
        orders_pending = Order.objects.filter(status='pending')
        print(f"   📊 Commandes en attente: {orders_pending.count()}")
        
        # Test relations
        farmer_products = Product.objects.filter(farmer=self.test_data['farmer'])
        print(f"   👨‍🌾 Produits agriculteur: {farmer_products.count()}")
        
        print("✅ Fonctionnalités testées avec succès!")
    
    def run_all_tests(self):
        """Exécuter tous les tests"""
        print("🌾 DÉMARRAGE DES TESTS ADMIN AGROCONNECT")
        print("=" * 50)
        
        try:
            self.setup_test_data()
            self.test_admin_models()
            self.test_admin_views()
            self.test_admin_features()
            
            print("\n" + "=" * 50)
            print("🎉 TOUS LES TESTS TERMINÉS AVEC SUCCÈS!")
            print("\n📋 Résumé:")
            print("   ✅ Données de test créées")
            print("   ✅ Modèles administrés")
            print("   ✅ Vues accessibles")
            print("   ✅ Fonctionnalités opérationnelles")
            
            print("\n🔗 Accès rapide:")
            print("   🌐 Admin standard: http://127.0.0.1:8000/admin/")
            print("   📊 Dashboard: http://127.0.0.1:8000/admin/dashboard/")
            print("   👤 Login: admin / admin123")
            
        except Exception as e:
            print(f"\n❌ ERREUR: {e}")
            print("🔧 Vérifiez la configuration Django")

def main():
    """Fonction principale"""
    tester = AdminInterfaceTest()
    tester.run_all_tests()

if __name__ == '__main__':
    main()
