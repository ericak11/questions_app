# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0009_auto_20141217_1639'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField(default=0)),
                ('answer', models.ForeignKey(to='questions.Answer')),
                ('user', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='answer',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 24, 20, 58, 5, 412442, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='company',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 24, 20, 58, 5, 409307, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=True,
        ),
    ]
