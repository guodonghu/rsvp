# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 20:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0005_auto_20170226_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date Post'),
            preserve_default=False,
        ),
    ]