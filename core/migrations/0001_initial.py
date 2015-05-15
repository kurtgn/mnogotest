# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseComponent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('manufacturer', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('serial_number', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Datacenter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Enclosure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('units_height', models.IntegerField(default=3)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('datacenter', models.ForeignKey(to='core.Datacenter')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Rack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('enclosure', models.ForeignKey(null=True, blank=True, to='core.Enclosure')),
                ('rack', models.ForeignKey(null=True, blank=True, to='core.Rack')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ServerType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
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
        migrations.CreateModel(
            name='Cpu',
            fields=[
                ('basecomponent_ptr', models.OneToOneField(parent_link=True, primary_key=True, serialize=False, to='core.BaseComponent', auto_created=True)),
                ('socket', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
            bases=('core.basecomponent',),
        ),
        migrations.CreateModel(
            name='Hdd',
            fields=[
                ('basecomponent_ptr', models.OneToOneField(parent_link=True, primary_key=True, serialize=False, to='core.BaseComponent', auto_created=True)),
                ('typesize', models.CharField(max_length=50)),
                ('volume', models.IntegerField()),
                ('connection_type', models.CharField(max_length=50)),
                ('standard', models.CharField(max_length=10, choices=[('HDD', 'HDD'), ('SSD', 'SSD'), ('Hybrid', 'Hybrid')])),
            ],
            options={
                'abstract': False,
            },
            bases=('core.basecomponent',),
        ),
        migrations.CreateModel(
            name='Net',
            fields=[
                ('basecomponent_ptr', models.OneToOneField(parent_link=True, primary_key=True, serialize=False, to='core.BaseComponent', auto_created=True)),
                ('connection_type', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
            bases=('core.basecomponent',),
        ),
        migrations.CreateModel(
            name='Raid',
            fields=[
                ('basecomponent_ptr', models.OneToOneField(parent_link=True, primary_key=True, serialize=False, to='core.BaseComponent', auto_created=True)),
                ('connection_type', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
            bases=('core.basecomponent',),
        ),
        migrations.CreateModel(
            name='Ram',
            fields=[
                ('basecomponent_ptr', models.OneToOneField(parent_link=True, primary_key=True, serialize=False, to='core.BaseComponent', auto_created=True)),
                ('volume', models.IntegerField()),
                ('standard', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
            bases=('core.basecomponent',),
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
            field=models.ForeignKey(null=True, blank=True, to='core.Rack'),
        ),
        migrations.AddField(
            model_name='basecomponent',
            name='server',
            field=models.ForeignKey(null=True, blank=True, to='core.Server'),
        ),
    ]
