from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('course_reviews/', views.course_reviews, name='course_reviews'),
]
