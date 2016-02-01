# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-01 09:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20160201_0904'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificationlinks',
            name='class_open_date',
            field=models.DateField(blank=True, help_text="\u4ec5\u5728\u6587\u7ae0\u7c7b\u578b\u4e3a'\u6700\u65b0\u5f00\u73ed'\u65f6\u624d\u4f7f\u7528\u6b64\u9879,\u9009\u62e9\u5f00\u73ed\u65e5\u671f", null=True, verbose_name='\u5f00\u73ed\u65e5\u671f'),
        ),
        migrations.AlterField(
            model_name='notificationlinks',
            name='categroy',
            field=models.CharField(choices=[(b'stu_dairy', '\u5b66\u5458\u65e5\u8bb0'), (b'good_news', '\u559c\u62a5'), (b'school_news', '\u516c\u544a'), (b'news_class', '\u6700\u65b0\u5f00\u73ed')], max_length=32, verbose_name='\u6587\u7ae0\u7c7b\u578b'),
        ),
    ]