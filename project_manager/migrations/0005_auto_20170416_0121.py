# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-15 22:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_manager', '0004_auto_20170328_0107'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=256)),
                ('original_name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('born', models.DateField()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='ticket',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='project',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='Ticket',
        ),
    ]
