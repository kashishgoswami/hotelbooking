# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-31 12:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_room_detail'),
    ]

    operations = [
        migrations.DeleteModel(
            name='room_table',
        ),
        migrations.AlterModelTable(
            name='room_detail',
            table='rooms_room_detail',
        ),
    ]