# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app4u', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images_Fake',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fake', models.ImageField(upload_to=b'fake')),
            ],
        ),
        migrations.CreateModel(
            name='Images_Real',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('real', models.ImageField(upload_to=b'real')),
            ],
        ),
        migrations.DeleteModel(
            name='Document',
        ),
    ]
