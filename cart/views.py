from django.shortcuts import render


def view_cart(request):
    """ View to view whats in the cart  """

    return render(request, 'cart/cart.html')