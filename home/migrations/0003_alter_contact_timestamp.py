# Generated by Django 4.0.5 on 2022-07-28 12:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contact_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='timeStamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]