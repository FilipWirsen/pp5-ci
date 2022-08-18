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


def course_reviews(request):
    """ View to return course reviews page """
    
    template = 'home/course_reviews.html'
    return render(request, template)


def deals_view(request):
    """ View that return products on campaing """
    products = Product.objects.exclude(discount_percentage=0)
    context = {
        'products': products,
    }

    return render(request, 'home/deals.html', context)


def contact_view(request):
    """ View to return contact page """
    template = 'home/contact.html'
    return render(request, template)