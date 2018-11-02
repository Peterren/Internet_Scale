from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('', include('exp_app.urls')),
]