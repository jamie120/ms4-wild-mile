# Generated by Django 3.1.7 on 2021-04-22 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversions', '0024_auto_20210422_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camperconversion',
            name='vehicle_height',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
        migrations.AlterField(
            model_name='camperconversion',
            name='vehicle_width',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
    ]
