# Generated by Django 3.2.6 on 2021-09-02 15:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_story_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='Datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 2, 18, 30, 41, 912820)),
        ),
    ]
