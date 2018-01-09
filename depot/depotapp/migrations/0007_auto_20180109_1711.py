# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('depotapp', '0006_myorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='myorder',
            name='order_price',
            field=models.DecimalField(default=0.0, max_digits=24, decimal_places=2),
        ),
        migrations.AddField(
            model_name='myorder',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
