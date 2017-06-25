from django.shortcuts import render

def home(request):
    return render(request, "testing/home.html", {"user": request.user})
