# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0015_auto_20160428_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='owner',
            field=models.ForeignKey(null=True, editable=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
