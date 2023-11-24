from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from .models import *
from django.contrib.auth.hashers import check_password
import random
from django.conf import settings
from django.core.mail import send_mail

def home(request):
    return render(request,'home.html')

def loginn(request):
    if request.method=='POST':
        n=request.POST.get('name')
        p=request.POST.get('pass')
        user=authenticate(username=n,password=p)
        if user is not None:
            login(request,user)
            messages.success(request,'Logedin successfully.')
            return redirect(f'/welcome/{n}')
        else:
            messages.info(request,'Invalid credentials.')
            return redirect('/login')

    return render(request,'login.html')
 
def signin(request):
    if request.user.is_authenticated:    
        return redirect(f'/welcome/{request.user}')
        # logout(request)
        # messages.success(request,'Loged out successfully.')
        # return redirect('/login')
    else:
        if  request.method=='POST':
            n=request.POST.get('name')
            e=request.POST.get('email')
            p=request.POST.get('pass')
            cp=request.POST.get('cpass')

            if p!=cp:
                messages.info(request,'password does not match')
                return redirect('/signin')
                
            elif User.objects.filter(username=n).exists():
                messages.info(request,'Username already taken')
                return redirect('/signin')
            
            elif User.objects.filter(email=e).exists():
                messages.info(request,'Email already taken')
                return redirect('/signin')
            
            else:
                otp=random.randint(100000,999999)
                subject = 'OTP for creating an account in ProjectVerse.'
                message = f'Hi {n}, thank you for registering in ProjectVerse. Your one time password is {otp}.'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [e]
                send_mail( subject, message, email_from, recipient_list )

                messages.success(request,'An OTP is sent to your regestered email.')
                d={'name':n,'email':e,'password':p,'otp':otp}
                return render(request,'email.html',d)
        # print('doneeee')                
        return render(request,'signin.html')
def welcome(request,n): 
    if request.user.is_authenticated:
        c=classes.objects.filter(user=request.user)
        pr={'n':n,'classes':c}
        return render(request,'welcome.html',pr)
    else:
        return redirect('/signin')
    
def email(request):   
    if request.method=='POST':
        n1=str(request.POST.get('n1'))
        n2=str(request.POST.get('n2'))
        n3=str(request.POST.get('n3'))
        n4=str(request.POST.get('n4'))
        n5=str(request.POST.get('n5'))
        n6=str(request.POST.get('n6'))
        n=request.POST.get('n')
        e=request.POST.get('e')
        p=request.POST.get('p')
        otp=request.POST.get('otp')
        uotp=n1+n2+n3+n4+n5+n6
        # print(uotp,n,e,p,otp,uotp,end=" ")
        if otp==uotp:
            user=User.objects.create_user(username=n,email=e,password=p)
            user.save()
            login(request,user)            
            messages.success(request,'Logedin successfully.')
            return redirect(f'/welcome/{request.user}')
        else: 
            messages.success(request,'Invalid OTP.')              
            return redirect('/login') 
    return render(request,'email.html')

def logoutt(request):
        logout(request)
        messages.success(request,'Loged out successfully.')
        return redirect('/')

def create_class(request):
    if request.user.is_authenticated:    
        if request.method=='POST':
            cname=request.POST.get('cname')
            roll=request.POST.get('roll')
            if classes.objects.filter(cname=cname).exists():
                messages.success(request,'Class name already taken, please choose a unique class name.')
                return redirect(f'/welcome/{request.user}')
            else:
                p=classes.objects.create(user=request.user,cname=cname,roll=roll)
                p.save()
                messages.success(request,'Class created successfully.')
                return redirect(f'/welcome/{request.user}')
    else:
        return redirect('/signin')
    

def delete_class(request,id):
    if request.user.is_authenticated:
        dp=classes.objects.get(id=id)
        dp.delete()
        messages.success(request,'Class deleted successfully')
        return redirect(f'/welcome/{request.user}')
    else:
        return redirect('/signin')
    
def take(request,id):
    if request.user.is_authenticated:
        i=classes.objects.get(id=id)
        clas={'c':i}
        return render(request,'take.html',clas)
    else:
        return redirect('/signin')
    

def view(request,id):
    if request.user.is_authenticated:
        return render(request,'view.html')

    else:
        return redirect('/signin')   

# Create your views here.
