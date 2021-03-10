from django.contrib import admin
from .models import VisaServices, AboutUs, ContactFormInfo, SiteSettings, EvisaOrders, CookiePolicy
# Register your models here.

admin.site.site_header = "Geo Travel Admin Site"
class ContactFormInfoAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'email', 'subject', 'created_at']

    class Meta:
        model = ContactFormInfo


admin.site.register(VisaServices)
admin.site.register(AboutUs)
admin.site.register(ContactFormInfo, ContactFormInfoAdmin)
admin.site.register(SiteSettings)
admin.site.register(EvisaOrders)
admin.site.register(CookiePolicy)