# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('depotapp', '0002_auto_20180104_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_buyer',
            field=models.NullBooleanField(),
        ),
    ]
