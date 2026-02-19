from modeltranslation.translator import register, TranslationOptions
from .models import NewsCategory, NewsTag, NewsImage, News


@register(NewsCategory)
class NewsCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(NewsTag)
class NewsTagTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(NewsImage)
class NewsImageTranslationOptions(TranslationOptions):
    fields = ('alt_text',)


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'content')