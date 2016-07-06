# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0012_course_of_user_hadsaved'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_of_user',
            name='user_grade',
            field=models.DecimalField(max_digits=1, decimal_places=0, default=1),
        ),
        migrations.AlterField(
            model_name='course_of_user',
            name='returnarr',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='course_of_user',
            name='time_table',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='course_of_user',
            name='user_name',
            field=models.CharField(max_length=50),
        ),
    ]
