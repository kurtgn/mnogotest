# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_floor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cpu',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('manufacturer', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('serial_number', models.CharField(max_length=50)),
                ('socket', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Enclosure',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('units_height', models.IntegerField(default=3)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Rack',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('unit_capacity', models.IntegerField(default=47)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('floor', models.ForeignKey(to='core.Floor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Row',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('room', models.ForeignKey(to='core.Room')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('enclosure', models.ForeignKey(blank=True, to='core.Enclosure', null=True)),
                ('rack', models.ForeignKey(blank=True, to='core.Rack', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ServerType',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('cpu_slots', models.IntegerField()),
                ('cpu_socket', models.CharField(max_length=50)),
                ('ram_slots', models.IntegerField()),
                ('ram_standard', models.CharField(max_length=50)),
                ('hdd_slots', models.IntegerField()),
                ('hdd_typesize', models.CharField(max_length=50)),
                ('hdd_standard', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='server',
            name='server_type',
            field=models.ForeignKey(to='core.ServerType'),
        ),
        migrations.AddField(
            model_name='rack',
            name='row',
            field=models.ForeignKey(to='core.Row'),
        ),
        migrations.AddField(
            model_name='enclosure',
            name='rack',
            field=models.ForeignKey(blank=True, to='core.Rack', null=True),
        ),
    ]
