from django.shortcuts import render, redirect
#from .models import Driver
from .forms import DriverForm
from django.http import HttpResponse, HttpResponseRedirect
import urllib.request
import urllib.parse
import json



@login_required
def list_drivers(request):
#    drivers = Driver.objects.all()
    req = urllib.request.Request('http://exp-api:8000/list_drivers')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    respond = json.loads(resp_json)
    drivers = respond["drivers"]
    return render(request, 'drivers.html', {'drivers': drivers})   
    # if len(drivers) > 5:
    #     drivers = drivers[1:-2].split("},")
    #     drivers = [json.loads(x+"}")["fields"] for x in drivers]
    #     return render(request, 'drivers.html',{'drivers': drivers})
    # else:
    #     return render(request, 'drivers.html', {'drivers': ""})


def create_driver(request):
    auth = request.COOKIES.get('auth')
    if auth:
        return HttpResponseRedirect('/') #可改homepage地址
    if request.method == "GET":
        form = DriverForm()
        return render(request, 'drivers-form.html',{'form':form})
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
            req = urllib.request.Request('http://exp-api:8000/create_driver/', data=post_encoded, method='POST')
            resp_json = urllib.request.urlopen(req).read().decode('utf-8')
            respond = json.loads(resp_json)
            if respond.json()["state"] == "Fail":
                return render(request, 'drivers-form.html', {'form': respond.json()["error"]})
            return HttpResponseRedirect('/')  # 可改homepage地址
    return render(request, 'drivers-form.html', {'form': "Invalid Input!"})


def update_driver(request, username):
    if request.method == "GET":
        form = DriverForm()
        return render(request, 'drivers-form.html',{'form':form})
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
            req = urllib.request.Request(f'http://exp-api:8000/update_driver/{username}', data=post_encoded, method='POST')
            resp_json = urllib.request.urlopen(req).read().decode('utf-8')
            respond = json.loads(resp_json)
            if respond.json()["state"] == "Fail":
                return render(request, 'drivers-form.html', {'form': respond.json()["error"]})
            return HttpResponseRedirect('/')  # 可改homepage地址
    return render(request, 'drivers-form.html', {'form': "Invalid Input!"})

def search_drivers():
    if request.method == "GET":
        return JsonResponse({'state': "Fail", 'error': 'USE POST REQUEST!'})
    if "QUERY" not in request.POST:
        return JsonResponse({'state': "Fail", 'error': 'QUERY MISSING!'})
    req = urllib.request.Request('http://exp-api:8000/search_drivers')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    respond = json.loads(resp_json)
    if respond['state'] == "Fail":
        return JsonResponse(respond)
    else:
        num = respond['result']['total']
        hits = respond['result']['hits']
        result = [driver["_source"] for driver in hits]
        return render(request, 'search.html', {'num': num, 'results': result})
#
# def delete_driver(request, id):
#     if request.method == "GET":
#         return render(request, 'drivers-form.html', {'form': "Use Post Request!"})
#     else:
#         respond = requests.post(f'http://exp-api:8002/delete_user/{id!s}', data=request.POST)
#         if respond.json()["state"] == "Fail":
#             return render(request, 'drivers-form.html', {'form': respond.json()["error"]})
#         driver = respond.json()
#         return render(request, 'driver-delete-confirm.html', {'driver': driver})


def bad_url(request):
    return render(request, '404.html', {})
