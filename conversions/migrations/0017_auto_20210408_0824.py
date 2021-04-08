# Generated by Django 3.1.7 on 2021-04-08 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversions', '0016_camperconversion_current_mileage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camperconversion',
            name='registered_vehicle_type',
            field=models.CharField(choices=[('P_VAN', 'Panel Van'), ('C_VAN_REFIT', 'Motor Caravan'), ('SPEC_VEH', 'Special Vehicle'), ('OTHER', 'Other - See description')], max_length=254),
        ),
        migrations.AlterField(
            model_name='postimage',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]