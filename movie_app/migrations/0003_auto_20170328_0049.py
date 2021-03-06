# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-27 21:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0002_auto_20170327_1756'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tiket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('is_open', models.BooleanField(db_index=True, default=True)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='movie_app.Project')),
            ],
            options={
                'ordering': ['-project', 'summary'],
                'verbose_name': '\u0442\u0438\u043a\u0435\u0442',
                'verbose_name_plural': '\u0442\u0438\u043a\u0435\u0442\u044b',
            },
        ),
        migrations.AlterUniqueTogether(
            name='tiket',
            unique_together=set([('project', 'summary', 'project')]),
        ),
    ]
