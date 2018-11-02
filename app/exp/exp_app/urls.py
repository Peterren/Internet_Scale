from django.conf.urls import url
from django.urls import path
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
]
