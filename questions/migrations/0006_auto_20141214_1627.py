# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0005_auto_20141212_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 14, 16, 27, 41, 174993, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
