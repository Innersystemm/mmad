# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-23 20:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignsVector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.IntegerField(default=0)),
                ('sign1', models.IntegerField(default=0)),
                ('sign2', models.IntegerField(default=0)),
                ('sign3', models.IntegerField(default=0)),
                ('sign4', models.IntegerField(default=0)),
            ],
        ),
    ]