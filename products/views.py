from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from django.db import transaction

from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


# ✅ Liste + Création produit
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Champs filtrables et recherchables
    filterset_fields = ['category', 'farmer']   # ex: catégorie, farmer
    search_fields = ['name', 'description']    # recherche par mot clé
    ordering_fields = ['price', 'created_at']  # tri par prix ou date
    

# ✅ Création commande
class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    @transaction.atomic
    def perform_create(self, serializer):
        user = self.request.user

        if user.user_type != 'buyer':
            raise PermissionDenied("Seuls les buyers peuvent passer une commande.")

        product = Product.objects.get(id=self.request.data.get('product'))
        quantity = int(self.request.data.get('quantity'))

        if quantity > product.quantity:
            raise PermissionDenied("Stock insuffisant.")

        product.quantity -= quantity
        product.save()

        total_price = product.price * quantity

        serializer.save(
            buyer=user,
            product=product,
            quantity=quantity,
            total_price=total_price
        )

class OrderUpdateStatusView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        order = self.get_object()

        if self.request.user != order.product.farmer:
            raise PermissionDenied("Seul le farmer peut modifier le statut.")

        serializer.save()