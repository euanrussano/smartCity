# Generated by Django 3.1.4 on 2021-01-01 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0003_auto_20210101_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('processed', 'Processed')], default='draft', editable=False, max_length=10),
        ),
    ]