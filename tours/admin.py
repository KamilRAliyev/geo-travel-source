from django.contrib import admin
from .models import *


# Register your models here.


class SliderTabularInline(admin.TabularInline):
    model = TourSliderImages


class CommentsTabularInline(admin.TabularInline):
    model = TourComments


class TourPriceTabularInline(admin.TabularInline):
    model = TourPriceTable


class TourAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'created_at']
    list_filter = ['created_at']
    inlines = [SliderTabularInline, TourPriceTabularInline, CommentsTabularInline]
    readonly_fields = ['created_at']

    class Meta:
        model = Tour


class TourOrderAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'tour_name', 'price', 'order_date',]
    list_filter = ['order_date']
    readonly_fields = ['full_name', 'email', 'tour_name', 'price', 'order_date',]

    class Meta:
        model = Tour


admin.site.register(Tour, TourAdmin)
admin.site.register(TourOrders, TourOrderAdmin)
admin.site.register(TourCategory)
