# Generated by Django 3.2.6 on 2021-09-02 10:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=100)),
                ('Datetime', models.DateTimeField(default=datetime.datetime(2021, 9, 2, 13, 32, 34, 968482))),
                ('source_url', models.URLField()),
                ('img_url', models.URLField(null=True)),
                ('category', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
