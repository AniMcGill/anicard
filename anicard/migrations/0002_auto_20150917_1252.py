# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anicard', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MembershipSpan',
            new_name='MembershipCard',
        ),
        migrations.AddField(
            model_name='cardrequest',
            name='delivered',
            field=models.BooleanField(default=False),
        ),
    ]
