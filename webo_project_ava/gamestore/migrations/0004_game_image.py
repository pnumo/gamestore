# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import gamestore.models


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0003_auto_20160413_0115'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='image',
            field=models.FileField(upload_to=gamestore.models.get_upload_file_name, default=0),
            preserve_default=False,
        ),
    ]
