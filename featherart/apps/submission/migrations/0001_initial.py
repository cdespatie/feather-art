# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content_path', models.CharField(max_length=500)),
                ('title', models.CharField(max_length=200)),
                ('date_submitted', models.DateTimeField()),
                ('description', models.CharField(max_length=2000)),
                ('content_rating', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
