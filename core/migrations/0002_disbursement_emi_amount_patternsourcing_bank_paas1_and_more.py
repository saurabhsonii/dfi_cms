# Generated by Django 4.1.4 on 2023-09-11 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='disbursement',
            name='emi_amount',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='patternsourcing',
            name='bank_paas1',
            field=models.FileField(blank=True, null=True, upload_to='bank/'),
        ),
        migrations.AddField(
            model_name='patternsourcing',
            name='bank_paas2',
            field=models.FileField(blank=True, null=True, upload_to='bank/'),
        ),
        migrations.AddField(
            model_name='patternsourcing',
            name='bank_paasbook',
            field=models.FileField(blank=True, null=True, upload_to='bank/'),
        ),
        migrations.AddField(
            model_name='patternsourcing',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='vehicledocuments',
            name='applicant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.loandetails'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vehicledocuments',
            name='bank_noc',
            field=models.FileField(blank=True, null=True, upload_to='VehicleDocuments/'),
        ),
        migrations.AlterField(
            model_name='vehicledocuments',
            name='form_28',
            field=models.FileField(blank=True, null=True, upload_to='VehicleDocuments/'),
        ),
        migrations.AlterField(
            model_name='vehicledocuments',
            name='form_29_30',
            field=models.FileField(blank=True, null=True, upload_to='VehicleDocuments/'),
        ),
        migrations.AlterField(
            model_name='vehicledocuments',
            name='form_34_35',
            field=models.FileField(blank=True, null=True, upload_to='VehicleDocuments/'),
        ),
        migrations.AlterField(
            model_name='vehicledocuments',
            name='insurance',
            field=models.FileField(blank=True, null=True, upload_to='VehicleDocuments/'),
        ),
        migrations.AlterField(
            model_name='vehicledocuments',
            name='rc_card',
            field=models.FileField(blank=True, null=True, upload_to='VehicleDocuments/'),
        ),
        migrations.AlterField(
            model_name='vehicledocuments',
            name='rto_noc',
            field=models.FileField(blank=True, null=True, upload_to='VehicleDocuments/'),
        ),
    ]
