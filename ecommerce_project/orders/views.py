from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order
from cart.views import cart_detail  # you might refactor this

@login_required
def order_create(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('product_list')
    order = Order.objects.create(
        user=request.user,
        shipping_address=request.POST.get('shipping_address', '')
    )
    for slug, qty in cart.items():
        product = get_object_or_404(Product, slug=slug)
        item = CartItem.objects.create(product=product, quantity=qty)
        order.items.add(item)
    request.session['cart'] = {}
    return redirect('order_detail', pk=order.pk)

@login_required
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'orders/order_detail.html', {'order': order})


# Create your views here.
