# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('depotapp', '0003_auto_20180104_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_register_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'date to register'),
        ),
    ]
