from modeltranslation.translator import register, TranslationOptions
from .models import Job


@register(Job)
class CategoryTranslationOptions(TranslationOptions):
    fields = ("name",)
