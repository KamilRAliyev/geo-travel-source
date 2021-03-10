from django.db import models
from django.db.models.signals import pre_save
from .utils import unique_slug_generator
import os
from django.urls import reverse
from froala_editor.fields import FroalaField


def get_filename_ext(filepath):
    base_name=os.path.basename(filepath)
    name, ext = os.path.split(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    return f"tours/{name}/{name}{ext}"


class Guide(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    slug = models.SlugField(blank=True, unique=True)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    content = FroalaField(theme='dark')
    content_ru = FroalaField(theme='dark', null=True, blank=True)
    content_es = FroalaField(theme='dark', null=True, blank=True)
    content_bg = FroalaField(theme='dark', null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Guide'
        verbose_name_plural = 'Guides'


class GuideOrder(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    message = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"{self.email}|{self.message}"

    class Meta:
        verbose_name = 'Guide Order'
        verbose_name_plural = 'Guide Orders'


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver, sender=Guide)


class GuidePriceTable(models.Model):
    page = models.ForeignKey(Guide, on_delete=models.CASCADE, related_name='GuideTable')
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    desc = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.page.name} | Price: {self.price} Desc: {self.desc}"

    class Meta:
        verbose_name = 'Guide Price Table'
        verbose_name_plural = "Guide Price Tables"
