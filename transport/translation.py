from modeltranslation.translator import register, TranslationOptions
from .models import VehicleCategory, Vehicles, TransformCars, TransferStaticPage, TransferPriceTable


@register(VehicleCategory)
class VehicleCategoryTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(Vehicles)
class VehiclesTranslationOptions(TranslationOptions):
    fields = ("name", "body_style", "transmission", )


@register(TransformCars)
class TransformCarsTranslationOptions(TranslationOptions):
    fields = ("name", "category",)


@register(TransferStaticPage)
class TransferStaticPageTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(TransferPriceTable)
class TransferPriceTableTranslationOptions(TranslationOptions):
    fields = ("desc",)


