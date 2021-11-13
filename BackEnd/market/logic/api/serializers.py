from rest_framework import serializers
from ..models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['url', 'name',]

class StatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Status
        fields = ['name',]

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    status = StatusSerializer()

    class Meta:
        model = Order
        fields = ['status',]

class StockSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Stock
        fields = ['pk', 'text', 'published',]

class StockEditSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Stock
        fields = ['pk', 'published',]
