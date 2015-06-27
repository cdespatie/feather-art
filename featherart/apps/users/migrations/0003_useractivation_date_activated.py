# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20141130_0010'),
    ]

    operations = [
        migrations.AddField(
            model_name='useractivation',
            name='date_activated',
            field=models.DateTimeField(null=True),
        ),
    ]
