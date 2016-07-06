# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_auto_20160327_0431'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course_of_user',
            name='idList',
        ),
    ]
