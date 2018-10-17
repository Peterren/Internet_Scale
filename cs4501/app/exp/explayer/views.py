from django.shortcuts import render, redirect
import json
from .forms import DriverForm
from django.http import JsonResponse
import requests

def list_drivers(request):
    respond = requests.get('http://models-api:8001/list_drivers')
    if respond.json()["state"] == "Fail":
        return JsonResponse({'state': "Fail", 'error': respond.json()["error"]})
    drivers = respond.json()["drivers"]
    return JsonResponse({'state': "Success", 'driver': drivers})

def create_driver(request):
    if request.method == "GET":
        return JsonResponse({'state': "Fail", 'error': 'USE POST REQUEST!'})
    else:
        form = DriverForm(request.POST)
        if form.is_valid():
            respond = requests.post(f'http://models-api:8001/create_user', data=request.POST)
            if respond.json()["state"] == "Fail":
                return JsonResponse({'state': "Fail", 'error': respond.json()["error"]})
            return redirect('list_drivers')
        return JsonResponse({'state': "Fail", 'error': 'Invalid Input!'})


def update_driver(request, id):
    if request.method == "GET":
        return JsonResponse({'state': "Fail", 'error': 'USE POST REQUEST!'})
    else:
        form = DriverForm(request.POST)
        if form.is_valid():
            respond = requests.post(f'http://models-api:8001/update_user/{id!s}', data=request.POST)
            if respond.json()["state"] == "Fail":
                return JsonResponse({'state': "Fail", 'error': respond.json()["error"]})
            return redirect('list_drivers')
        return JsonResponse({'state': "Fail", 'error': 'Invalid Input!'})

def delete_driver(request, id):
    if request.method == "GET":
        return render(request, 'drivers-form.html', {'form': "Use Post Request!"})
    else:
        respond = requests.post(f'http://models-api:8001/delete_user/{id!s}', data=request.POST)
        if respond.json()["state"] == "Fail":
            return JsonResponse({'state': "Fail", 'error': respond.json()["error"]})
        driver = respond.json()["driver"]
        return render(request, 'driver-delete-confirm.html', {'driver': driver})


