from modeltranslation.translator import register, TranslationOptions
from .models import Job


@register(Job)
class JobTranslationOptions(TranslationOptions):
    fields = ("name",)
