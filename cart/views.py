from django.shortcuts import render, redirect, get_object_or_404, reverse, HttpResponse
from django.contrib import messages

from products.models import Product


def view_cart(request):
    """ View to view whats in the cart  """

    return render(request, 'cart/cart.html')


def add_to_cart(request, product_id):
    """ Adds quantity of product to shopping cart """
    cart = request.session.get('cart', {})
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    product = get_object_or_404(Product, pk=product_id)

    if product_id in list(cart.keys()):
        cart[product_id] += quantity
        messages.success(request, f'Updated quantity of {product.name} to {cart[product_id]}')
    else:
        cart[product_id] = quantity
        messages.success(request, f'Succesfully added {cart[product_id]} of {product.name} to cart')
    
    request.session['cart'] = cart
    return redirect(redirect_url)


def remove_from_cart(request, product_id):
    """Remove product from the shopping cart"""
    product = get_object_or_404(Product, pk=product_id)
    cart = request.session.get('cart', {})
    cart.pop(product_id)
    messages.success(request, f'Removed {product.name} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

