# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='game',
            name='price',
        ),
        migrations.RemoveField(
            model_name='game',
            name='purchaser',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='money',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(unique=True, max_length=70),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=models.CharField(unique=True, max_length=30),
        ),
    ]
