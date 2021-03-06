# Generated by Django 3.0.2 on 2020-04-17 03:51

from django.db import migrations, models
import django.db.models.deletion
import froala_editor.fields
import transport.models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0004_auto_20200226_0415'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransferStaticPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=transport.models.upload_image_path)),
                ('content', froala_editor.fields.FroalaField()),
            ],
            options={
                'verbose_name': 'Transfer Static Page',
                'verbose_name_plural': 'Transfer Static Pages',
            },
        ),
        migrations.CreateModel(
            name='TransferStaticPageOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'Transfer Static Page Order',
                'verbose_name_plural': 'Transfer Static Page Orders',
            },
        ),
        migrations.CreateModel(
            name='TransferPriceTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('desc', models.CharField(max_length=50)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TransferTable', to='transport.TransferStaticPage')),
            ],
            options={
                'verbose_name': 'Transfer Price Table',
                'verbose_name_plural': 'Transfer Price Tables',
            },
        ),
    ]
