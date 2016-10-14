# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-12 13:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=64)),
                ('text', models.TextField()),
                ('published', models.BooleanField(db_index=True, default=True)),
            ],
        ),
    ]
