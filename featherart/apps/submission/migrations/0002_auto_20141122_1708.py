# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import submission.models


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='content_path',
            field=models.FileField(upload_to=submission.models.get_file_path),
            preserve_default=True,
        ),
    ]
