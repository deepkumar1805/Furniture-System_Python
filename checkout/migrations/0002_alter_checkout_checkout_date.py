# Generated by Django 4.1.7 on 2023-03-29 10:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='checkout_date',
            field=models.DateField(default=datetime.datetime(2023, 4, 28, 10, 50, 29, 462483, tzinfo=datetime.timezone.utc), verbose_name='expiration time (of ad)'),
        ),
    ]