from rest_framework import serializers
from .models import Product, Order
from django.contrib.auth import get_user_model

User = get_user_model()


# =====================================
# USER SERIALIZER (POUR FARMERS)
# =====================================
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']


# =====================================
# PRODUCT
# =====================================
class ProductSerializer(serializers.ModelSerializer):
    farmer = serializers.StringRelatedField(read_only=True)
    image = serializers.ImageField(required=False)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'quantity', 'image', 'farmer']


# =====================================
# ORDER
# =====================================
class OrderSerializer(serializers.ModelSerializer):
    buyer = serializers.StringRelatedField(read_only=True)
    product = ProductSerializer(read_only=True)

    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        write_only=True,
        source='product'
    )

    image = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'product', 'product_id', 'quantity', 'buyer', 'status', 'image']

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None