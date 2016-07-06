# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0011_auto_20160327_0817'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_of_user',
            name='hadSaved',
            field=models.BooleanField(default=False),
        ),
    ]
