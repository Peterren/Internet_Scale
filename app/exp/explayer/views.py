from django.shortcuts import render, redirect

from .models import Driver
from .forms import DriverForm

def list_drivers(request):
    drivers = Driver.objects.all()
    return render(request, 'drivers.html',{'drivers': drivers})

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

