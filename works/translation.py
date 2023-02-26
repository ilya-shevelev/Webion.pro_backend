from modeltranslation.translator import register, TranslationOptions
from .models import Work


@register(Work)
class WorkTranslationOptions(TranslationOptions):
    fields = ("name", "description", "client")
