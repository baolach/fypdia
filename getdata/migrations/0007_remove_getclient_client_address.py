# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-21 01:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('getdata', '0006_auto_20170321_0031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='getclient',
            name='client_address',
        ),
    ]
