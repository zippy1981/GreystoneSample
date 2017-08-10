# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-10 18:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_text', models.CharField(blank=True, default='', max_length=100)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]