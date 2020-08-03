# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import room_detail

# Create your views here.
# def room(request):

#     return render(request,'room.html')

def room_detail_view(request):

    query_result=room_detail.objects.all()
    return render(request,'room_details.html',{'data':query_result})

