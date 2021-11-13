from django.http.request import HttpRequest
from django.http.response import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from .models import *

# Create your views here.

def sortview(request, *args, **kwargs):
    print(args)
    print(kwargs)
    if kwargs['product_slug'] != Sort.objects.get(pk=kwargs['sort_pk']).product.slug:
        return HttpResponseNotFound()
    context = {'sort' : Sort.objects.get(pk=kwargs['sort_pk']),}
    return render(request, 'logic/sort.html', context)

    # def get(self, request, *args, **kwargs) -> HttpResponse:
    #     # print(Sort.objects.get(pk=kwargs['sort_pk']).product.slug == kwargs['product_slug'])
    #     # if kwargs['product_slug'] != Sort.objects.get(pk=kwargs['sort_pk']).product.slug:
    #     #     return HttpResponseNotFound()
    #     # else:
    #         return super().get(request, *args, **kwargs)

def g_products(request, *args, **kwargs):
    year = request.GET.get('year')
    size = request.GET.get('size')
    product = request.GET.get('product')
    price_lower = request.GET.get('price')
    price_highter = request.GET.get('price')
    obj = Properties.objects
    if year:
        obj = obj.filter(year=year)
    if size:
        obj = obj.filter(size=size)
    if product:
        obj = obj.filter(product=product)
    if price_lower:
        obj = obj.filter(get_price_clear__lte=price_lower)
    if price_highter:
        obj = obj.filter(get_price_clear__gte=price_highter)
    return HttpResponse(args, kwargs)



class Categ(ListView):
    model = ProductCategory
    template_name = 'logic/cat.html'
    context_object_name = 'cats'


class Main(ListView):
    model = Sort
    template_name = 'logic/main.html'
    context_object_name = 'sorts'