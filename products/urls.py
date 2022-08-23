from django.urls import path
from . import views

urlpatterns = [
   path('', views.all_products, name='products'),
   path('<int:product_id>/', views.product_detail, name='product_detail'),
   path('delete/<int:product_id>/',
        views.delete_product, name='delete_product'),
   path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
   path('add/', views.add_product, name='add_product'),
   path('product_review<int:product_id>/',
        views.product_review, name='product_review'),
   path('deals/', views.deals_view, name='deals'),
]
