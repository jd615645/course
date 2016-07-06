# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20160326_0935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='name',
        ),
    ]
