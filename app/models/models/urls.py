from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('models_app.urls')),
    url(r'^admin/', admin.site.urls),
]