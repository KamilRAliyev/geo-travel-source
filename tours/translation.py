from .models import Tour, TourCategory, TourPriceTable
from modeltranslation.translator import register, TranslationOptions

@register(Tour)
class TourTranslationOptions(TranslationOptions):
    fields = ("name","description","city")


@register(TourCategory)
class TourCategoryTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(TourPriceTable)
class TourPriceTableTranslationOptions(TranslationOptions):
    fields = ("desc",)

