from django.conf.urls import include, url
from django.urls import path, re_path
from .views import *
from django.contrib.auth import views as vs

urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('products/<slug:product_slug>-<int:product_pk>/', productview, name='product'),
    path('categories/<slug:cat_slug>/', category, name='cat'),
    path('categories/', Categ.as_view(), name='all_cats'),
    path('search/', search, name='search'),
    path('contacts/', contacts, name='contacts'),
    path('categories/products/<int:sort_pk>', sorts, name='sort'),
    path('categories/products/sorts/<int:sort_pk>', sort_normal, name='sort_normal'),
    url(r'^register/$', register, name='register'),
    path('login/', vs.LoginView.as_view(), name='login'),
    path('logout/', vs.LogoutView.as_view(), name='login'),
    url(r'^edit/$', edit, name='edit'),
    path('profile/', profile, name='profile'),
    path('stats/', stats, name='stats'),
]

