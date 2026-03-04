from rest_framework import generics, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer, UserSerializer

User = get_user_model()


# =====================================
# PRODUITS
# =====================================
class ProductListCreateView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Chaque vendeur voit uniquement SES produits
        if self.request.user.role == 'farmer':
            return Product.objects.filter(farmer=self.request.user)
        # Les acheteurs voient tous les produits
        return Product.objects.all()

    def perform_create(self, serializer):
        # Produit automatiquement lié au vendeur connecté
        serializer.save(farmer=self.request.user)

    def get_serializer_context(self):
        # 🔹 Essentiel pour construire l'URL complète des images
        return {'request': self.request}


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Empêche modification/suppression d’un autre vendeur
        if self.request.user.role == 'farmer':
            return Product.objects.filter(farmer=self.request.user)
        # Les acheteurs ne peuvent pas modifier
        return Product.objects.none()

    def get_serializer_context(self):
        return {'request': self.request}


# =====================================
# COMMANDES
# =====================================
class OrderListCreateView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == "farmer":
            # Toutes les commandes des produits du farmer
            return Order.objects.filter(product__farmer=user)
        else:
            # Commandes passées par l'utilisateur (buyer)
            return Order.objects.filter(buyer=user)

    def perform_create(self, serializer):
        serializer.save(buyer=self.request.user)
        

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == "farmer":
            return Order.objects.filter(product__farmer=user)
        else:
            return Order.objects.filter(buyer=user)

    def get_serializer_context(self):
        return {'request': self.request}


# =====================================
# LISTE DES FARMERS
# =====================================
class FarmerListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Tous les utilisateurs avec le rôle farmer
        return User.objects.filter(role='seller')

    def get_serializer_context(self):
        return {'request': self.request}