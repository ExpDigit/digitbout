from rest_framework import routers, viewsets
from django.urls import path, include
from .viewsets import StockViewSet, UserViewSet, CategoryViewSet, OrderViewSet, StockDetail, BotDataDetail
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'cats', CategoryViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'stock', StockViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('edit-stock/', StockDetail.as_view()),
    path('bot/', BotDataDetail.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]