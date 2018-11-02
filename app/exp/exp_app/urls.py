from django.conf.urls import url
from django.urls import path
<<<<<<< HEAD
from . import views, views_auth

urlpatterns = [
    path('list_drivers', views.list_drivers, name='list_drivers'),
    path('get_driver/<string:username>', views.get_driver, name = "get_driver"),
    path('create_user', views.create_driver, name='create_driver'),
    path('update_user/<string:username>', views.update_driver, name='update_driver'),
    # path('delete_user/<string:username>', delete_driver, name='delete_driver'),
    path('authenticate/?$', views_auth.authenticate, name='authenticate'),
    path('login/?$', views_auth.login, name='login'),
    path('logout/?$', views_auth.logout, name='logout'),
    path('register/?$', views_auth.register, name='register-user'),
    # path('.*$', views.bad_url, name='404'),
=======
from .auth import views as auth_views
from . import views

urlpatterns = [
    path('list_drivers', list_drivers, name='list_drivers'),
    path('get_driver/<string:username>', get_driver, name = "get_driver"),
    path('create_user', create_driver, name='create_driver'),
    path('update_user/<string:username>', update_driver, name='update_driver'),
    path('delete_user/<string:username>', delete_driver, name='delete_driver'),
    url(r'^authenticate/?$', auth_views.authenticate, name='authenticate'),
    url(r'^login/?$', auth_views.login, name='login'),
    url(r'^logout/?$', auth_views.logout, name='logout'),
    url(r'^register/?$', auth_views.register, name='register-user'),

    url(r'^.*$', views.bad_url, name='404'),
>>>>>>> origin/master
]
