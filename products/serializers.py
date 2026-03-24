from rest_framework import serializers
from .models import Product, Order, Cart, Message, Culture, AgriculturalAdvice
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
    category_display = serializers.CharField(source='get_category_display', read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'quantity', 'image', 'category', 'category_display', 'location', 'farmer', 'created_at', 'updated_at']


# =====================================
# CART
# =====================================
class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        write_only=True,
        source='product'
    )
    total_price = serializers.ReadOnlyField()

    class Meta:
        model = Cart
        fields = ['id', 'product', 'product_id', 'quantity', 'total_price', 'created_at']


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


# =====================================
# MESSAGE
# =====================================
class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    receiver = UserSerializer(read_only=True)
    sender_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        write_only=True,
        source='sender'
    )
    receiver_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        write_only=True,
        source='receiver'
    )

    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver', 'sender_id', 'receiver_id', 'content', 'timestamp', 'is_read']
        read_only_fields = ['timestamp', 'is_read']


# =====================================
# CULTURE
# =====================================
class CultureSerializer(serializers.ModelSerializer):
    farmer = UserSerializer(read_only=True)
    crop_type_display = serializers.CharField(source='get_crop_type_display', read_only=True)

    class Meta:
        model = Culture
        fields = ['id', 'farmer', 'name', 'description', 'crop_type', 'crop_type_display', 'planting_date', 'expected_harvest', 'area', 'created_at']


# =====================================
# AGRICULTURAL ADVICE
# =====================================
class AgriculturalAdviceSerializer(serializers.ModelSerializer):
    advice_type_display = serializers.CharField(source='get_advice_type_display', read_only=True)
    crop_type_display = serializers.CharField(source='get_crop_type_display', read_only=True)

    class Meta:
        model = AgriculturalAdvice
        fields = ['id', 'title', 'content', 'advice_type', 'advice_type_display', 'crop_type', 'crop_type_display', 'created_at', 'is_active']
        read_only_fields = ['created_at']