from modeltranslation.translator import register, TranslationOptions
from .models import Review


@register(Review)
class ReviewTranslationOptions(TranslationOptions):
    fields = ("client_name", "text")
