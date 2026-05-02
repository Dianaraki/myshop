from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product
from .forms import CategoryForm, ProductForm, ReviewForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.conf import settings
import os


def basty_bet(request):
    sanatter = Category.objects.all()
    return render(request, 'shop/basty.html', {'sanatter': sanatter})

def katalog(request, sanat_id=None):
    sanatter = Category.objects.all()
    sanat = None
    tauarlar = Product.objects.all()

    if sanat_id:
        sanat = get_object_or_404(Category, id=sanat_id)
        tauarlar = tauarlar.filter(category=sanat)

    return render(request, 'shop/katalog.html', {
        'sanatter': sanatter,
        'tauarlar': tauarlar,
        'sanat': sanat
    })

def tauar_detail(request, tauar_id):
    sanatter = Category.objects.all()
    tauar = get_object_or_404(Product, id=tauar_id)
    reviews = tauar.reviews.all() 
    return render(request, 'shop/tauar_detail.html', {
        'product': tauar, 
        'reviews': reviews,
        'sanatter': sanatter
    })
@login_required(login_url='login')
def sanat_qosu(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('katalog')
    else:
        form = CategoryForm()
    return render(request, 'shop/form_bet.html', {'form': form, 'title': "Жаңа санат"})
@login_required(login_url='login')
def tauar_qosu(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('katalog')
    else:
        form = ProductForm()
    return render(request, 'shop/form_bet.html', {'form': form, 'title': "Жаңа тауар"})
@login_required(login_url='login')
def pikir_qaldyru(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.save()
            return redirect('tauar_detail', tauar_id=product.pk)
    else:
        form = ReviewForm()
    return render(request, 'shop/form_bet.html', {'form': form, 'title': "Пікір қалдыру"})

    
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect('basty_bet')
    else:
        form = UserCreationForm()
    return render(request, 'shop/register.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('basty_bet')
    else:
        form = AuthenticationForm()
    return render(request, 'shop/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('basty_bet')

def lab15_status(request):
    context = {
        'debug_status': settings.DEBUG,
        'allowed_hosts': settings.ALLOWED_HOSTS,
        'static_root': settings.STATIC_ROOT,
        'secret_key_loaded': bool(settings.SECRET_KEY)
    }
    return render(request, 'shop/lab15.html', context)