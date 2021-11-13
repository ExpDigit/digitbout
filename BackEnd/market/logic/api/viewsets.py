from rest_framework import viewsets
from .serializers import CategorySerializer, UserSerializer
from django.contrib.auth.models import User
from ..models import ProductCategory

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = CategorySerializer