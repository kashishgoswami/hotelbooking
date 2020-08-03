# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class booking_table(models.Model):
    
    price=models.IntegerField()
    check_in=models.DateField()
    check_out=models.DateField()
    member=models.IntegerField()
