from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.db import models

from .models import Product, Order, Cart, Message, Culture, AgriculturalAdvice
from .serializers import ProductSerializer, OrderSerializer, UserSerializer, CartSerializer, MessageSerializer, CultureSerializer, AgriculturalAdviceSerializer

User = get_user_model()


# =====================================
# PRODUITS
# =====================================
class ProductListCreateView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Chaque vendeur voit uniquement SES produits
        if self.request.user.role == 'seller':
            return Product.objects.filter(farmer=self.request.user)
        # Les acheteurs voient tous les produits
        return Product.objects.all()

    def perform_create(self, serializer):
        # Produit automatiquement lie au vendeur connecte
        serializer.save(farmer=self.request.user)

    def get_serializer_context(self):
        # Essentiel pour construire l'URL complete des images
        return {'request': self.request}


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Empeche modification/suppression d'un autre vendeur
        if self.request.user.role == 'seller':
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
        if user.role == "seller":
            # Toutes les commandes des produits du farmer
            return Order.objects.filter(product__farmer=user)
        else:
            # Commandes passees par l'utilisateur (buyer)
            return Order.objects.filter(buyer=user)

    def perform_create(self, serializer):
        serializer.save(buyer=self.request.user)
        

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == "seller":
            return Order.objects.filter(product__farmer=user)
        else:
            return Order.objects.filter(buyer=user)

    def get_serializer_context(self):
        return {'request': self.request}


# =====================================
# PANIER (CART)
# =====================================
class CartListView(generics.ListCreateAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Ajouter ou mettre a jour un produit dans le panier
        product = serializer.validated_data['product']
        quantity = serializer.validated_data.get('quantity', 1)
        
        cart_item, created = Cart.objects.get_or_create(
            user=self.request.user,
            product=product,
            defaults={'quantity': quantity}
        )
        
        if not created:
            cart_item.quantity += quantity
            cart_item.save()

    def get_serializer_context(self):
        return {'request': self.request}


class CartDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def get_serializer_context(self):
        return {'request': self.request}


class CartClearView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        Cart.objects.filter(user=request.user).delete()
        return Response({'message': 'Panier vide avec succes'}, status=status.HTTP_204_NO_CONTENT)


# =====================================
# COMMANDES EN BULK
# =====================================
class BulkOrderCreateView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        items = request.data.get('items', [])
        orders = []
        
        for item in items:
            product_id = item.get('product_id')
            quantity = item.get('quantity', 1)
            
            try:
                product = Product.objects.get(id=product_id)
                if product.quantity >= quantity:
                    order = Order.objects.create(
                        product=product,
                        buyer=request.user,
                        quantity=quantity
                    )
                    product.quantity -= quantity
                    product.save()
                    orders.append(order)
            except Product.DoesNotExist:
                continue
        
        # Vider le panier apres commande
        Cart.objects.filter(user=request.user).delete()
        
        serializer = OrderSerializer(orders, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# =====================================
# LISTE DES FARMERS
# =====================================
class FarmerListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Tous les utilisateurs avec le role farmer
        return User.objects.filter(role='seller')

    def get_serializer_context(self):
        return {'request': self.request}


# =====================================
# MESSAGES
# =====================================
class MessageListView(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Un utilisateur ne voit que ses messages (envoyes ou recus)
        user = self.request.user
        return Message.objects.filter(
            models.Q(sender=user) | models.Q(receiver=user)
        ).distinct()

    def perform_create(self, serializer):
        # L'expediteur est automatiquement l'utilisateur connecte
        serializer.save(sender=self.request.user)


class MessageDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Message.objects.filter(
            models.Q(sender=user) | models.Q(receiver=user)
        )


class ConversationView(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        other_user_id = self.kwargs.get('user_id')
        
        # Messages entre l'utilisateur connecte et l'autre utilisateur
        return Message.objects.filter(
            (models.Q(sender=user) & models.Q(receiver_id=other_user_id)) |
            (models.Q(sender_id=other_user_id) & models.Q(receiver=user))
        ).order_by('timestamp')


# =====================================
# CULTURES
# =====================================
class CultureListCreateView(generics.ListCreateAPIView):
    serializer_class = CultureSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'seller':
            return Culture.objects.filter(farmer=user)
        return Culture.objects.all()  # Les acheteurs peuvent voir toutes les cultures

    def perform_create(self, serializer):
        serializer.save(farmer=self.request.user)


class CultureDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CultureSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'seller':
            return Culture.objects.filter(farmer=user)
        return Culture.objects.all()


# =====================================
# CONSEILS AGRICOLES
# =====================================
class AgriculturalAdviceListView(generics.ListAPIView):
    serializer_class = AgriculturalAdviceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = AgriculturalAdvice.objects.filter(is_active=True)
        
        # Filtrer par type de culture si specifie
        crop_type = self.request.query_params.get('crop_type')
        if crop_type:
            queryset = queryset.filter(crop_type=crop_type)
            
        # Filtrer par type de conseil si specifie
        advice_type = self.request.query_params.get('advice_type')
        if advice_type:
            queryset = queryset.filter(advice_type=advice_type)
            
        return queryset


class AgriculturalAdviceDetailView(generics.RetrieveAPIView):
    serializer_class = AgriculturalAdviceSerializer
    permission_classes = [IsAuthenticated]
    queryset = AgriculturalAdvice.objects.filter(is_active=True)
