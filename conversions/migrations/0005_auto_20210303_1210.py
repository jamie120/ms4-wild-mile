# Generated by Django 3.1.7 on 2021-03-03 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversions', '0004_auto_20210303_1123'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ConversionImage',
            new_name='PostImage',
        ),
    ]