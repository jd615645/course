# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course_of_user',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=10)),
                ('user_dept', models.CharField(max_length=20)),
                ('time_table', models.CharField(max_length=600)),
                ('returnarr', models.CharField(max_length=30)),
                ('create', models.DateTimeField()),
            ],
        ),
    ]
