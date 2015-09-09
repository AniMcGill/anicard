# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CardRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('printed', models.BooleanField(default=False)),
                ('paid', models.BooleanField(default=False)),
                ('lost', models.BooleanField(default=False)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MembershipSpan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('design', models.ImageField(upload_to=b'')),
                ('year_start', models.DateField()),
                ('year_end', models.DateField()),
                ('open', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='cardrequest',
            name='year',
            field=models.ForeignKey(to='anicard.MembershipSpan'),
        ),
    ]
