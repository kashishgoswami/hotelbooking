# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class room_detail(models.Model):
    
    price=models.IntegerField()
    date=models.DateField()

    class Meta:
        db_table="rooms_room_detail"

