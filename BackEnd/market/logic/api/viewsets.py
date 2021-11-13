from rest_framework import viewsets
from .serializers import CategorySerializer, OrderSerializer, StockSerializer, UserSerializer
from django.contrib.auth.models import User
from ..models import Order, ProductCategory, Stock
import datetime

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = CategorySerializer
    
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class StockViewSet(viewsets.ModelViewSet):
    now = datetime.datetime.now()
    queryset = Stock.objects.filter(published=False, publication_date__lte=now)
    serializer_class = StockSerializer