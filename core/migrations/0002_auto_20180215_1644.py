# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-15 16:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='risk',
            old_name='custom_fields',
            new_name='fields',
        ),
    ]