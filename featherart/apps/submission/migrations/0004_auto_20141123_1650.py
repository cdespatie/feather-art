# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0003_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='submissions',
        ),
        migrations.AddField(
            model_name='submission',
            name='tags',
            field=models.ManyToManyField(to='submission.Tag'),
            preserve_default=True,
        ),
    ]
