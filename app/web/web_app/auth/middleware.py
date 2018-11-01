from . import logout
from .. import get
from .models import User


class AuthenticationMiddleware(object):
    """
    Manually implement django.contrib.auth.middleware.AuthenticationMiddleware :)
    """
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if request.session and 'auth_token' in request.session:
            user = get('authenticate', params={'authenticator': request.session['auth_token']}) or None
            request.user = User(user)
            if user is None:
                logout(request)
        else:
            request.user = User(None)

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
