# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0008_auto_20141216_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 17, 16, 39, 21, 398671, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='company',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 17, 16, 39, 21, 396923, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=True,
        ),
    ]
