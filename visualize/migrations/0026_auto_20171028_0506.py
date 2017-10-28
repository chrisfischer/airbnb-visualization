# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 05:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualize', '0025_auto_20171028_0504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='city',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='listing',
            name='host_neighbourhood',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='host_verifications',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='listing',
            name='jurisdiction_names',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='listing',
            name='market',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='listing',
            name='neighbourhood',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='listing',
            name='smart_location',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='listing',
            name='street',
            field=models.CharField(max_length=200),
        ),
    ]
