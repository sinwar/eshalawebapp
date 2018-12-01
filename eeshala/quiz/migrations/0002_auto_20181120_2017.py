# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import re
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progress',
            name='score',
            field=models.CharField(max_length=1024, verbose_name='Score', validators=[django.core.validators.RegexValidator(re.compile('^[\\d,]+$', 32), 'Enter only digits separated by commas.', 'invalid')]),
        ),
        migrations.AlterField(
            model_name='sitting',
            name='incorrect_questions',
            field=models.CharField(max_length=1024, blank=True, verbose_name='Incorrect questions', validators=[django.core.validators.RegexValidator(re.compile('^[\\d,]+$', 32), 'Enter only digits separated by commas.', 'invalid')]),
        ),
        migrations.AlterField(
            model_name='sitting',
            name='question_list',
            field=models.CharField(max_length=1024, verbose_name='Question List', validators=[django.core.validators.RegexValidator(re.compile('^[\\d,]+$', 32), 'Enter only digits separated by commas.', 'invalid')]),
        ),
        migrations.AlterField(
            model_name='sitting',
            name='question_order',
            field=models.CharField(max_length=1024, verbose_name='Question Order', validators=[django.core.validators.RegexValidator(re.compile('^[\\d,]+$', 32), 'Enter only digits separated by commas.', 'invalid')]),
        ),
    ]
