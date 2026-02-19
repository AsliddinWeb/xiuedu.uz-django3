from modeltranslation.translator import register, TranslationOptions

from .models import (AboutBreadcrumb, AboutUniversity, AboutStatistic,
                     AboutHistory, AboutFunfact, AboutMission,
                     AboutMissionItem, AboutCampusTour, Leader)


@register(AboutBreadcrumb)
class AboutBreadcrumbTranslationOptions(TranslationOptions):
    fields = ('title', 'parent_title')


@register(AboutUniversity)
class AboutUniversityTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(AboutStatistic)
class AboutStatisticTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(AboutHistory)
class AboutHistoryTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'content_2')


@register(AboutFunfact)
class AboutFunfactTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(AboutMission)
class AboutMissionTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(AboutMissionItem)
class AboutMissionItemTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(AboutCampusTour)
class AboutCampusTourTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'button_text')


@register(Leader)
class LeaderTranslationOptions(TranslationOptions):
    fields = ('full_name', 'position', 'degree', 'short_bio',
              'biography', 'education', 'expertise', 'courses',
              'publications', 'reception_days')