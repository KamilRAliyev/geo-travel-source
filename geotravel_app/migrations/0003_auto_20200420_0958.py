# Generated by Django 3.0.2 on 2020-04-20 05:58

from django.db import migrations
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('geotravel_app', '0002_auto_20200418_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='content_ru',
            field=froala_editor.fields.FroalaField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='visaservices',
            name='content_ru',
            field=froala_editor.fields.FroalaField(blank=True, null=True),
        ),
    ]
