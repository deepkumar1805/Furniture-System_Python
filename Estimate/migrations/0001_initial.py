# Generated by Django 4.1.7 on 2023-03-29 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estimate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apartment_type', models.CharField(choices=[('2bhk', '2bhk'), ('3bhk', '3bhK'), ('3.5bhk', '3.5bhk'), ('4bhk', '4bhk')], max_length=10)),
                ('bedroomes_type', models.CharField(choices=[('Master Room', 'Master Room'), ('Home Office Study', 'Home Office Study'), ('Parents', 'Parents'), ('Kids Bedroom', 'Kids Bedroom'), ('Kids Room 1', 'Kids Room 1'), ('Kids Room 2', 'Kids Room 2'), ('Guest Bedroom', 'Guest Bedroom')], max_length=50)),
                ('modular_kitchen', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('Carpet_area_in_sqft', models.CharField(max_length=10)),
            ],
        ),
    ]
