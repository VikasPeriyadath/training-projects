# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-29 08:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bankapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='branch_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
