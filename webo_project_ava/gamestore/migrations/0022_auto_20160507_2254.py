# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0021_auto_20160507_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savedata',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
