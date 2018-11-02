from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.http import urlencode


def login_required(view):
    """
    Replace django.contrib.auth.login_required
    """
    def wrap(request, *args, **kwargs):
        # check if user is authenticated
        if request.user.is_authenticated:
            return view(request, *args, **kwargs)
        # TODO: redirect
        return HttpResponseRedirect('{}?{}'.format(reverse('login'), urlencode({'next': request.path})))
    return wrap
