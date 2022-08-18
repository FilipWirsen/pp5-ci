from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('course_reviews/', views.course_reviews, name='course_reviews'),
    path('deals/', views.deals_view, name='deals'),
    path('contact/', views.contact_view, name='contact'),
]
