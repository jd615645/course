# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_remove_course_of_user_idlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_of_user',
            name='idList',
            field=models.ManyToManyField(to='course.Course'),
        ),
    ]
