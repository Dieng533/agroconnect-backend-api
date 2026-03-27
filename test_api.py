#!/usr/bin/env python
"""
Script de test de l'API AgroConnect avec Supabase
"""

import requests
import json

def test_api_endpoints():
    """Tester les endpoints de l'API AgroConnect"""
    base_url = "http://127.0.0.1:8000/api"
    
    print("🌾 TEST DES ENDPOINTS API AGROCONNECT")
    print("=" * 50)
    
    # Test 1: Connexion pour obtenir le token
    print("\n🔐 Test 1: Connexion")
    login_data = {
        "username": "admin",
        "password": "admin123"
    }
    
    try:
        response = requests.post(f"{base_url}/token/", json=login_data)
        if response.status_code == 200:
            token_data = response.json()
            access_token = token_data.get("access")
            print(f"✅ Connexion réussie! Token obtenu.")
            
            # Test 2: Accès aux produits avec token
            print("\n📦 Test 2: Liste des produits")
            headers = {
                "Authorization": f"Bearer {access_token}",
                "Content-Type": "application/json"
            }
            
            products_response = requests.get(f"{base_url}/products/", headers=headers)
            if products_response.status_code == 200:
                products = products_response.json()
                print(f"✅ {len(products)} produits trouvés")
                if products:
                    print(f"   Premier produit: {products[0].get('name', 'N/A')}")
            else:
                print("   Aucun produit dans la base")
        else:
            print(f"❌ Erreur produits: {products_response.status_code}")
            
            # Test 3: Création d'un produit
            print("\n📦 Test 3: Création d'un produit")
            product_data = {
                "name": "Test Product API",
                "description": "Produit de test créé via API",
                "category": "cereals",
                "price": "1500.00",
                "quantity": 10
            }
            
            create_response = requests.post(f"{base_url}/products/", json=product_data, headers=headers)
            if create_response.status_code == 201:
                print("✅ Produit créé avec succès!")
                created_product = create_response.json()
                print(f"   ID: {created_product.get('id')}")
                print(f"   Nom: {created_product.get('name')}")
            else:
                print(f"❌ Erreur création: {create_response.status_code}")
                print(f"   Détail: {create_response.text}")
            
        else:
            print(f"❌ Erreur connexion: {response.status_code}")
            print(f"   Détail: {response.text}")
            
    except Exception as e:
        print(f"❌ Erreur lors des tests: {e}")
    
    print("\n" + "=" * 50)
    print("🎯 Tests terminés!")
    print("\n📱 URLs testées:")
    print(f"   🔐 Login: {base_url}/token/")
    print(f"   📦 Produits: {base_url}/products/")

if __name__ == "__main__":
    test_api_endpoints()
