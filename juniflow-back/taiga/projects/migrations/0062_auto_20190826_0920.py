# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2021-present Kaleidos Ventures SL

# Generated by Django 1.11.22 on 2019-08-26 09:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0061_auto_20180918_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='videoconferences',
            field=models.CharField(blank=True, choices=[('whereby-com', 'Whereby.com'), ('jitsi', 'Jitsi'), ('custom', 'Custom'), ('talky', 'Talky')], max_length=250, null=True, verbose_name='videoconference system'),
        ),
        migrations.AlterField(
            model_name='projecttemplate',
            name='videoconferences',
            field=models.CharField(blank=True, choices=[('whereby-com', 'Whereby.com'), ('jitsi', 'Jitsi'), ('custom', 'Custom'), ('talky', 'Talky')], max_length=250, null=True, verbose_name='videoconference system'),
        ),
    ]
