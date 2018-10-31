from django.conf.urls import url

from .auth import views as auth_views
from . import views

urlpatterns = [
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
]
