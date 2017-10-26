# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 22:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loginReg_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('collectionDate', models.DateField()),
                ('client', models.IntegerField()),
                ('project', models.CharField(max_length=3)),
                ('hcSequence', models.CharField(max_length=1000)),
                ('lcSequence', models.CharField(max_length=1000)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analysis', to='loginReg_app.User')),
            ],
        ),
        migrations.CreateModel(
            name='Calculation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hcMass', models.IntegerField()),
                ('lcMass', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Modification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gZero', models.BooleanField(default=False)),
                ('gZeroF', models.BooleanField(default=False)),
                ('gOneF', models.BooleanField(default=False)),
                ('gTwoF', models.BooleanField(default=False)),
                ('manFive', models.BooleanField(default=False)),
                ('manSix', models.BooleanField(default=False)),
                ('manSeven', models.BooleanField(default=False)),
                ('manEight', models.BooleanField(default=False)),
                ('manNine', models.BooleanField(default=False)),
                ('pyroQ', models.BooleanField(default=False)),
                ('pyroE', models.BooleanField(default=False)),
                ('lysLoss', models.BooleanField(default=False)),
                ('sodiumAdduct', models.BooleanField(default=False)),
                ('waterAdduct', models.BooleanField(default=False)),
                ('analysis', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='modifications', to='analysis_app.Analysis')),
            ],
        ),
        migrations.CreateModel(
            name='Peak',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numOfPeaks', models.IntegerField()),
                ('peak1', models.IntegerField(null=True)),
                ('peak2', models.IntegerField(null=True)),
                ('peak3', models.IntegerField(null=True)),
                ('peak4', models.IntegerField(null=True)),
                ('peak5', models.IntegerField(null=True)),
                ('peak6', models.IntegerField(null=True)),
                ('peak7', models.IntegerField(null=True)),
                ('peak8', models.IntegerField(null=True)),
                ('peak9', models.IntegerField(null=True)),
                ('peak10', models.IntegerField(null=True)),
                ('peak11', models.IntegerField(null=True)),
                ('peak12', models.IntegerField(null=True)),
                ('peak13', models.IntegerField(null=True)),
                ('peak14', models.IntegerField(null=True)),
                ('peak15', models.IntegerField(null=True)),
                ('analysis', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='peaks', to='analysis_app.Analysis')),
            ],
        ),
    ]
