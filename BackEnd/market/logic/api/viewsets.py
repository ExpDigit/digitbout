from django.http.response import Http404, HttpResponse
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import CategorySerializer, OrderSerializer, StockEditSerializer, StockSerializer, UserSerializer
from django.contrib.auth.models import User
from ..models import Order, ProductCategory, Stock
from rest_framework.response import Response
from rest_framework import status
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

class StockDetail(APIView):
    def get_object(self, pk):
        try:
            return Stock.objects.get(pk=pk)
        except Stock.DoesNotExist:
            raise Http404

    def get(self, requset):
        return Http404

    def put(self, request, format=None):
        stock = self.get_object(request.data['pk'])
        serializer = StockEditSerializer(stock, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)