# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-15 21:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laundry', '0004_auto_20180815_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laundry',
            name='description',
            field=models.TextField(help_text='For important message or pick up time'),
        ),
        migrations.AlterField(
            model_name='laundry',
            name='laundryweight',
            field=models.IntegerField(blank=True, help_text='weight in KG'),
        ),
        migrations.AlterField(
            model_name='laundry',
            name='location',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='laundry',
            name='name',
            field=models.CharField(max_length=120),
        ),
    ]
