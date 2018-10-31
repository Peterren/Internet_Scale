from . import forward_get


def authenticate(request):
    return forward_get(request, 'authenticate', ['authenticator'])


def login(request):
    return forward_get(request, 'login', ['username', 'password'])


def logout(request):
    return forward_get(request, 'logout', ['authenticator'])


def register(request):
    return forward_get(request, 'register', ['username', 'password', 'first_name', 'last_name', 'birthday'])
