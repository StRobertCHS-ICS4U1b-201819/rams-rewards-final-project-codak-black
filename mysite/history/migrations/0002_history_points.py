# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-20 06:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='points',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
