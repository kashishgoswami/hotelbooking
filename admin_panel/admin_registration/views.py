# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import register_table
# Create your views here.

def register_detail_view(request):

    query_result=register_table.objects.all()
    return render(request,'register_details.html',{'data':query_result})
