# Generated by Django 4.1.5 on 2023-04-04 11:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0010_alter_checkout_checkout_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='OrderPrice',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='checkout',
            name='checkout_date',
            field=models.DateField(default=datetime.datetime(2023, 4, 4, 11, 3, 10, 325020, tzinfo=datetime.timezone.utc), verbose_name='expiration time (of ad)'),
        ),
    ]