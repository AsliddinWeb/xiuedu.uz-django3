from modeltranslation.translator import register, TranslationOptions

from .models import (BannerSettings, BannerVideo, BannerSlider, BannerNavigation,
                     AboutSection, StatisticItem, NewsStaticTexts, Partner, LicenseStaticTexts, LicenseItem,
                     ProgramStaticTexts, StudentLifeStaticTexts, StudentLifeItem, DirectionStaticTexts,
                     EventStaticTexts)


@register(BannerVideo)
class BannerVideoTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'button_text')


@register(BannerSlider)
class BannerSliderTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'description', 'button_text')


@register(BannerNavigation)
class BannerNavigationTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(AboutSection)
class AboutSectionTranslationOptions(TranslationOptions):
    fields = ('subtitle', 'title', 'description', 'description_2',
              'circle_text', 'mission_title', 'vision_title', 'button_text')


@register(StatisticItem)
class StatisticItemTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(NewsStaticTexts)
class NewsStaticTextsTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'button_text')


@register(Partner)
class PartnerTranslationOptions(TranslationOptions):
    fields = ('name',)



@register(LicenseStaticTexts)
class LicenseStaticTextsTranslationOptions(TranslationOptions):
    fields = ('title', 'button_text')


@register(LicenseItem)
class LicenseItemTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'button_text')



@register(ProgramStaticTexts)
class ProgramStaticTextsTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(StudentLifeStaticTexts)
class StudentLifeStaticTextsTranslationOptions(TranslationOptions):
    fields = ('title', 'title_highlight', 'description')


@register(StudentLifeItem)
class StudentLifeItemTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(DirectionStaticTexts)
class DirectionStaticTextsTranslationOptions(TranslationOptions):
    fields = ('title', 'button_text')


@register(EventStaticTexts)
class EventStaticTextsTranslationOptions(TranslationOptions):
    fields = ('title', 'button_text')