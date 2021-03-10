from django.contrib import admin
from .models import *


class VehicleAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'price', 'created_at']

    class Meta:
        model = Vehicles


class VehicleOrderAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'vehicle_name', 'vehicle_url', 'price', 'order_date']

    class Meta:
        model = CarRentOrders


class TransferPriceTabularInline (admin.TabularInline):
    model = TransferPriceTable


class TransferStaticAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    inlines = [TransferPriceTabularInline]

    class Meta:
        model = TransferStaticPage


admin.site.register(TransferStaticPage, TransferStaticAdmin)
admin.site.register(Vehicles, VehicleAdmin)
admin.site.register(VehicleCategory)
admin.site.register(CarRentOrders,VehicleOrderAdmin)
admin.site.register(TransformCars)
# admin.site.register(TransferOrder)
