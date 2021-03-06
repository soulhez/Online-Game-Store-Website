# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-22 17:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authtest', '0002_auto_20170110_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('price', models.IntegerField(default=0)),
                ('url', models.CharField(max_length=200)),
                ('image_path', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('developer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authtest.CustomUser')),
            ],
        ),
    ]
