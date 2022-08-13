from django.shortcuts import render, redirect


def view_cart(request):
    """ View to view whats in the cart  """

    return render(request, 'cart/cart.html')


def add_to_cart(request, product_id):
    """ Adds quantity of product to shopping cart """
    cart = request.session.get('cart', {})
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    if product_id in list(cart.keys()):
        cart[product_id] += quantity
    else:
        cart[product_id] = quantity
    
    request.session['cart'] = cart
    return redirect(redirect_url)
