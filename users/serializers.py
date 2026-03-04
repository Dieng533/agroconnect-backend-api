# serializers.py
from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    role = serializers.ChoiceField(choices=[('buyer', 'Acheteur'), ('seller', 'Vendeur')])
    username = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'role']

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
            role=role
        )
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    # 🔹 Champ "name" pour Flutter
    name = serializers.CharField(source='username', read_only=True)

    class Meta:
        model = User
        # Assurez-vous que `name` est bien déclaré avant dans le serializer
        fields = ['id', 'name', 'username', 'email', 'role']