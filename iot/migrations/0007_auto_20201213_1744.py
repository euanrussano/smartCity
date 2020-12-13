# Generated by Django 3.1.4 on 2020-12-13 20:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('iot', '0006_auto_20201213_1550'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='InputSensor',
            new_name='inputSensor',
        ),
        migrations.AlterField(
            model_name='event',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 13, 20, 44, 12, 688060, tzinfo=utc), verbose_name='date created'),
        ),
    ]