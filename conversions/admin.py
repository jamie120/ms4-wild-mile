from django.contrib import admin
from .models import CamperConversion, Category, Electric, ConversionImage

# Register your models here.


class ConversionImageInline(admin.TabularInline):
    model = ConversionImage
    extra = 3


class CamperConversionAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'registered_vehicle_type',
    )

    inlines = [ConversionImageInline, ]

    ordering = ('name',)


admin.site.register(CamperConversion, CamperConversionAdmin)
admin.site.register(Category)
admin.site.register(Electric)
