# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0007_auto_20141214_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 16, 18, 41, 55, 47466, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='company',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 16, 18, 41, 55, 44313, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=True,
        ),
    ]
