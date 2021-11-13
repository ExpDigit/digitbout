from django.conf.urls import include
from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', Main.as_view()),
    path('products/<slug:product_slug>/<int:sort_pk>', sortview, name='sort'),
    path('products/', g_products, name='product'),
    path('products/<slug:product_slug>/', Categ.as_view(), name='product'),
    path('categories/<slug:cat_slug>/', Categ.as_view(), name='cat'),
    path('categories/', Categ.as_view(), name='cats'),
]