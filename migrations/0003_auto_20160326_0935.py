# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_remove_course_of_user_time_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=15)),
                ('courseID', models.CharField(max_length=10)),
                ('book', models.CharField(max_length=50)),
                ('create', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='course_of_user',
            name='time_table',
            field=models.CharField(default=datetime.datetime(2016, 3, 26, 9, 35, 11, 140807, tzinfo=utc), max_length=600),
            preserve_default=False,
        ),
    ]
