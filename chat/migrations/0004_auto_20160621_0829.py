# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-21 14:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20160620_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='send_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
