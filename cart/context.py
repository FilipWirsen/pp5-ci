from django.conf import settings
from decimal import Decimal


def cart_contents(request):
    """" Context proccesor to acces cart dict on all templates """
    cart_items = []
    total = 0
    product_count = 0

    if total < settings.FREE_SHIPPING_THRESHHOLD:
        shipping = total * Decimal(settings.STANDARD_SHIPPING_PERCENTAGE)
        free_shipping_delta = settings.FREE_SHIPPING_THRESHHOLD - total
    else:
        shipping = 0
        free_shipping_delta = 0
    
    grand_total = total + shipping

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'shipping': shipping,
        'free_shipping_delta': free_shipping_delta,
        'free_delivery_threshold': settings.FREE_SHIPPING_THRESHHOLD,
        'grand_total': grand_total,
    }

    return context