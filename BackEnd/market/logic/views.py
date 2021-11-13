from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from .models import *

# Create your views here.


def home(request):
    return render(request, 'base.html')


class Categ(ListView):
    model = ProductCategory
    template_name = "logic/categ.html"
    context_object_name = 'cats'