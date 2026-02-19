from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import GalleryImage


@admin.register(GalleryImage)
class GalleryImageAdmin(TranslationAdmin):
    list_display = ['title', 'order', 'is_featured', 'is_active', 'created_at']
    list_filter = ['is_active', 'is_featured']
    search_fields = ['title']
    list_editable = ['order', 'is_featured', 'is_active']
    ordering = ['order', '-created_at']

    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('title', 'image', 'image_large')
        }),
        ('Boshqa', {
            'fields': ('order', 'is_featured', 'is_active')
        }),
    )