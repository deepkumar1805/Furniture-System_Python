# Generated by Django 4.1.5 on 2023-04-04 13:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0017_remove_checkout_payment_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='Payment_type',
            field=models.CharField(choices=[('COD', 'COD'), ('Online', 'Online')], default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='checkout',
            name='checkout_date',
            field=models.DateField(default=datetime.datetime(2023, 4, 4, 13, 50, 43, 438552, tzinfo=datetime.timezone.utc), verbose_name='expiration time (of ad)'),
        ),
    ]