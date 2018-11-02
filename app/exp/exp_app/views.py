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

<<<<<<< HEAD

def get_driver(request, username):
    # login_required
=======
def get_driver(request, username):

>>>>>>> origin/master
    url = 'http://models-api:8000/get_driver/'+str(username)
    req = urllib.request.Request(url)
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    respond = json.loads(resp_json)

    if respond["state"] == "Fail":
        return JsonResponse({'state': "Fail", 'error': respond["error"]})
    driver = respond["driver"]
    return JsonResponse({'state': "Success", 'driver': driver})

def create_driver(request):
    if request.method == "GET":
        return JsonResponse({'state': "Fail", 'error': 'USE POST REQUEST!'})
    else:
        form = DriverForm(request.POST)
        if form.is_valid():
            post_data = {}
            post_data["first_name"] = request.POST["first_name"]
            post_data["last_name"] = request.POST["last_name"]
            post_data["car_model"] = request.POST["car_model"]
            post_data["password"] = request.POST["password"]
            post_data["email"] = request.POST["email"]
            post_data["username"] = request.POST["username"]
            post_data["birthday"] = request.POST["birthday"]
            post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
            req = urllib.request.Request('http://models-api:8000/create_driver/', data=post_encoded, method='POST')
            resp_json = urllib.request.urlopen(req).read().decode('utf-8')
            respond = json.loads(resp_json)
            if respond.json()["state"] == "Fail":
                return JsonResponse({'state': "Fail", 'error': respond.json()["error"]})
            return redirect('list_drivers')
        return JsonResponse({'state': "Fail", 'error': 'Invalid Input!'})


def update_driver(request, username):
<<<<<<< HEAD
    # login_required
=======
>>>>>>> origin/master
    if request.method == "GET":
        return JsonResponse({'state': "Fail", 'error': 'USE POST REQUEST!'})
    else:
        form = DriverForm(request.POST)
        if form.is_valid():
            post_data = {}
            post_data["first_name"] = request.POST["first_name"]
            post_data["last_name"] = request.POST["last_name"]
            post_data["car_model"] = request.POST["car_model"]
            post_data["password"] = request.POST["password"]
            post_data["email"] = request.POST["email"]
            post_data["username"] = request.POST["username"]
            post_data["birthday"] = request.POST["birthday"]
            post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
            req = urllib.request.Request(f'http://models-api:8000/update_driver/{username}', data=post_encoded, method='POST')
            resp_json = urllib.request.urlopen(req).read().decode('utf-8')
            respond = json.loads(resp_json)
            if respond.json()["state"] == "Fail":
                return JsonResponse({'state': "Fail", 'error': respond.json()["error"]})
            return redirect('list_drivers')
        return JsonResponse({'state': "Fail", 'error': 'Invalid Input!'})

# def delete_driver(request, id):
#     if request.method == "GET":
#         return render(request, 'drivers-form.html', {'form': "Use Post Request!"})
#     else:
#         req = urllib.request.Request('http://models-api:8000/update_driver/', data=request.POST, method='POST')
#         respond = requests.post(f'http://models-api:8000/delete_user/{id!s}', data=request.POST)
#         if respond.json()["state"] == "Fail":
#             return JsonResponse({'state': "Fail", 'error': respond.json()["error"]})
#         driver = respond.json()["driver"]
#         return render(request, 'driver-delete-confirm.html', {'driver': driver})

