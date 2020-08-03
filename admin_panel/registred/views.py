# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import admin_register_table

# Create your views here.
def register_view(request):
    
    
    if request.method=='POST':
        data=admin_register_table(fname=request.POST.get('fname1',False),lname=request.POST.get('lname',False),email=request.POST.get('email',False),password=request.POST.get('pass',False),experience=request.POST.get('exper',False))
        data.save()
        return render(request,'regis_from.html')
    else:
        return render(request,'regis_from.html')
