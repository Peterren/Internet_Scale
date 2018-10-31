from django.shortcuts import render, redirect
#from .models import Driver
from .forms import DriverForm
import urllib.request
import urllib.parse
import json



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

#
# def create_driver(request):
#     if request.method == "GET":
#         form = DriverForm()
#         return render(request, 'drivers-form.html',{'form':form})
#     else:
#         form = DriverForm(request.POST)
#         if form.is_valid():
#             respond = requests.post(f'http://exp-api:8002/create_user', data=request.POST)
#             if respond.json()["state"] == "Fail":
#                 return render(request, 'drivers-form.html', {'form': respond.json()["error"]})
#             return redirect('list_drivers')
#         return render(request, 'drivers-form.html', {'form': "Invalid Input!"})
#
# def update_driver(request, id):
#     if request.method == "GET":
#         form = DriverForm()
#         return render(request, 'drivers-form.html',{'form':form})
#     else:
#         form = DriverForm(request.POST)
#         if form.is_valid():
#             respond = requests.post(f'http://exp-api:8002/update_user/{id!s}', data=request.POST)
#             if respond.json()["state"] == "Fail":
#                 return render(request, 'drivers-form.html', {'form': respond.json()["error"]})
#             return redirect('list_drivers')
#         return render(request, 'drivers-form.html', {'form': "Invalid Input!"})
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
#
#
