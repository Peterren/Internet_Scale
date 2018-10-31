from django.shortcuts import render, redirect
import json
from .forms import DriverForm
from django.http import JsonResponse
import urllib.request
import urllib.parse
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import get, forward_post

def list_drivers(request):
    req = urllib.request.Request('http://models-api:8000/list_drivers')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    respond = json.loads(resp_json)

    if respond["state"] == "Fail":
        return JsonResponse({'state': "Fail", 'error': respond["error"]})
    drivers = respond["drivers"]
    return JsonResponse({'state': "Success", 'drivers': drivers})

def get_driver(request, id):

    url = 'http://models-api:8000/get_driver/'+str(id)
    req = urllib.request.Request(url)
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    respond = json.loads(resp_json)

    if respond["state"] == "Fail":
        return JsonResponse({'state': "Fail", 'error': respond["error"]})
    driver = respond["driver"]
    return JsonResponse({'state': "Success", 'driver': driver})
#
# def create_driver(request):
#     if request.method == "GET":
#         return JsonResponse({'state': "Fail", 'error': 'USE POST REQUEST!'})
#     else:
#         form = DriverForm(request.POST)
#         if form.is_valid():
#
#             post_data = {""request.POST.get()
#             post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
#
#             req = urllib.request.Request('http://placeholder.com/v1/api/posts/create', data=post_encoded, method='POST')
#             resp_json = urllib.request.urlopen(req).read().decode('utf-8')
#
#             resp = json.loads(resp_json)
#             respond = requests.post(f'http://models-api:8001/create_user', data=request.POST)
#             if respond.json()["state"] == "Fail":
#                 return JsonResponse({'state': "Fail", 'error': respond.json()["error"]})
#             return redirect('list_drivers')
#         return JsonResponse({'state': "Fail", 'error': 'Invalid Input!'})
#
#
# def update_driver(request, id):
#     if request.method == "GET":
#         return JsonResponse({'state': "Fail", 'error': 'USE POST REQUEST!'})
#     else:
#         form = DriverForm(request.POST)
#         if form.is_valid():
#             respond = requests.post(f'http://models-api:8001/update_user/{id!s}', data=request.POST)
#             if respond.json()["state"] == "Fail":
#                 return JsonResponse({'state': "Fail", 'error': respond.json()["error"]})
#             return redirect('list_drivers')
#         return JsonResponse({'state': "Fail", 'error': 'Invalid Input!'})
#
# def delete_driver(request, id):
#     if request.method == "GET":
#         return render(request, 'drivers-form.html', {'form': "Use Post Request!"})
#     else:
#         respond = requests.post(f'http://models-api:8001/delete_user/{id!s}', data=request.POST)
#         if respond.json()["state"] == "Fail":
#             return JsonResponse({'state': "Fail", 'error': respond.json()["error"]})
#         driver = respond.json()["driver"]
#         return render(request, 'driver-delete-confirm.html', {'driver': driver})

@csrf_exempt
def create_driver(request):
    return forward_post(request, 'drivers', ['first_name', 'last_name', 'car_model', 'rating'])
