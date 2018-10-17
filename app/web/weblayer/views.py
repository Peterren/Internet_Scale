from django.shortcuts import render, redirect
#from .models import Driver
from .forms import DriverForm

import requests



def list_drivers(request):
#    drivers = Driver.objects.all()
    respond = requests.get('http://exp-api:8002/list_drivers')
    drivers = respond.json()
    return render(request, 'drivers.html',{'drivers': drivers})

def create_driver(request):
    if request.method == "GET":
        form = DriverForm()
        return render(request, 'drivers-form.html',{'form':form})
    else:
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_drivers')
        return render(request, 'drivers-form.html', {'form': "Invalid Input!"})

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

