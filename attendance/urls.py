"""
URL configuration for attendance project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('login/',loginn,name='login'),
    path('signin/',signin,name='signin'),
    path('email/',email,name='email'),
    path('welcome/<str:n>',welcome,name='welcome'),
    path('logout/',logoutt,name='logout'),
    path('create_class/',create_class,name='create_class'),
    path('delete_class/<int:id>',delete_class,name='delete_class'),
    path('take/<int:id>',take,name='take'),
    path('view/<int:id>',view,name='view'),
]
