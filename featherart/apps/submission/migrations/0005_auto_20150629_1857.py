# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0004_auto_20141123_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='tags',
            field=models.ManyToManyField(to='submission.Tag', blank=True),
        ),
    ]
