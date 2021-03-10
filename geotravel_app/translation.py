from .models import VisaServices, AboutUs, SiteSettings
from modeltranslation.translator import register, TranslationOptions


@register(VisaServices)
class VisaServicesTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(AboutUs)
class AboutUsTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(SiteSettings)
class SiteSettingsTranslationOptions(TranslationOptions):
    fields = ("about_us", "company_address")
