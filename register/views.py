from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login

from django.http import HttpResponse

def index(request):
    context = {}
    return render(request,'register/index.html',context)
def create(request):
    user = User.objects.create_user(username=request.POST['userName'], email=request.POST['email'], password=request.POST['password'], first_name=request.POST['firstName'], last_name=request.POST['lastName'])
    if user is not None:
        login(request, user)
        return render(request, 'register/success.html', None)
    else:
        return render(request, 'register/fail.html', None)
    
def success(request):
    return HttpResponse("You have register succesfully.")
# Create your views here.
