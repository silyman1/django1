# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('depotapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Tel',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_register_time',
            field=models.DateTimeField(verbose_name=b'date to register', blank=True),
        ),
    ]
