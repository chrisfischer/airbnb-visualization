# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 05:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualize', '0030_auto_20171028_0511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='street',
            field=models.CharField(max_length=2000),
        ),
    ]
