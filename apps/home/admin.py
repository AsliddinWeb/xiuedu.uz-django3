from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import (BannerSettings, BannerVideo, BannerSlider, BannerNavigation, AboutSection,
                     StatisticItem, NewsStaticTexts, Partner, LicenseStaticTexts, LicenseItem, ProgramStaticTexts,
                     StudentLifeStaticTexts, StudentLifeItem, DirectionStaticTexts, EventStaticTexts)


@admin.register(BannerSettings)
class BannerSettingsAdmin(admin.ModelAdmin):
    list_display = ['show_video', 'is_active']
    list_filter = ['is_active', 'show_video']

    fieldsets = (
        ('Sozlamalar', {
            'fields': ('show_video', 'is_active')
        }),
    )

    def has_add_permission(self, request):
        if BannerSettings.objects.exists():
            return False
        return True


@admin.register(BannerVideo)
class BannerVideoAdmin(TranslationAdmin):
    list_display = ['title', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'subtitle']

    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('title', 'subtitle')
        }),
        ('Video', {
            'fields': ('video_file', 'poster_image')
        }),
        ('Tugma', {
            'fields': ('button_text', 'button_link')
        }),
        ('Boshqa', {
            'fields': ('is_active',)
        }),
    )

    def has_add_permission(self, request):
        if BannerVideo.objects.exists():
            return False
        return True


@admin.register(BannerSlider)
class BannerSliderAdmin(TranslationAdmin):
    list_display = ['title', 'order', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'subtitle', 'description']
    list_editable = ['order', 'is_active']
    ordering = ['order', '-created_at']

    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('title', 'subtitle', 'description')
        }),
        ('Rasm', {
            'fields': ('image', 'image_alt_uz', 'image_alt_ru', 'image_alt_en')
        }),
        ('Tugma', {
            'fields': ('button_text', 'button_link')
        }),
        ('Boshqa', {
            'fields': ('order', 'is_active')
        }),
    )


@admin.register(BannerNavigation)
class BannerNavigationAdmin(TranslationAdmin):
    list_display = ['title', 'description', 'order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title', 'description']
    list_editable = ['order', 'is_active']
    ordering = ['order', 'title']

    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('title', 'description', 'link', 'icon')
        }),
        ('Boshqa', {
            'fields': ('order', 'is_active')
        }),
    )


@admin.register(AboutSection)
class AboutSectionAdmin(TranslationAdmin):
    list_display = ['title', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'subtitle', 'description']

    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('subtitle', 'title', 'description', 'description_2')
        }),
        ('Chap taraf rasmlari', {
            'fields': ('left_image_1', 'left_image_2')
        }),
        ('Aylanuvchi matn', {
            'fields': ('circle_text',)
        }),
        ('Missiya', {
            'fields': ('mission_title', 'mission_icon')
        }),
        ('Viziya', {
            'fields': ('vision_title', 'vision_icon')
        }),
        ('Tugma', {
            'fields': ('button_text', 'button_link')
        }),
        ('Asosiy rasm (yuqorida)', {
            'fields': ('image', 'image_alt_uz', 'image_alt_ru', 'image_alt_en')
        }),
        ('Boshqa', {
            'fields': ('is_active',)
        }),
    )

    def has_add_permission(self, request):
        if AboutSection.objects.exists():
            return False
        return True


@admin.register(StatisticItem)
class StatisticItemAdmin(TranslationAdmin):
    list_display = ['title', 'description', 'order', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['order', 'is_active']
    ordering = ['order', 'title']

    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('title', 'description', 'icon')
        }),
        ('Boshqa', {
            'fields': ('order', 'is_active')
        }),
    )


@admin.register(NewsStaticTexts)
class NewsStaticTextsAdmin(TranslationAdmin):
    list_display = ['title', 'is_active']
    list_filter = ['is_active']

    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('title', 'description')
        }),
        ('Tugma', {
            'fields': ('button_text', 'button_link')
        }),
        ('Boshqa', {
            'fields': ('is_active',)
        }),
    )

    def has_add_permission(self, request):
        if NewsStaticTexts.objects.exists():
            return False
        return True


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'is_active', 'created_at']
    list_filter = ['is_active']
    search_fields = ['name']
    list_editable = ['order', 'is_active']
    ordering = ['order', 'name']

    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('name', 'logo', 'link')
        }),
        ('Boshqa', {
            'fields': ('order', 'is_active')
        }),
    )


@admin.register(LicenseStaticTexts)
class LicenseStaticTextsAdmin(TranslationAdmin):
    list_display = ['title', 'is_active']
    list_filter = ['is_active']

    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('title',)
        }),
        ('Tugma', {
            'fields': ('button_text', 'button_link')
        }),
        ('Boshqa', {
            'fields': ('is_active',)
        }),
    )

    def has_add_permission(self, request):
        if LicenseStaticTexts.objects.exists():
            return False
        return True


@admin.register(LicenseItem)
class LicenseItemAdmin(TranslationAdmin):
    list_display = ['title', 'order', 'is_active', 'created_at']
    list_filter = ['is_active']
    search_fields = ['title', 'description']
    list_editable = ['order', 'is_active']
    ordering = ['order', '-created_at']

    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('title', 'description', 'background_image')
        }),
        ('Tugma', {
            'fields': ('button_text', 'button_link')
        }),
        ('Boshqa', {
            'fields': ('order', 'is_active')
        }),
    )


@admin.register(ProgramStaticTexts)
class ProgramStaticTextsAdmin(TranslationAdmin):
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
        if ProgramStaticTexts.objects.exists():
            return False
        return True



@admin.register(StudentLifeStaticTexts)
class StudentLifeStaticTextsAdmin(TranslationAdmin):
    list_display = ['title', 'is_active']
    list_filter = ['is_active']

    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('title', 'title_highlight', 'description')
        }),
        ('Boshqa', {
            'fields': ('is_active',)
        }),
    )

    def has_add_permission(self, request):
        if StudentLifeStaticTexts.objects.exists():
            return False
        return True


@admin.register(StudentLifeItem)
class StudentLifeItemAdmin(TranslationAdmin):
    list_display = ['title', 'order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title']
    list_editable = ['order', 'is_active']
    ordering = ['order', 'title']

    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('title', 'link')
        }),
        ('Rasm', {
            'fields': ('image', 'image_alt_uz', 'image_alt_ru', 'image_alt_en')
        }),
        ('Boshqa', {
            'fields': ('order', 'is_active')
        }),
    )


@admin.register(DirectionStaticTexts)
class DirectionStaticTextsAdmin(TranslationAdmin):
    list_display = ['title', 'is_active']
    list_filter = ['is_active']

    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('title',)
        }),
        ('Tugma', {
            'fields': ('button_text', 'button_link')
        }),
        ('Boshqa', {
            'fields': ('is_active',)
        }),
    )

    def has_add_permission(self, request):
        if DirectionStaticTexts.objects.exists():
            return False
        return True



@admin.register(EventStaticTexts)
class EventStaticTextsAdmin(TranslationAdmin):
    list_display = ['title', 'is_active']
    list_filter = ['is_active']

    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('title',)
        }),
        ('Tugma', {
            'fields': ('button_text', 'button_link')
        }),
        ('Rasm', {
            'fields': ('side_image',)
        }),
        ('Boshqa', {
            'fields': ('is_active',)
        }),
    )

    def has_add_permission(self, request):
        if EventStaticTexts.objects.exists():
            return False
        return True