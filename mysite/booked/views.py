# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from booked.models import booking_table

# Create your views here.

def booking(request):

    if request.method=='POST':
        data=booking_table(price=request.POST.get('price1',False),check_in=request.POST.get('checkin',False),check_out=request.POST.get('checkout',False),member=request.POST.get('mem',False))
        data.save()
        return render(request,'homepage.html')
    else:
        return render(request,'book.html')