from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_reviews, name='course_reviews'),
]