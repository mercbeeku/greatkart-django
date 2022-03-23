from itertools import product
from django.http import HttpResponse
from django.shortcuts import render

from store.models import Product

def home(request):
    products = Product.objects.all().order_by('-create_date')[:8]
    latest_products = Product.objects.all().order_by('-create_date')[:8]
    best_seller = Product.objects.all().order_by('-create_date')[:8]
    context = {
        'products': products,
        'latest_products': latest_products,
        'best_seller' : best_seller,
    }
    return render(request, 'home.html', context)