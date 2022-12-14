# Generated by Django 4.0.5 on 2022-07-30 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('context', models.TextField()),
                ('slug', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=200)),
                ('timeStamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]
