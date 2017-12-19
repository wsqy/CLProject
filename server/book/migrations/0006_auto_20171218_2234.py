# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-18 22:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_auto_20171209_0116'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-weights', 'create_time'], 'verbose_name': '文章', 'verbose_name_plural': '文章'},
        ),
        migrations.AddField(
            model_name='article',
            name='is_display',
            field=models.BooleanField(default=True, verbose_name='文章是否显示'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='is_display',
            field=models.BooleanField(default=True, verbose_name='章节是否显示'),
        ),
    ]