# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-08-08 17:55
from __future__ import unicode_literals

import conference.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0014_stripe_charge_default_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='talk',
            name='repository_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='talk',
            name='slides_url',
            field=models.URLField(blank=True),
        ),
    ]