# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=50)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('unread', models.BooleanField(default=True)),
                ('receiver', models.ForeignKey(related_name=b'received_messages', to='users.User')),
                ('sender', models.ForeignKey(related_name=b'sent_messages', to='users.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
