from rest_framework import routers
from django.urls import path, include
from .viewsets import StockViewSet, UserViewSet, CategoryViewSet, OrderViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'cats', CategoryViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'stock', StockViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]