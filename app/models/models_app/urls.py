
from django.urls import path
from . import views_auth

from .views import list_drivers, create_driver, update_driver, delete_driver, get_driver
urlpatterns = [
    path('list_drivers', list_drivers, name='list_drivers'),
    path('get_driver/<str:username>', get_driver, name = "get_driver"),
    path('create_user', create_driver, name='create_driver'),
    path('update_user/<str:username>', update_driver, name='update_driver'),
    # path('delete_user/<str:username>', delete_driver, name='delete_driver'),
    path('authenticate/?$', views_auth.authenticate, name='authenticate'),
    path('login/?$', views_auth.login, name='login'),
    path('logout/?$', views_auth.logout, name='logout'),
    path('register/?$', views_auth.register, name='register-user'),
]
