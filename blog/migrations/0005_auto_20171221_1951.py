# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-21 10:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20171221_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
