# Generated by Django 3.0.2 on 2020-01-12 08:29

from django.db import migrations, models
import django.utils.timezone
import tours.models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0003_auto_20200111_0520'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tour',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=tours.models.upload_image_path),
        ),
    ]
