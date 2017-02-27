# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gamestore', '0002_auto_20160408_2348'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
        migrations.AddField(
            model_name='game',
            name='owner',
            field=models.ForeignKey(editable=False, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
