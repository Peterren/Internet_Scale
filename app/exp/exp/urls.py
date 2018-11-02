<<<<<<< HEAD
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('', include('exp_app.urls')),
=======
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('exp_app.urls')),
    url(r'^admin/', admin.site.urls),
>>>>>>> origin/master
]