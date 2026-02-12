from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from .models import (
    SiteSettings, SocialNetwork, HeaderSettings, HeaderMenu,
    FooterSettings, FooterCategoryMenu, FooterMenuItem
)


@admin.register(SiteSettings)
class SiteSettingsAdmin(TranslationAdmin):
    list_display = ['site_name', 'phone', 'email', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['site_name', 'phone', 'email']

    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('site_name', 'site_description', 'site_keywords')
        }),
        ('Logolar', {
            'fields': ('logo', 'logo_white', 'logo_dark', 'favicon')
        }),
        ('Aloqa ma\'lumotlari', {
            'fields': ('phone', 'phone_2', 'email', 'email_2', 'address', 'work_time')
        }),
        ('Xarita', {
            'fields': ('map_iframe', 'latitude', 'longitude'),
            'classes': ('collapse',)
        }),
        ('SEO va Analytics', {
            'fields': ('google_analytics', 'yandex_metrika', 'facebook_pixel'),
            'classes': ('collapse',)
        }),
        ('Boshqa', {
            'fields': ('copyright_text', 'is_active')
        }),
    )

    def has_add_permission(self, request):
        if SiteSettings.objects.exists():
            return False
        return True


@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'order', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'url']
    list_editable = ['order', 'is_active']
    ordering = ['order', 'name']


@admin.register(HeaderSettings)
class HeaderSettingsAdmin(TranslationAdmin):
    list_display = ['show_banner', 'show_header_button', 'show_search', 'show_language_switcher', 'is_active']
    list_filter = ['is_active', 'show_banner', 'show_search']

    fieldsets = (
        ('Banner', {
            'fields': ('show_banner', 'banner_text', 'banner_link')
        }),
        ('Header tugma', {
            'fields': ('show_header_button', 'button_image', 'button_text', 'button_link')
        }),
        ('Qo\'shimcha', {
            'fields': ('show_search', 'show_language_switcher', 'is_active')
        }),
    )

    def has_add_permission(self, request):
        if HeaderSettings.objects.exists():
            return False
        return True


@admin.register(HeaderMenu)
class HeaderMenuAdmin(TranslationAdmin):
    list_display = ['title', 'parent', 'order', 'is_mega_menu', 'show_badge', 'is_active']
    list_filter = ['is_active', 'is_mega_menu', 'show_badge', 'parent']
    search_fields = ['title', 'url', 'description']
    list_editable = ['order', 'is_active']
    ordering = ['parent', 'order', 'title']

    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('parent', 'title', 'url', 'icon')
        }),
        ('Mega Menu', {
            'fields': ('is_mega_menu', 'description', 'image'),
            'classes': ('collapse',)
        }),
        ('Badge', {
            'fields': ('show_badge', 'badge_text', 'badge_color'),
            'classes': ('collapse',)
        }),
        ('Sozlamalar', {
            'fields': ('open_new_tab', 'css_class', 'order', 'is_active')
        }),
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('parent')


@admin.register(FooterSettings)
class FooterSettingsAdmin(TranslationAdmin):
    list_display = ['show_newsletter', 'show_recent_news', 'show_copyright', 'is_active']
    list_filter = ['is_active', 'show_newsletter', 'show_recent_news']

    fieldsets = (
        ('Haqida', {
            'fields': ('about_title', 'about_text')
        }),
        ('Newsletter', {
            'fields': ('show_newsletter', 'newsletter_title', 'newsletter_description')
        }),
        ('Yangiliklar', {
            'fields': ('show_recent_news', 'recent_news_count')
        }),
        ('Boshqa', {
            'fields': ('show_copyright', 'show_payment_icons', 'is_active')
        }),
    )

    def has_add_permission(self, request):
        if FooterSettings.objects.exists():
            return False
        return True


class FooterMenuItemInline(TranslationTabularInline):
    model = FooterMenuItem
    extra = 1
    fields = ['title', 'url', 'icon', 'open_new_tab', 'order', 'is_active']
    ordering = ['order', 'title']


@admin.register(FooterCategoryMenu)
class FooterCategoryMenuAdmin(TranslationAdmin):
    list_display = ['title', 'order', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title']
    list_editable = ['order', 'is_active']
    ordering = ['order', 'title']
    inlines = [FooterMenuItemInline]


@admin.register(FooterMenuItem)
class FooterMenuItemAdmin(TranslationAdmin):
    list_display = ['title', 'category', 'url', 'order', 'is_active']
    list_filter = ['is_active', 'category', 'open_new_tab']
    search_fields = ['title', 'url']
    list_editable = ['order', 'is_active']
    ordering = ['category', 'order', 'title']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('category')