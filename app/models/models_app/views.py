from django.shortcuts import render, redirect
from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize
from .models import Driver
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from .forms import DriverForm
from django.http import HttpResponse
import json

from .models import Product
from .forms import ProductForm


class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        return super().default(obj)


def list_drivers(request):
    drivers = Driver.objects.all()
    result = []
    for driver in drivers:
        result.append({"first_name": driver.first_name, "last_name": driver.last_name, "car_model": driver.car_model,"rating": driver.rating})
    return JsonResponse({'state': "Success", 'drivers': result})


def get_driver(request, username):
    try:
        driver = Driver.objects.get(username=username)
    except ObjectDoesNotExist:
        return JsonResponse({'state': "Fail", 'error': "Username doesn't exist!"}, status=404)
    return JsonResponse({'state': "Success", 'driver': {"first_name" : driver.first_name, "last_name"  : driver.last_name, "car_model" : driver.car_model, "rating" : driver.rating, "email": driver.email,"username": driver.username, "birthday": driver.birthday}})


def create_driver(request):
    form = DriverForm(request.POST or None)
    if form.is_valid():
        form.save()
        return JsonResponse({'state': "Success"})
    return JsonResponse({'state': "Fail", 'error': 'Invalid Input!'}, status=404)


def update_driver(request, username):
    try:
        driver = Driver.objects.get(username=username)
    except ObjectDoesNotExist:
        return JsonResponse({'state': "Fail", 'error': "Username doesn't exist!"}, status=404)
    form = DriverForm(request.POST or None, instance = driver)
    if form.is_valid():
        form.save()
        return JsonResponse({'state': "Success"})
    return JsonResponse({'state': "Fail", 'error': 'Invalid Input!'}, status=404)


def delete_driver(request, username):
    try:
        driver = Driver.objects.get(username=username)
    except ObjectDoesNotExist:
        return JsonResponse({'state': "Fail", 'error': "Username doesn't exist!"}, status=404)
    if request.method == 'POST':
        driver.delete()
        return JsonResponse({'state': "Success", 'driver': {"first_name" : driver.first_name, "last_name"  : driver.last_name, "car_model" : driver.car_model, "rating" : driver.rating, "email": driver.email,"username": driver.username, "birthday": driver.birthday}})
    return JsonResponse({'state': "Fail", 'error': 'USE POST REQUEST!'}, status=404)


class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        return super().default(obj)


def list_products(request):
    products = Product.objects.all()
    result = []
    for product in products:
        result.append({"description": product.description, "price": product.price, "quantity": product.quantity,"id": product.id})
    return JsonResponse({'state': "Success", 'products': result})


def get_product(request, id):
    try:
        product = Product.objects.get(id=id)
    except ObjectDoesNotExist:
        return JsonResponse({'state': "Fail", 'error': "Id doesn't exist!"}, status=404)

    return JsonResponse({'state': "Success", 'product': {"description": product.description, "price": product.price, "quantity": product.quantity,"id": product.id}})


def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return JsonResponse({'state': "Success"})
    return JsonResponse({'state': "Fail", 'error': 'Invalid Input!'}, status=404)

def update_product(request, id):
    try:
        product = Product.objects.get(id=id)
    except ObjectDoesNotExist:
        return JsonResponse({'state': "Fail", 'error': "Id doesn't exist!"}, status=404)
    form = ProductForm(request.POST or None, instance = product)
    if form.is_valid():
        form.save()
        return JsonResponse({'state': "Success"})
    return JsonResponse({'state': "Fail", 'error': 'Invalid Input!'}, status=404)


def delete_product(request, id):
    try:
        product = Product.objects.get(id=id)
    except ObjectDoesNotExist:
        return JsonResponse({'state': "Fail", 'error': "Id doesn't exist!"}, status=404)
    if request.method == 'POST':
        product.delete()
        return JsonResponse({'state': "Success", 'product': {"description": product.description, "price": product.price,
                                                             "quantity": product.quantity, "id": product.id}})
    return JsonResponse({'state': "Fail", 'error': 'USE POST REQUEST!'}, status=404)