from django.shortcuts import render
from products.models import Product

# Create your views here.


def home(request):
    """ View to return home page """
    products = Product.objects.order_by('-rating')
    context = {
        'products': products,
    }
    return render(request, 'home/index.html', context)