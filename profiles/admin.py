from django.contrib import admin
from .models import SavedListings, UserProfile

# Register your models here.


class SavedListingsInline(admin.TabularInline):
    model = SavedListings


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
    )

    inlines = [SavedListingsInline, ]


admin.site.register(UserProfile, UserProfileAdmin)
