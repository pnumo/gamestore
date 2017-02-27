# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0020_auto_20160507_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savedata',
            name='score',
            field=models.TextField(null=True),
        ),
    ]
