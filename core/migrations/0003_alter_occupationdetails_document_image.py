# Generated by Django 4.1.4 on 2023-09-05 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_occupationdetails_document_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occupationdetails',
            name='document_image',
            field=models.CharField(max_length=500),
        ),
    ]
