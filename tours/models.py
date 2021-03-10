from django.db import models
from django.db.models.signals import pre_save
from .utils import unique_slug_generator
import os
from django.urls import reverse
from froala_editor.fields import FroalaField


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.split(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    return f"tours/{name}/{name}{ext}"


# Create your models here.
class TourCategory(models.Model):
    name = models.CharField(max_length=200)
    order = models.IntegerField(blank=False, null=False, default=0)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse("category", kwargs={"pk":self.pk})

    class Meta:
        verbose_name = 'Tour Category'
        verbose_name_plural = 'Tour Categories'


class Tour(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    slug = models.SlugField(blank=True, unique=True)
    description = models.CharField(max_length=400, blank=False, null=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=False)
    duration = models.IntegerField(blank=False, null=False)
    city = models.CharField(max_length=200)
    rating = models.IntegerField(default=5)
    category = models.ForeignKey('TourCategory', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    content = FroalaField(null=True, blank=True, theme='dark' )
    content_ru = FroalaField(null=True, blank=True, theme='dark')
    content_es = FroalaField(theme='dark', null=True, blank=True)
    content_bg = FroalaField(theme='dark', null=True, blank=True)

    def __str__(self):
        return f"{self.name} | {self.description}"

    def get_absolute_url(self):
        return reverse("tour_details", kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Tour'
        verbose_name_plural = 'Tours'


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver, sender=Tour)


class TourOrders(models.Model):
    tour_name = models.CharField(blank=False,null=False, max_length=200)
    full_name = models.CharField(blank=False,null=False, max_length=200)
    email = models.EmailField(blank=False, null=False)
    order_date = models.DateTimeField(auto_now_add=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)

    def __str__(self):
        return f"Tour: {self.tour_name}, Person: {self.full_name}, Order date: {self.order_date}"

    class Meta:
        verbose_name = 'Tour Order'
        verbose_name_plural = "Tour Orders"


class TourSliderImages(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='Tours')
    images = models.ImageField(upload_to=upload_image_path, blank=True, null=True)

    def __str__(self):
        return f"Tour: {self.tour}, Image {self.images.name}"

    class Meta:
        verbose_name = 'Tour Slider Image'
        verbose_name_plural = "Tour Slider Images"


class TourComments(models.Model):
    full_name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='Tour')

    def __str__(self):
        return f"Name: {self.full_name}, Comment {self.comment[:100]}"

    class Meta:
        verbose_name = 'Tour Comment'
        verbose_name_plural = "Tour Comments"


class TourPriceTable(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='TourTable')
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    desc = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.tour.name} | Price: {self.price} Desc: {self.desc}"

    class Meta:
        verbose_name = 'Tour Price Table'
        verbose_name_plural = "Tour Price Tables"
