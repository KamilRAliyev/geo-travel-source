# Generated by Django 3.0.2 on 2020-01-20 00:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0007_tourorders'),
    ]

    operations = [
        migrations.CreateModel(
            name='TourSliderImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, null=True, upload_to='sliders/<function upload_image_path at 0x03631978>')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Tours', to='tours.Tour')),
            ],
            options={
                'verbose_name': 'Tour Slider Image',
                'verbose_name_plural': 'Tour Slider Images',
            },
        ),
    ]
