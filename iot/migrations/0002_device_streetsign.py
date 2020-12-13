# Generated by Django 3.1.4 on 2020-12-13 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.IntegerField(default=0)),
                ('longitude', models.IntegerField(default=0)),
                ('status', models.CharField(max_length=200)),
                ('enabled', models.BooleanField()),
                ('account', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='iot.account')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='iot.city')),
            ],
        ),
        migrations.CreateModel(
            name='StreetSign',
            fields=[
                ('device_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='iot.device')),
                ('text', models.CharField(max_length=200)),
            ],
            bases=('iot.device',),
        ),
    ]
