# Generated by Django 4.1.4 on 2023-08-26 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_customuser_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='is_seen',
            field=models.BooleanField(default=False),
        ),
    ]