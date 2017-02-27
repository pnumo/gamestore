# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0014_auto_20160424_2253'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Highscores',
        ),
        migrations.RemoveField(
            model_name='game',
            name='games',
        ),
        migrations.AddField(
            model_name='game',
            name='highscores',
            field=models.TextField(null=True),
        ),
    ]
