# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', filebrowser.fields.FileBrowseField(max_length=200, null=True, verbose_name=b'Image', blank=True)),
                ('document', filebrowser.fields.FileBrowseField(max_length=200, null=True, verbose_name=b'PDF', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
