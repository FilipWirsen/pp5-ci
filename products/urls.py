from django.urls import path
from . import views

urlpatterns = [
   path('', views.all_products, name='products'),
   path('<int:product_id>/', views.product_detail, name='product_detail'),
   path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
   path('edit/<int:product_id>/', views.edit_product, name='edit_product'),

]
