# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-02 17:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='user',
            field=models.CharField(max_length=200),
        ),
    ]