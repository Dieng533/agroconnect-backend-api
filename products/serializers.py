from rest_framework import serializers
from .models import Product, Order

class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    buyer = serializers.ReadOnlyField(source='buyer.username')
    total_price = serializers.ReadOnlyField()

    class Meta:
        model = Order
        fields = '__all__'