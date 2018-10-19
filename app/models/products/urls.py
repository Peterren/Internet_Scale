from django.urls import path

from .views import list_products, create_product, update_product, delete_product, get_product

urlpatterns = [
    path('product/list', list_products, name='list_products'),
    path('product/get/<int:id>', get_product, name="get_product"),
    path('product/create', create_product, name='create_product'),
    path('product/update/<int:id>', update_product, name='update_product'),
    path('product/delete/<int:id>', delete_product, name='delete_product'),
]
