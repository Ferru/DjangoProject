from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

def index(request):
    context = {}
    return render(request, 'login/index.html', context)
def validate(request):
    username = request.POST['userName']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'login/success.html', None)
    else:
        return render(request, 'login/index.html', {errorMessage : "User or password incorrect"})
    
def success(request):
    return HttpResponse("You have log in succesfully.")


# Create your views here.
