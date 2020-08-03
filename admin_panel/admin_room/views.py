# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import room_detail

# Create your views here.


def room_insert(request):

    if request.method=='POST':
        data=room_detail(price=request.POST.get('price',False),date=request.POST.get('dateavail',False))
        data.save()
        return render(request,'homepage.html')
    else:
        return render(request,'room_form.html')
