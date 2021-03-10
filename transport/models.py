from django.db import models
from .utils import unique_slug_generator
from django.db.models.signals import pre_save
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


class VehicleCategory(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Vehicle Category'
        verbose_name_plural = 'Vehicle Categories'


class Vehicles(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    slug = models.SlugField(blank=True, unique=True)
    category = models.ForeignKey('VehicleCategory', on_delete=models.CASCADE)
    passenger = models.IntegerField(default=4, null=False, blank=False)
    year = models.CharField(max_length=4, blank=False, null=False)
    body_style = models.CharField(max_length=100, blank=False, null=False)
    engine = models.CharField(max_length=100, blank=False, null=False)
    transmission = models.CharField(max_length=100, blank=False, null=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=False)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    content = FroalaField(null=True, blank=True, theme='dark')
    content_ru = FroalaField(null=True, blank=True, theme='dark')
    content_es = FroalaField(theme='dark', null=True, blank=True)
    content_bg = FroalaField(theme='dark', null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse("vehicle_details", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver, sender=Vehicles)


class CarRentOrders(models.Model):
    vehicle_name = models.CharField(blank=False, null=False, max_length=200)
    vehicle_url = models.CharField(blank=False, null=False, max_length=300)
    full_name = models.CharField(blank=False, null=False, max_length=200)
    email = models.EmailField(blank=False, null=False)
    order_date = models.DateTimeField(auto_now_add=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    start_date = models.DateField(blank=False, null=False)
    end_date = models.DateField(blank=False, null=False)

    def __str__(self):
        return f"Tour: {self.vehicle_name}, Person: {self.full_name}, Order date: {self.order_date}"

    class Meta:
        verbose_name = 'Car Rent Order'
        verbose_name_plural = "Car Rent Orders"


class TransformCars(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    category = models.CharField(max_length=200, blank=False, null=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=False)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    passenger = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Transform Car'
        verbose_name_plural = "Transform Cars"


class TransferOrder(models.Model):
    fr = models.CharField(max_length=400, blank=False, null=False)
    to = models.CharField(max_length=400, blank=False, null=False)
    transform_car = models.ForeignKey('TransformCars', on_delete=models.CASCADE, blank=False, null=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=False)
    passenger_number_one_way = models.IntegerField(blank=False, null=False)
    passenger_number_two_way = models.IntegerField(blank=True, null=True)
    flight_one_way = models.CharField(max_length=400, blank=False, null=False)
    flight_two_way = models.CharField(max_length=400, blank=True, null=True)
    full_name = models.CharField(max_length=200, blank=False, null=False)
    phone_number = models.CharField(max_length=80, blank=False, null=False)
    plate_info = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(blank=False, null=False)
    date_arrival = models.DateField(blank=False, null=False)
    date_arrival_time = models.TimeField(blank=False, null=False)
    date_arrival_two_way = models.DateField(blank=True, null=True)
    date_arrival_time_two_way = models.TimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.full_name}| {self.date_arrival}:{self.date_arrival_time}"

    class Meta:
        verbose_name = 'Transfer Order'
        verbose_name_plural = "Transfer Orders"


class TransferStaticPage(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    slug = models.SlugField(blank=True, unique=True)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    content = FroalaField(theme='dark')
    content_ru = FroalaField(null=True, blank=True, theme='dark')
    content_es = FroalaField(theme='dark', null=True, blank=True)
    content_bg = FroalaField(theme='dark', null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Transfer Static Page'
        verbose_name_plural = 'Transfer Static Pages'


class TransferStaticPageOrder(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    message = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"{self.email}|{self.message}"

    class Meta:
        verbose_name = 'Transfer Static Page Order'
        verbose_name_plural = 'Transfer Static Page Orders'


pre_save.connect(product_pre_save_receiver, sender=TransferStaticPage)


class TransferPriceTable(models.Model):
    page = models.ForeignKey(TransferStaticPage, on_delete=models.CASCADE, related_name='TransferTable')
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    desc = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.page.name} | Price: {self.price} Desc: {self.desc}"

    class Meta:
        verbose_name = 'Transfer Price Table'
        verbose_name_plural = "Transfer Price Tables"
