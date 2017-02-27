# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0018_savedata'),
    ]

    operations = [
        migrations.AddField(
            model_name='savedata',
            name='score',
            field=models.TextField(null=True),
        ),
    ]
