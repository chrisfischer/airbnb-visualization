# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 03:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualize', '0008_auto_20171028_0313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='scrape_id',
            field=models.DecimalField(decimal_places=0, max_digits=20),
        ),
    ]
