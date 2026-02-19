from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline

from .models import (AboutBreadcrumb, AboutUniversity, AboutStatistic,
                     AboutHistory, AboutFunfact, AboutMission,
                     AboutMissionItem, AboutCampusTour, Leader)


# 1. Breadcrumb
@admin.register(AboutBreadcrumb)
class AboutBreadcrumbAdmin(TranslationAdmin):
    list_display = ['title', 'is_active']
    list_filter = ['is_active']

    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('title', 'parent_title', 'parent_link', 'background_image')
        }),
        ('Boshqa', {
            'fields': ('is_active',)
        }),
    )

    def has_add_permission(self, request):
        if AboutBreadcrumb.objects.exists():
            return False
        return True


# 2. Universitet haqida
class AboutStatisticInline(TranslationTabularInline):
    model = AboutStatistic
    extra = 1
    fields = ['value', 'description', 'icon', 'order', 'is_active']
    ordering = ['order']


@admin.register(AboutUniversity)
class AboutUniversityAdmin(TranslationAdmin):
    list_display = ['title', 'is_active']
    list_filter = ['is_active']

    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('title', 'description')
        }),
        ('Rasm', {
            'fields': ('image', 'image_alt_uz', 'image_alt_ru', 'image_alt_en')
        }),
        ('Boshqa', {
            'fields': ('is_active',)
        }),
    )

    def has_add_permission(self, request):
        if AboutUniversity.objects.exists():
            return False
        return True


@admin.register(AboutStatistic)
class AboutStatisticAdmin(TranslationAdmin):
    list_display = ['value', 'description', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    ordering = ['order']

    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('value', 'description', 'icon')
        }),
        ('Boshqa', {
            'fields': ('order', 'is_active')
        }),
    )


# 3. Tarix
@admin.register(AboutHistory)
class AboutHistoryAdmin(TranslationAdmin):
    list_display = ['title', 'is_active']
    list_filter = ['is_active']

    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('title', 'content', 'content_2')
        }),
        ('Rasm', {
            'fields': ('image', 'image_alt_uz', 'image_alt_ru', 'image_alt_en')
        }),
        ('Boshqa', {
            'fields': ('is_active',)
        }),
    )

    def has_add_permission(self, request):
        if AboutHistory.objects.exists():
            return False
        return True


# 4. Funfact
@admin.register(AboutFunfact)
class AboutFunfactAdmin(TranslationAdmin):
    list_display = ['value', 'description', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    ordering = ['order']

    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('value', 'description')
        }),
        ('Boshqa', {
            'fields': ('order', 'is_active')
        }),
    )


# 5. Missiya
@admin.register(AboutMission)
class AboutMissionAdmin(TranslationAdmin):
    list_display = ['title', 'is_active']
    list_filter = ['is_active']

    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('title',)
        }),
        ('Boshqa', {
            'fields': ('is_active',)
        }),
    )

    def has_add_permission(self, request):
        if AboutMission.objects.exists():
            return False
        return True


@admin.register(AboutMissionItem)
class AboutMissionItemAdmin(TranslationAdmin):
    list_display = ['title', 'side', 'order', 'is_active']
    list_filter = ['is_active', 'side']
    list_editable = ['side', 'order', 'is_active']
    ordering = ['order']

    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('title', 'description', 'side')
        }),
        ('Rasm', {
            'fields': ('image', 'image_alt_uz', 'image_alt_ru', 'image_alt_en')
        }),
        ('Boshqa', {
            'fields': ('order', 'is_active')
        }),
    )


# 6. Kampus sayohati
@admin.register(AboutCampusTour)
class AboutCampusTourAdmin(TranslationAdmin):
    list_display = ['title', 'is_active']
    list_filter = ['is_active']

    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('title', 'description')
        }),
        ('Video', {
            'fields': ('video_url', 'video_thumbnail')
        }),
        ('Tugma', {
            'fields': ('button_text', 'button_link')
        }),
        ('Boshqa', {
            'fields': ('is_active',)
        }),
    )

    def has_add_permission(self, request):
        if AboutCampusTour.objects.exists():
            return False
        return True


# 7. Rahbariyat
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