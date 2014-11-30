# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useractivation',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime.now),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useractivation',
            name='activation_id',
            field=models.CharField(default=uuid.uuid4, unique=True, max_length=100),
            preserve_default=True,
        ),
    ]
