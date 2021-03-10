from django.db import models
from froala_editor.fields import FroalaField


class VisaServices(models.Model):
    name = models.CharField(default='E-visa to Azerbaijan', max_length=200)
    content = FroalaField(theme='dark')
    content_ru = FroalaField(theme='dark', null=True, blank=True)
    content_es = FroalaField(theme='dark', null=True, blank=True)
    content_bg = FroalaField(theme='dark', null=True, blank=True)
    image = models.ImageField(upload_to='visa/e_visa', null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Visa Services'
        verbose_name_plural = 'Visa Services'


class EvisaOrders(models.Model):
    fullname = models.CharField(max_length=200, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    phone_number = models.CharField(max_length=20, blank=False, null=False)
    passport_scans = models.FileField(upload_to='visa/e_visa_order/passport_scans', blank=False, null=False)
    document_scans = models.FileField(upload_to='visa/e_visa_order/document_scans/', blank=False, null=False)

    def __str__(self):
        return f"{self.fullname}"

    class Meta:
        verbose_name = 'E-Visa Order'
        verbose_name_plural = 'E-Visa Orders'


class AboutUs(models.Model):
    name = models.CharField(max_length=200)
    content = FroalaField(theme='dark')
    content_ru = FroalaField(theme='dark', null=True, blank=True)
    content_es = FroalaField(theme='dark', null=True, blank=True)
    content_bg = FroalaField(theme='dark', null=True, blank=True)
    image = models.ImageField(upload_to='visa/e_visa', null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return f"about/{self.pk}"

    class Meta:
        verbose_name = 'About Us'
        verbose_name_plural = 'About Us'


class ContactFormInfo(models.Model):
    fullname = models.CharField(max_length=200, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    subject = models.CharField(max_length=200, blank=False, null=False)
    message = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fullname} | {self.email} | {self.subject}"

    class Meta:
        verbose_name = 'Contact Form Information'
        verbose_name_plural = 'Contact Form Information'


class CookiePolicy(models.Model):
    content = FroalaField(theme='dark')
    content_ru = FroalaField(theme='dark', null=True, blank=True)
    content_es = FroalaField(theme='dark', null=True, blank=True)
    content_bg = FroalaField(theme='dark', null=True, blank=True)

    def __str__(self):
        return "Cookie Policy"

    class Meta:
        verbose_name = 'Cookie Policy'
        verbose_name_plural = 'Cookie Policies'


class SiteSettings(models.Model):
    about_us = models.TextField()
    phone_num = models.CharField(max_length=20, null=False, blank=False)
    company_email = models.EmailField(max_length=200, blank=False, null=False)
    company_address = models.CharField(max_length=200, null=False, blank=False)
    facebook_link = models.CharField(max_length=200, null=False, blank=False)
    skype_link = models.CharField(max_length=200, null=False, blank=False)
    vk_link = models.CharField(max_length=200, null=False, blank=False)

    class Meta:
        verbose_name = 'Website settings'
        verbose_name_plural = 'Website settings'
