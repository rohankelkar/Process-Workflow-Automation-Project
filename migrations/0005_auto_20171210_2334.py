# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-10 23:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_auto_20171210_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklist',
            name='container',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contained_lists', to='first_app.Container'),
        ),
        migrations.AlterField(
            model_name='checklist',
            name='holder',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='taked_lists', to='first_app.User'),
        ),
    ]
