# Generated by Django 3.1.7 on 2021-03-09 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversions', '0010_auto_20210309_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimage',
            name='image',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]