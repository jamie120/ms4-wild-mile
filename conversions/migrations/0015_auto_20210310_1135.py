# Generated by Django 3.1.7 on 2021-03-10 11:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('conversions', '0014_auto_20210310_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camperconversion',
            name='unique_ref',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
