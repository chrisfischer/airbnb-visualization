# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 03:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualize', '0009_auto_20171028_0315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='host_response_rate',
            field=models.IntegerField(default=-1),
        ),
    ]
