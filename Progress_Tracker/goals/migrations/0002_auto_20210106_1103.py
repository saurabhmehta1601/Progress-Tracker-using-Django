# Generated by Django 3.1.5 on 2021-01-06 05:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monthlygoal',
            name='task',
        ),
        migrations.AddField(
            model_name='monthlygoal',
            name='task_detail',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='monthlygoal',
            name='task_title',
            field=models.CharField(default='', max_length=70),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='monthlygoal',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 5, 5, 32, 32, 659344, tzinfo=utc)),
        ),
    ]