# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_course_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_of_user',
            name='course_list',
            field=models.ManyToManyField(to='course.Course'),
        ),
    ]
