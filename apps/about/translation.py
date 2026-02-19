from modeltranslation.translator import register, TranslationOptions
from .models import Leader


@register(Leader)
class LeaderTranslationOptions(TranslationOptions):
    fields = ('full_name', 'position', 'degree', 'short_bio',
              'biography', 'education', 'expertise', 'courses',
              'publications', 'reception_days')