<<<<<<< HEAD
from django.urls import path, include
=======
from django.conf.urls import url
>>>>>>> origin/master

from .auth import views as auth_views
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('list_drivers', views.list_drivers, name='list_drivers'),
    path('get_driver/<int:id>', views.get_driver, name = "get_driver"),
    path('create_user', views.create_driver, name='create_driver'),
    path('update_user/<int:id>', views.update_driver, name='update_driver'),
    # path('delete_user/<int:id>', delete_driver, name='delete_driver'),
    path('authenticate/?$', auth_views.authenticate, name='authenticate'),
    path('login/?$', auth_views.login, name='login'),
    path('logout/?$', auth_views.logout, name='logout'),
    path('register/?$', auth_views.register, name='register-user'),
    path('.*$', views.bad_url, name='404'),
=======
    path('list_drivers', list_drivers, name='list_drivers'),
    path('get_driver/<int:id>', get_driver, name = "get_driver"),
    path('create_user', create_driver, name='create_driver'),
    path('update_user/<int:id>', update_driver, name='update_driver'),
    path('delete_user/<int:id>', delete_driver, name='delete_driver'),
    url(r'^authenticate/?$', auth_views.authenticate, name='authenticate'),

    url(r'^login/?$', auth_views.login, name='login'),
    url(r'^logout/?$', auth_views.logout, name='logout'),
    url(r'^register/?$', auth_views.register, name='register-user'),

    url(r'^.*$', views.bad_url, name='404'),
>>>>>>> origin/master
]
