# Generated by Django 3.1.7 on 2021-03-10 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_auto_20210305_0949'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlineitem',
            name='listing_uuid',
            field=models.CharField(blank=True, max_length=36, null=True),
        ),
    ]
