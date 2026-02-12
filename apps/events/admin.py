from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline

from .models import Event, EventFeature


class EventFeatureInline(TranslationTabularInline):
    model = EventFeature
    extra = 1
    fields = ['title', 'description', 'order']
    ordering = ['order', 'title']


@admin.register(Event)
class EventAdmin(TranslationAdmin):
    list_display = ['title', 'event_date', 'event_time', 'cost', 'is_free', 'total_slots', 'booked_slots', 'is_featured', 'is_active']
    list_filter = ['is_active', 'is_featured', 'is_free', 'event_date']
    search_fields = ['title', 'description', 'venue_name']
    list_editable = ['is_featured', 'is_active']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [EventFeatureInline]

    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('title', 'slug', 'short_description', 'description')
        }),
        ('Rasm', {
            'fields': ('image', 'image_alt_uz', 'image_alt_ru', 'image_alt_en')
        }),
        ('Sana va vaqt', {
            'fields': ('event_date', 'event_time', 'end_time')
        }),
        ('Narx va o\'rinlar', {
            'fields': ('is_free', 'cost', 'total_slots', 'booked_slots')
        }),
        ('Tugma', {
            'fields': ('button_text', 'button_link')
        }),
        ('Joy ma\'lumotlari', {
            'fields': ('venue_name', 'venue_address', 'venue_phone', 'venue_website', 'venue_map_embed')
        }),
        ('Ijtimoiy tarmoqlar', {
            'fields': ('facebook_link', 'instagram_link', 'linkedin_link', 'telegram_link', 'youtube_link'),
            'classes': ('collapse',)
        }),
        ('Boshqa', {
            'fields': ('is_featured', 'is_active')
        }),
    )