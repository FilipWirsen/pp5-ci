from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout_view(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart. Add products before trying to checkout.")
        return redirect(reverse('products'))

    order_form = OrderForm()
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LOdyoAgnFUG4JtXY9Yr5KBQ7aGQF96TAy9UzZkmgymNlwipTWjNoAsyliYrVlWZbT7ymYnQdufmbe4D0HLxMl2i00NZFQWrSf',
        'client_secret': 'test client secret',
    }
    return render(request, 'checkout/checkout.html', context)