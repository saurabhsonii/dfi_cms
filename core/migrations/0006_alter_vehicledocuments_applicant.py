# Generated by Django 4.1.4 on 2023-09-05 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_appcant_vehicledocuments_applicant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicledocuments',
            name='applicant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.vehicledetails'),
        ),
    ]