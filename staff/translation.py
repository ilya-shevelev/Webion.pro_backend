from modeltranslation.translator import register, TranslationOptions
from .models import Staff


@register(Staff)
class CategoryTranslationOptions(TranslationOptions):
    fields = ("name",)
