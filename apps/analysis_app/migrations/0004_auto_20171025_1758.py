# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 00:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis_app', '0003_auto_20171025_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modification',
            name='gOneF',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='modification',
            name='gTwoF',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='modification',
            name='gZero',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='modification',
            name='gZeroF',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='modification',
            name='lysLoss',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='modification',
            name='manEight',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='modification',
            name='manFive',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='modification',
            name='manNine',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='modification',
            name='manSeven',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='modification',
            name='manSix',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='modification',
            name='pyroE',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='modification',
            name='pyroQ',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='modification',
            name='sodiumAdduct',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='modification',
            name='waterAdduct',
            field=models.IntegerField(),
        ),
    ]
