from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    model = get_user_model()
    permission_classes = []
    serializer_class = UserSerializer