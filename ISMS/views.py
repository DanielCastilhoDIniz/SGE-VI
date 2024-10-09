from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    nome = 'Daniel'
    return render(request,'pages/home.html', context={'nome':nome})

def login(request):
    return render(request,'pages/login.html')

def registration(request):
    return render(request,'pages/registration.html')