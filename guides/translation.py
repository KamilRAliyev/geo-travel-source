from .models import Guide, GuidePriceTable
from modeltranslation.translator import register, TranslationOptions


@register(Guide)
class GuideTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(GuidePriceTable)
class GuidePriceTableTranslationOptions(TranslationOptions):
    fields = ("desc",)
