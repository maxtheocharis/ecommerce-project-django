from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product

def cart_detail(request):
    cart = request.session.get('cart', {})
    items = []
    total = 0
    for slug, qty in cart.items():
        product = get_object_or_404(Product, slug=slug)
        line_total = product.price * qty
        items.append({'product': product, 'quantity': qty, 'sub_total': line_total})
        total += line_total
    return render(request, 'cart/cart_detail.html', {'items': items, 'total': total})

def cart_add(request, slug):
    cart = request.session.get('cart', {})
    cart[slug] = cart.get(slug, 0) + 1
    request.session['cart'] = cart
    return redirect('cart_detail')

def cart_remove(request, slug):
    cart = request.session.get('cart', {})
    if slug in cart:
        del cart[slug]
        request.session['cart'] = cart
    return redirect('cart_detail')
