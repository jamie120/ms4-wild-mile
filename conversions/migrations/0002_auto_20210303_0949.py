# Generated by Django 3.1.7 on 2021-03-03 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conversions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Electric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
            ],
        ),
        migrations.RenameField(
            model_name='camperconversion',
            old_name='images',
            new_name='main_image',
        ),
        migrations.RemoveField(
            model_name='camperconversion',
            name='main_image_url',
        ),
        migrations.AddField(
            model_name='camperconversion',
            name='beds_description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='camperconversion',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='conversions.category'),
        ),
        migrations.AddField(
            model_name='camperconversion',
            name='gas_sign_off',
            field=models.CharField(blank=True, choices=[('GAS_SAFE_CERT', 'Gas Safe Certificate'), ('NA', 'None'), ('NO_GAS', 'Gas Free')], default='None', max_length=254),
        ),
        migrations.AddField(
            model_name='camperconversion',
            name='listing_title',
            field=models.CharField(default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='camperconversion',
            name='location',
            field=models.CharField(default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='camperconversion',
            name='phone_number',
            field=models.IntegerField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='camperconversion',
            name='vehicle_height',
            field=models.IntegerField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='camperconversion',
            name='vehicle_make_and_model',
            field=models.CharField(default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='camperconversion',
            name='vehicle_width',
            field=models.IntegerField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='camperconversion',
            name='year',
            field=models.IntegerField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='camperconversion',
            name='unladen_weight',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='camperconversion',
            name='unladen_weight_verified',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.CreateModel(
            name='ConversionImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('conversion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='conversions.camperconversion')),
            ],
        ),
        migrations.AddField(
            model_name='camperconversion',
            name='electrics',
            field=models.ManyToManyField(to='conversions.Electric'),
        ),
    ]