from django.contrib.auth import authenticate


def login(request):
    user = authenticate(request)
    return None
