# Generated by Django 3.1.5 on 2021-01-06 05:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0002_auto_20210106_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlygoal',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 5, 5, 34, 9, 131599, tzinfo=utc)),
        ),
    ]
