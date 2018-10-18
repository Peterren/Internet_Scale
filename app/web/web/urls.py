from django.urls import path
from weblayer import views

urlpatterns = [
    path('', views.list_drivers, name='list_drivers'),
    # path('drivers/signup', views.create_driver, name='create_driver'),
    # path('drivers/update/<int:id>', views.update_driver, name='update_driver'),
    # path('drivers/delete/<int:id>', views.delete_driver, name='delete_driver'),
]
