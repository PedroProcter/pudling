# Generated by Django 4.0.3 on 2022-04-06 17:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_alter_booking_begins_at_alter_booking_ends_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='begins_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 6, 13, 46, 43, 74565)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='ends_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 6, 13, 46, 43, 74565)),
        ),
    ]
