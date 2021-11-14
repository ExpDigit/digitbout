from django.http.request import HttpRequest
from django.http.response import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView
from .models import *
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm

# Create your views here.

def temp(request):
    return HttpResponse("Do nothing!")

def sortview(request, *args, **kwargs):
    print(args)
    print(kwargs)
    if kwargs['product_slug'] != Sort.objects.get(pk=kwargs['sort_pk']).product.slug:
        return HttpResponseNotFound()
    context = {'sort' : Sort.objects.get(pk=kwargs['sort_pk']),}
    return render(request, 'logic/sort.html', context)

def contacts(request, *args, **kwargs):
    if request.GET.get('search'):
        search_redirect(request)
    return render(request, 'logic/contacts.html')

def search_redirect(request):
    return reverse_lazy('search/?search='+request.GET.get('search'))

def search(request, *args, **kwargs):

    return HttpResponse("Hello" + request.GET.get('search') + "!")

def category(request, *args, **kwargs):
    temp = ProductCategory.objects.get(slug=kwargs['cat_slug']).pk
    context = {'prods' : Product.objects.filter(category=temp),}
    return render(request, 'logic/cat.html', context)
    
def sorts(request, *args, **kwargs):
    context = {'sorts' : Sort.objects.filter(product=kwargs['sort_pk']),}
    return render(request, 'logic/cat.html', context)
    
def sort_normal(request, *args, **kwargs):
    context = {'normal_sorts' : Properties.objects.filter(sort=kwargs['sort_pk']),}
    return render(request, 'logic/cat.html', context)

def catalog(request, *args, **kwargs):
    if request.GET.get('search'):
        search_redirect(request)
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
    context = {'products' : obj}
    return render(request, 'logic/catalog.html', context)


def productview(request, *args, **kwargs):
    context = {'product' : Properties.objects.get(pk=kwargs['product_pk']),}
    return render(request, 'logic/product.html', context)



class Categ(ListView):
    model = ProductCategory
    template_name = 'logic/cat.html'
    context_object_name = 'cats'


class Main(ListView):
    model = Properties
    template_name = 'logic/main.html'
    context_object_name = 'products'


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
        return redirect('main')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request,
                      'account/edit.html',
                      {'user_form': user_form,
                       'profile_form': profile_form})

@login_required
def profile(request, *args, **kwargs):
    context = {'user': User.objects.get(pk=request.user.pk), 'profile' : Profile.objects.get(user=request.user.pk)}
    return render(request, 'logic/profile.html', context)

def stats(request, *args, **kwargs):
    context = {'user': User.objects.all(), 'profile' : Profile.objects.all()}
    return render(request, 'logic/stats.html', context)