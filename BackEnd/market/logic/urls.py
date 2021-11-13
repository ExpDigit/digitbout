from django.conf.urls import include
from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('categories/', Categ.as_view()),
]