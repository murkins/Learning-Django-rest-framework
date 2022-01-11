# Generated by Django 4.0 on 2022-01-04 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fbvApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('travel_points', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
