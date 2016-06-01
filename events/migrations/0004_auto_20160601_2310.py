# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 20:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_eventguests_can_edit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=12, max_digits=16, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(blank=True, default='tel aviv', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=12, max_digits=16, null=True),
        ),
    ]