# Generated by Django 3.1.7 on 2021-02-26 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversions', '0006_auto_20210226_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camperconversion',
            name='unladen_weight_verified',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]