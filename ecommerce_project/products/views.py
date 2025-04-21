# products/views.py

from django.shortcuts import render, get_object_or_404
from .models import Product

def product_list(request):
    """
    Show all available products.
    """
    products = Product.objects.filter(available=True)
    return render(request, 'products/product_list.html', {
        'products': products
    })

def product_detail(request, slug):
    """
    Show a single product’s detail page, looked up by slug.
    """
    product = get_object_or_404(Product, slug=slug, available=True)
    return render(request, 'products/product_detail.html', {
        'product': product
    })
