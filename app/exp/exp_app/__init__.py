from json import JSONDecodeError
import requests
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
MODEL_URL = 'http://models-api:8000/'


def make_path(paths):
    return MODEL_URL + ('{}/' * len(paths)).format(*paths)


def get(*paths, params=None, json=True):
    """
    Performs a get request on the models API layer.
    For example, get('hello', 'world') will query http://models-api:8000/hello/world
    :param paths: each sub-path entered as a separate argument
    :param params: URL parameters
    :param json: Parse json into dict
    :return: JSON response from models API
    """
    try:
        response = requests.get(make_path(paths), params=params)
        if json:
            return response.json()
        return response
    except JSONDecodeError:
        return {}


def post(*paths, data=None):
    return requests.post(make_path(paths), data=data)


def missing_param(body, params):
    for param in params:
        if param not in body:
            return True
    return False


def forward_get(request, model_api, required_params):
    if missing_param(request.GET, required_params):
        # missing a required parameter
        return HttpResponseBadRequest()

    response = get(model_api, params=request.GET, json=False)
    try:
        return JsonResponse(response.json(), safe=False, status=response.status_code)
    except JSONDecodeError:
        return HttpResponseBadRequest()


def forward_post(request, model_api, required_data):
    if missing_param(request.POST, required_data):
        # missing a required field
        return HttpResponseBadRequest()

    data = {field: request.POST[field] for field in required_data}
    response = post(model_api, data=data)
    return HttpResponse(status=response.status_code)
