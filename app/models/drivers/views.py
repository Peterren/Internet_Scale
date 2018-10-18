from django.shortcuts import render, redirect
from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize
from .models import Driver
from django.http import JsonResponse
from .forms import DriverForm
from django.http import HttpResponse
import json



class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        return super().default(obj)

def list_drivers(request):
    drivers = serialize('json', Driver.objects.all(), cls=LazyEncoder)
    # drivers = Driver.objects.all()
    return JsonResponse({'state': "Success", 'drivers': drivers})

# def create_driver(request):
#     form = DriverForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return JsonResponse({'state': "Success"})
#     return JsonResponse({'state': "Fail", 'error': 'Invalid Input!'})
#
#
# def update_driver(request, id):
#     driver = Driver.objects.get(id=id)
#     form = DriverForm(request.POST or None, instance = driver)
#     if form.is_valid():
#         form.save()
#         return JsonResponse({'state': "Success"})
#     return JsonResponse({'state': "Fail", 'error': 'Invalid Input!'})
#
# def delete_driver(request, id):
#     driver = serialize('json', Driver.objects.get(id=id), cls=LazyEncoder)
#     if request.method == 'POST':
#         driver.delete()
#         return JsonResponse({'state': "Success", 'driver': driver})
#     return JsonResponse({'state': "Fail", 'error': 'USE POST REQUEST!'})

