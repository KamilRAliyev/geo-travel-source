from django.contrib import admin
from .models import *


class GuidePriceTabularInline (admin.TabularInline):
    model = GuidePriceTable


class GuideOrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message', 'created_at']

    class Meta:
        model = GuideOrder


class GuideAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    inlines = [GuidePriceTabularInline]

    class Meta:
        model = Guide


admin.site.register(Guide, GuideAdmin)
admin.site.register(GuideOrder, GuideOrderAdmin)
