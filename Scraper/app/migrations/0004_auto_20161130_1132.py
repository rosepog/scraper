# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 03:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20161130_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrape',
            name='ActivityName',
            field=models.CharField(blank=True, max_length=100, unique=True, verbose_name='ActivityName'),
        ),
        migrations.AlterField(
            model_name='scrape',
            name='Category',
            field=models.TextField(blank=True, verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='scrape',
            name='City',
            field=models.CharField(blank=True, max_length=100, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='scrape',
            name='Description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='scrape',
            name='Province',
            field=models.CharField(blank=True, max_length=10, verbose_name='Province'),
        ),
    ]
