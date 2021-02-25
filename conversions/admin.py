from django.contrib import admin
from .models import CamperConversion, Category, Electric

# Register your models here.


class CamperConversionAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'registered_vehicle_type',
    )

    ordering = ('name',)

admin.site.register(CamperConversion, CamperConversionAdmin)
admin.site.register(Category)
admin.site.register(Electric)
