from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate

def home(request):
    return render(request,'home.html')
def login(request):
    return render(request,'login.html')
def signin(request):
    return render(request,'signin.html')

# Create your views here.
