# Generated by Django 3.1.4 on 2020-12-14 02:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('iot', '0002_auto_20201213_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 14, 2, 50, 32, 66759, tzinfo=utc), verbose_name='date created'),
        ),
    ]
