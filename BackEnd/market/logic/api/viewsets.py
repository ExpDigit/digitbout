from django.http.response import Http404, HttpResponse
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import CategorySerializer, OrderSerializer, StockEditSerializer, StockSerializer, UserSerializer, BotDataSerializer
from django.contrib.auth.models import User
from ..models import BotData, Order, ProductCategory, Stock
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
    
# class BotDataViewSet(viewsets.ModelViewSet):
#     queryset = BotData.objects.all()
#     serializer_class = BotDataSerializer

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

class BotDataDetail(APIView):
    def get_object(self, pk):
        try:
            return BotData.objects.get(pk=pk)
        except BotData.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        bdata = BotData.objects.all()
        serializer = BotDataSerializer(bdata, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BotDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        bdata = BotData.objects.get(user_id=request.data['user_id'])
        bdata.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)