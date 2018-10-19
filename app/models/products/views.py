from django.shortcuts import render, redirect
from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import Product
from .forms import ProductForm

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

