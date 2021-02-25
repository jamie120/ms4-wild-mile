# Generated by Django 3.1.7 on 2021-02-25 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Electric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twelve_volt_electrics', models.BooleanField()),
                ('usb_sockets', models.BooleanField()),
                ('leisure_battery', models.BooleanField()),
                ('split_charge_relay', models.BooleanField()),
                ('solar_panel', models.BooleanField()),
                ('inverter', models.BooleanField()),
                ('mains_electrics', models.BooleanField()),
                ('mains_charger', models.BooleanField()),
                ('mains_sign_off', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='camperconversion',
            name='electrics',
            field=models.ManyToManyField(to='conversions.Electric'),
        ),
    ]
