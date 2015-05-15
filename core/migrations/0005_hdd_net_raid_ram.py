# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20150515_0903'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hdd',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('manufacturer', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('serial_number', models.CharField(max_length=50)),
                ('typesize', models.CharField(max_length=50)),
                ('volume', models.IntegerField()),
                ('connection_type', models.CharField(max_length=50)),
                ('standard', models.CharField(choices=[('HDD', 'HDD'), ('SSD', 'SSD'), ('Hybrid', 'Hybrid')], max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Net',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('manufacturer', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('serial_number', models.CharField(max_length=50)),
                ('connection_type', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Raid',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('manufacturer', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('serial_number', models.CharField(max_length=50)),
                ('connection_type', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ram',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('manufacturer', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('serial_number', models.CharField(max_length=50)),
                ('volume', models.IntegerField()),
                ('standard', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
