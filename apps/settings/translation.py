from modeltranslation.translator import register, TranslationOptions
from .models import (
    SiteSettings, HeaderSettings, HeaderMenu,
    FooterSettings, FooterCategoryMenu, FooterMenuItem
)


@register(SiteSettings)
class SiteSettingsTranslationOptions(TranslationOptions):
    fields = ('site_name', 'site_description', 'site_keywords',
              'address', 'work_time', 'copyright_text')


@register(HeaderSettings)
class HeaderSettingsTranslationOptions(TranslationOptions):
    fields = ('banner_text', 'button_text')


@register(HeaderMenu)
class HeaderMenuTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'badge_text')


@register(FooterSettings)
class FooterSettingsTranslationOptions(TranslationOptions):
    fields = ('about_title', 'about_text', 'newsletter_title', 'newsletter_description')


@register(FooterCategoryMenu)
class FooterCategoryMenuTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(FooterMenuItem)
class FooterMenuItemTranslationOptions(TranslationOptions):
    fields = ('title',)