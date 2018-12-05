from django.shortcuts import render, redirect
import json
from .forms import DriverForm
from django.http import JsonResponse
import urllib.request
import urllib.parse
from kafka import KafkaProducer
import time
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import get, forward_post
from elasticsearch import Elasticsearch

es = Elasticsearch(['es'])
producer = KafkaProducer(bootstrap_servers='kafka:9092')


def list_drivers(request):
    req = urllib.request.Request('http://models-api:8000/list_drivers')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    respond = json.loads(resp_json)

    if respond["state"] == "Fail":
        return JsonResponse({'state': "Fail", 'error': respond["error"]})
    drivers = respond["drivers"]
    return JsonResponse({'state': "Success", 'drivers': drivers})


def get_driver(request, username):
    # login_required
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
            else:
                try:
                    producer.send('drivers', json.dumps(post_data).encode('utf-8'))
                except:
                    time.sleep(1)
                    producer.send('drivers', json.dumps(post_data).encode('utf-8'))
                return redirect('list_drivers')
        return JsonResponse({'state': "Fail", 'error': 'Invalid Input!'})


def update_driver(request, username):
    # login_required
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

def search_drivers(request):
    if request.method == "GET":
        return JsonResponse({'state': "Fail", 'error': 'USE POST REQUEST!'})

    if "QUERY" not in request.POST:
        return JsonResponse({'state': "Fail", 'error': 'QUERY MISSING!'})
    else:
        result = es.search(index = "drivers-indexer", body = {'query':{'query_string':{'query': request.POST['QUERY']}}, 'size':10}))
        if result['timed_out']:
            return JsonResponse{'state': "Fail", 'error': 'QUERY TIMED OUT!'}
        else:
            return JsonResponse({'state': "Success", 'result': result["hits"]})


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

