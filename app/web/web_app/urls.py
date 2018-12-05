from django.urls import path, include

from .auth import views as auth_views
from . import views

urlpatterns = [
    path('list_drivers', views.list_drivers, name='list_drivers'),
    path('get_driver/<int:id>', views.get_driver, name = "get_driver"),
    path('create_user', views.create_driver, name='create_driver'),
    path('update_user/<int:id>', views.update_driver, name='update_driver'),
    # path('delete_user/<int:id>', delete_driver, name='delete_driver'),
    path('authenticate/?$', auth_views.authenticate, name='authenticate'),
    path('login/?$', auth_views.login, name='login'),
    path('logout/?$', auth_views.logout, name='logout'),
    path('register/?$', auth_views.register, name='register-user'),
    path('search_drivers/?$', views.search_drivers, name = 'search_drivers')
    path('.*$', views.bad_url, name='404'),
]
