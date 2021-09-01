# Generated by Django 3.2.6 on 2021-08-31 18:50

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
                ('Datetime', models.DateTimeField(auto_now_add=True)),
                ('source_url', models.URLField()),
                ('img_url', models.URLField(blank=True)),
                ('category', models.CharField(max_length=50)),
            ],
        ),
    ]
