# Generated by Django 3.0.2 on 2020-04-20 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guides', '0007_guide_content_ru'),
    ]

    operations = [
        migrations.AddField(
            model_name='guide',
            name='name_es',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='guidepricetable',
            name='desc_es',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
