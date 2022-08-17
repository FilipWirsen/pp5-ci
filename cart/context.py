from django.shortcuts import get_object_or_404
from django.conf import settings
from decimal import Decimal

from products.models import Product


def cart_contents(request):
    """" Context proccesor to acces cart dict on all templates """
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    product_count = 0

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=product_id)
        product_count += quantity
        if product.get_discounted_price:
            total += quantity * product.discounted_price
        else:
            total += quantity * product.price
        cart_items.append({
            'product_id': product_id,
            'quantity': quantity,
            'product': product
        })
            
    if total < settings.FREE_SHIPPING_THRESHOLD:
        shipping = settings.STANDARD_SHIPPING_PRICE
        free_shipping_delta = settings.FREE_SHIPPING_THRESHOLD - total
    else:
        shipping = 0
        free_shipping_delta = 0
    if total == 0:
        grand_total = total
    else:
        grand_total = total + shipping

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'shipping': shipping,
        'free_shipping_delta': free_shipping_delta,
        'free_delivery_threshold': settings.FREE_SHIPPING_THRESHOLD,
        'grand_total': grand_total,
    }

    return context