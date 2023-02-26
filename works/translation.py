from modeltranslation.translator import register, TranslationOptions
from .models import Work


@register(Work)
class CategoryTranslationOptions(TranslationOptions):
    fields = ("name", "description", "client")
