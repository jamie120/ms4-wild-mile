from django.contrib import admin
from .models import CamperConversion, Category, Electric, PostImage


class ConversionImageInline(admin.TabularInline):
    model = PostImage
    extra = 3


class CamperConversionAdmin(admin.ModelAdmin):
    list_display = (
        'listing_title',
        'price',
        'registered_vehicle_type',
    )

    inlines = [ConversionImageInline, ]

    ordering = ('name',)


admin.site.register(CamperConversion, CamperConversionAdmin)
admin.site.register(Category)
admin.site.register(Electric)
