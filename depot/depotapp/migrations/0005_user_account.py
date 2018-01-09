# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('depotapp', '0004_auto_20180108_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='account',
            field=models.DecimalField(default=0.0, max_digits=24, decimal_places=2),
        ),
    ]
