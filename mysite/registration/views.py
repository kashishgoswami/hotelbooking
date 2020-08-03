# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from registration.forms import RegistrationForm
from registration.models import register_table

# Create your views here.


# def register_view(request):
#     return render(request,'register.html')

def register(request):

    if request.method=='POST':
        data=register_table(fname=request.POST.get('fname1',False),lname=request.POST.get('lname',False),email=request.POST.get('email',False),password=request.POST.get('pass',False))
        data.save()
        return render(request,'login.html')
    else:
        return render(request,'register.html')