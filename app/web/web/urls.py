from django.urls import path
from weblayer import views
from views import list_drivers, create_driver, update_driver, delete_driver

urlpatterns = [
    path('drivers', list_drivers, name='list_drivers'),
    path('drivers/signup', create_driver, name='create_driver'),
    path('drivers/update/<int:id>', update_driver, name='update_driver'),
    path('drivers/delete/<int:id>', delete_driver, name='delete_driver'),
]
