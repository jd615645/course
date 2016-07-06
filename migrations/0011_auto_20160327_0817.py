# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0010_auto_20160327_0814'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course_of_user',
            old_name='courseList',
            new_name='idList',
        ),
    ]
