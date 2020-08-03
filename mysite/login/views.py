# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from .models import register_table

# Create your views here.

def b(request):
    
    return render(request,'login.html')

























