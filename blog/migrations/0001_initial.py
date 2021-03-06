# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-01 00:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('description', models.CharField(blank=True, help_text='simple description', max_length=100, null=True, verbose_name='description')),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Create Date')),
            ],
        ),
    ]
