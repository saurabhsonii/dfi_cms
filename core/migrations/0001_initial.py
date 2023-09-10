# Generated by Django 4.1.4 on 2023-09-10 05:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(max_length=75)),
                ('phone_number', models.PositiveIntegerField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=350, null=True)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile/')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('user_role', models.CharField(choices=[('agent', 'AGENT'), ('manager', 'MANAGER')], max_length=50)),
                ('is_agent', models.BooleanField(blank=True, null=True)),
                ('parent_id', models.IntegerField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to.', related_name='custom_user_groups', related_query_name='custom_user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='custom_user_permissions', related_query_name='custom_user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('subject', models.CharField(blank=True, max_length=250, null=True)),
                ('phone_number', models.CharField(max_length=12)),
                ('message', models.TextField()),
                ('is_seen', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='applicant-details/')),
            ],
        ),
        migrations.CreateModel(
            name='LoanDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_type', models.CharField(blank=True, max_length=150, null=True)),
                ('vehicle_name', models.CharField(blank=True, max_length=150, null=True)),
                ('vehicle_model', models.CharField(blank=True, max_length=250, null=True)),
                ('vehicle_number', models.CharField(blank=True, max_length=150, null=True)),
                ('home_lap', models.CharField(blank=True, max_length=200, null=True)),
                ('home_home', models.CharField(blank=True, max_length=200, null=True)),
                ('business_name', models.CharField(blank=True, max_length=200, null=True)),
                ('business_type', models.CharField(blank=True, max_length=200, null=True)),
                ('micro_name', models.CharField(blank=True, max_length=200, null=True)),
                ('micro_type', models.CharField(blank=True, max_length=200, null=True)),
                ('gold_type', models.CharField(blank=True, max_length=150, null=True)),
                ('gold_quantity', models.FloatField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('parent_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=150)),
                ('state_code', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleDocuments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rc_card', models.FileField(upload_to='VehicleDocuments/')),
                ('insurance', models.FileField(upload_to='VehicleDocuments/')),
                ('form_29_30', models.FileField(upload_to='VehicleDocuments/')),
                ('form_34_35', models.FileField(upload_to='VehicleDocuments/')),
                ('bank_noc', models.FileField(upload_to='VehicleDocuments/')),
                ('rto_noc', models.FileField(upload_to='VehicleDocuments/')),
                ('form_28', models.FileField(upload_to='VehicleDocuments/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('applicant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.loandetails')),
            ],
        ),
        migrations.CreateModel(
            name='PersonalDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('mr', 'MR'), ('mrs', 'MRS'), ('other', 'OTHER')], max_length=150)),
                ('applicant_name', models.CharField(max_length=150)),
                ('father_name', models.CharField(max_length=150)),
                ('mother_name', models.CharField(blank=True, max_length=150, null=True)),
                ('applicant_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('contact', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=350)),
                ('city', models.CharField(max_length=50)),
                ('county', models.CharField(default='INDIA', max_length=150)),
                ('pincode', models.CharField(max_length=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.state')),
                ('vehicle_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.loandetails')),
            ],
        ),
        migrations.CreateModel(
            name='OccupationDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.personaldetails')),
                ('document_image', models.ManyToManyField(to='core.documentimages')),
            ],
        ),
        migrations.CreateModel(
            name='Disbursement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=150)),
                ('loan_amount', models.CharField(max_length=15)),
                ('net_amount', models.CharField(max_length=15)),
                ('emi_duration', models.CharField(choices=[('24 month', '24'), ('36 month', '36'), ('48 month', '48'), ('60 month', '60')], max_length=50)),
                ('status', models.BooleanField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('vehicle_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.loandetails')),
            ],
        ),
    ]
