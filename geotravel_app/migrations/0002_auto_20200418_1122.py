# Generated by Django 3.0.2 on 2020-04-18 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geotravel_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='name_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='name_ru',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='about_us_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='about_us_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='company_address_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='company_address_ru',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='visaservices',
            name='name_en',
            field=models.CharField(default='E-visa to Azerbaijan', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='visaservices',
            name='name_ru',
            field=models.CharField(default='E-visa to Azerbaijan', max_length=200, null=True),
        ),
    ]
