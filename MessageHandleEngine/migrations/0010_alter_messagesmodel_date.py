# Generated by Django 4.1.4 on 2022-12-30 09:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MessageHandleEngine', '0009_alter_messagesmodel_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagesmodel',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 30, 9, 10, 13, 969397), null=True),
        ),
    ]
