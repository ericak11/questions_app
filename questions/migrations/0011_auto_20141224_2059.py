# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0010_auto_20141224_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 24, 20, 59, 20, 622286, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='company',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 24, 20, 59, 20, 619092, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=True,
        ),
    ]
