# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-18 07:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_manager', '0006_auto_20170416_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='poster',
            field=models.ImageField(blank=True, default='movie/default/poster/default.png', null=True, upload_to='movie/<built-in function id>/poster/'),
        ),
    ]
