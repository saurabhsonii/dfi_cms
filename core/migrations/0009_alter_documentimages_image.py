# Generated by Django 4.1.4 on 2023-09-06 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_rename_disbrement_disbursement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentimages',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='applicant-details/'),
        ),
    ]
