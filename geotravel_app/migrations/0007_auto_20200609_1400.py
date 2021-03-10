# Generated by Django 3.0.2 on 2020-06-09 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geotravel_app', '0006_auto_20200609_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='name_bg',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='about_us_bg',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='company_address_bg',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='visaservices',
            name='name_bg',
            field=models.CharField(default='E-visa to Azerbaijan', max_length=200, null=True),
        ),
    ]
