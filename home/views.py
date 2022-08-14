from django.shortcuts import render

# Create your views here.


def home(request):
    """ View to return home page """
    return render(request, 'home/index.html')