from django.contrib import admin
from django.urls import path
from pages.views import home_view, contact_view, about_view
from products.views import product_details_view, product_create_view, dynamic_lookup_view, product_delete_view, product_list_view


# Name spacing
app_name = 'products'

# url patterns
urlpatterns = [
    path('', product_details_view, name='product'),
    path('create/', product_create_view, name='create'),
    path('<int:id>', dynamic_lookup_view, name='product-detail'),
    path('<int:id>/delete/', product_delete_view, name='delete'),
    path('allproducts/', product_list_view, name='all'),


]