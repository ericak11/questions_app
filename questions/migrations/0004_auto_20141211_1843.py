# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_question_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='content',
            field=models.TextField(max_length=2000),
            preserve_default=True,
        ),
    ]
