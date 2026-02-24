from rest_framework import generics, permissions
from .serializers import RegisterSerializer, UserProfileSerializer
from .models import User


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.data.get('role') == 'seller':
            response.data['conseil'] = "Vérifiez vos informations avant de publier vos produits."
        return response


class ProfileView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user