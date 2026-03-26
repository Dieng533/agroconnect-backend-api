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
    buyer_phone = serializers.CharField(source='buyer.phone', read_only=True)
    buyer_id = serializers.IntegerField(source='buyer.id', read_only=True)
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_price = serializers.DecimalField(source='product.price', read_only=True, max_digits=10, decimal_places=2)
    product_image = serializers.SerializerMethodField()
    total = serializers.SerializerMethodField()

    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        write_only=True,
        source='product'
    )

    image = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'product', 'product_id', 'product_name', 'product_price', 'product_image', 'quantity', 'buyer', 'buyer_phone', 'buyer_id', 'status', 'image', 'total']

    def get_product_image(self, obj):
        request = self.context.get('request')
        if obj.product and obj.product.image:
            return request.build_absolute_uri(obj.product.image.url)
        return None

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.product and obj.product.image:
            return request.build_absolute_uri(obj.product.image.url)
        return None

    def get_total(self, obj):
        if obj.product:
            return obj.product.price * obj.quantity
        return 0


# =====================================
# MESSAGE
# =====================================
class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    receiver = UserSerializer(read_only=True)
    receiver_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver', 'receiver_id', 'content', 'timestamp', 'is_read']
        read_only_fields = ['timestamp', 'is_read', 'sender']

    def validate_receiver_id(self, value):
        """Vérifie que le receiver existe et n'est pas soi-même"""
        if not User.objects.filter(id=value).exists():
            raise serializers.ValidationError("L'utilisateur destinataire n'existe pas")
        
        # Vérifier qu'on ne s'envoie pas de message à soi-même
        request = self.context.get('request')
        if request and request.user.id == value:
            raise serializers.ValidationError("Vous ne pouvez pas vous envoyer de message à vous-même")
        
        return value

    def create(self, validated_data):
        # Le sender est automatiquement l'utilisateur authentifié
        validated_data['sender'] = self.context['request'].user
        return super().create(validated_data)


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