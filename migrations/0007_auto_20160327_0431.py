# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_course_of_user_course_list'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course_of_user',
            old_name='course_list',
            new_name='idList',
        ),
    ]
