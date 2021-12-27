from rest_framework import generics
from django.contrib.auth import get_user_model
from user.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer


class ShowUserView(generics.ListCreateAPIView):
    """Create a new user in the system"""
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
