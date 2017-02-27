# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0019_savedata_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savedata',
            name='score',
            field=models.IntegerField(null=True),
        ),
    ]
