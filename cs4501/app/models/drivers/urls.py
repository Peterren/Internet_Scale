from django.urls import path

from .views import list_drivers, create_driver, update_driver, delete_driver

urlpatterns = [
    path('list_drivers', list_drivers, name='list_drivers'),
    path('create_user', create_driver, name='create_driver'),
    path('update_user/<int:id>', update_driver, name='update_driver'),
    path('delete_user/<int:id>', delete_driver, name='delete_driver'),
]
