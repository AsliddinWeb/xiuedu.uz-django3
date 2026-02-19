from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Leader


@admin.register(Leader)
class LeaderAdmin(TranslationAdmin):
    list_display = ['full_name', 'position', 'order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['full_name', 'position']
    list_editable = ['order', 'is_active']
    prepopulated_fields = {'slug': ('full_name',)}

    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('full_name', 'slug', 'position', 'degree')
        }),
        ('Rasm', {
            'fields': ('image', 'image_alt_uz', 'image_alt_ru', 'image_alt_en')
        }),
        ('Biografiya', {
            'fields': ('short_bio', 'biography', 'education', 'expertise')
        }),
        ('Darslar va nashrlari', {
            'fields': ('courses', 'publications'),
            'classes': ('collapse',)
        }),
        ('Aloqa', {
            'fields': ('phone', 'email', 'reception_days')
        }),
        ('Ijtimoiy tarmoqlar', {
            'fields': ('facebook_link', 'linkedin_link', 'telegram_link', 'youtube_link', 'instagram_link'),
            'classes': ('collapse',)
        }),
        ('Boshqa', {
            'fields': ('order', 'is_active')
        }),
    )