from django.contrib.auth import authenticate
from django.shortcuts import redirect


def login(request):
    user = authenticate(request)
    if user is not None:
        login(request, user)
    return redirect(request.GET.get("next", "/"))
