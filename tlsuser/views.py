from django.contrib.auth import authenticate, login
from django.shortcuts import redirect


def tlslogin(request):
    user = authenticate(request)
    if user is not None:
        login(request, user)
    return redirect(request.GET.get("next", "/"))
