# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_testmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='cpu',
            name='server',
            field=models.ForeignKey(to='core.Server', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='hdd',
            name='server',
            field=models.ForeignKey(to='core.Server', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='net',
            name='server',
            field=models.ForeignKey(to='core.Server', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='raid',
            name='server',
            field=models.ForeignKey(to='core.Server', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ram',
            name='server',
            field=models.ForeignKey(to='core.Server', blank=True, null=True),
        ),
    ]
