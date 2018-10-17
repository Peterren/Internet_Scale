from django.shortcuts import render, redirect
from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize
from .models import Driver
from .forms import DriverForm
from django.http import HttpResponse
import json


class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        return super().default(obj)

def list_drivers(request):

    drivers = serialize('json', Driver.objects.all(), cls=LazyEncoder)
    # drivers = Driver.objects.all()
    return HttpResponse(drivers, content_type='application/json')
    # return render(request, 'drivers.html',{'drivers': drivers})

def create_driver(request):
    form = DriverForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_drivers')
    return render(request, 'drivers-form.html',{'form':form})

def update_driver(request, id):
    driver = Driver.objects.get(id=id)
    form = DriverForm(request.POST or None, instance = driver)
    if form.is_valid():
        form.save()
        return redirect('list_drivers')

    return render(request, 'drivers-form.html',{'form':form, 'driver': driver})

def delete_driver(request, id):
    driver = Driver.objects.get(id=id)
    if request.method == 'POST':
        driver.delete()
        return redirect('list_drivers')

    return render(request, 'driver-delete-confirm.html',{'driver': driver})

