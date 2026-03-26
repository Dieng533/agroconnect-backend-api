# serializers.py
from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    role = serializers.ChoiceField(choices=[('buyer', 'Acheteur'), ('seller', 'Vendeur')])
    username = serializers.CharField(required=True)
    phone = serializers.CharField(required=True, max_length=20, error_messages={
        'required': 'Le numéro de téléphone est obligatoire',
        'blank': 'Le numéro de téléphone ne peut pas être vide'
    })

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone', 'password', 'role']

    def validate_phone(self, value):
        if not value or value.strip() == '':
            raise serializers.ValidationError('Le numéro de téléphone est obligatoire')
        return value.strip()

    def create(self, validated_data):
        role = validated_data.get('role')
        if role == 'admin':
            raise serializers.ValidationError(
                "La création d'un compte administrateur n'est pas autorisée."
            )

        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            username=validated_data['username'],
            phone=validated_data.get('phone', ''),
            role=role
        )
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    # Champ "name" pour Flutter
    name = serializers.CharField(source='username', read_only=True)

    class Meta:
        model = User
        # Assurez-vous que `name` est bien déclaré avant dans le serializer
        fields = ['id', 'name', 'username', 'email', 'phone', 'role']