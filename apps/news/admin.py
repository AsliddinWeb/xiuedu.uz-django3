from django.contrib import admin
from django.utils import timezone
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from .models import NewsCategory, NewsTag, NewsImage, News, NewsComment


@admin.register(NewsCategory)
class NewsCategoryAdmin(TranslationAdmin):
    list_display = ['name', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(NewsTag)
class NewsTagAdmin(TranslationAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class NewsImageInline(TranslationTabularInline):
    model = NewsImage
    extra = 1
    fields = ['image', 'alt_text', 'order']
    ordering = ['order']


class NewsCommentInline(admin.TabularInline):
    model = NewsComment
    extra = 0
    fields = ['name', 'phone', 'subject', 'message', 'status']
    readonly_fields = ['name', 'phone', 'subject', 'message']


@admin.register(News)
class NewsAdmin(TranslationAdmin):
    list_display = ['title', 'category', 'author', 'published_at', 'views_count', 'is_featured', 'is_active']
    list_filter = ['is_active', 'is_featured', 'category', 'published_at']
    search_fields = ['title', 'content']
    list_editable = ['is_featured', 'is_active']
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ['tags']
    exclude = ['author', 'published_at']
    readonly_fields = ['views_count']
    inlines = [NewsImageInline, NewsCommentInline]

    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('title', 'slug', 'category', 'tags', 'short_description', 'content')
        }),
        ('Asosiy rasm', {
            'fields': ('image', 'image_alt_uz', 'image_alt_ru', 'image_alt_en')
        }),
        ('Boshqa', {
            'fields': ('views_count', 'is_featured', 'is_active')
        }),
    )

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        super().save_model(request, obj, form, change)


@admin.register(NewsComment)
class NewsCommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'news', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['name', 'phone', 'message']
    list_editable = ['status']
    readonly_fields = ['name', 'phone', 'subject', 'message', 'news']