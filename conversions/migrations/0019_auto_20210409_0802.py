# Generated by Django 3.1.7 on 2021-04-09 08:02

from django.db import migrations, models
import smartfields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('conversions', '0018_auto_20210408_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camperconversion',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='postimage',
            name='image',
            field=smartfields.fields.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
