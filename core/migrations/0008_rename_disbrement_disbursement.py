# Generated by Django 4.1.4 on 2023-09-06 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_disbrement_vehicle_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Disbrement',
            new_name='Disbursement',
        ),
    ]