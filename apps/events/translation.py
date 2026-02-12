from modeltranslation.translator import register, TranslationOptions

from .models import Event, EventFeature


@register(Event)
class EventTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'short_description',
              'button_text', 'venue_name', 'venue_address')


@register(EventFeature)
class EventFeatureTranslationOptions(TranslationOptions):
    fields = ('title', 'description')