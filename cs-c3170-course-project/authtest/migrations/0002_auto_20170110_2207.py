# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-10 20:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authtest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]