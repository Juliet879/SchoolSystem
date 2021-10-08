# Generated by Django 3.2.5 on 2021-09-03 10:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=40)),
                ('organizer', models.CharField(blank=True, max_length=35, null=True)),
                ('guest', models.CharField(blank=True, max_length=35, null=True)),
                ('date', models.DateTimeField(max_length=10)),
                ('start_time', models.DateTimeField(default=datetime.date.today)),
                ('end_time', models.DateTimeField()),
                ('event_link', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]
