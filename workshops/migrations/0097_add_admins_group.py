# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-08 16:10
from __future__ import unicode_literals

from django.db import migrations


def forward(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Person = apps.get_model('workshops', 'Person')

    group = Group.objects.get_or_create(name='Admins')
    for p in Person.objects.all():
        p.groups.add(group)
        p.save()


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0096_change_help_text_in_training_request'),
    ]

    operations = [
        migrations.RunPython(forward, reverse_code=migrations.RunPython.noop),
    ]
