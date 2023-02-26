from modeltranslation.translator import register, TranslationOptions
from .models import Staff


@register(Staff)
class StaffTranslationOptions(TranslationOptions):
    fields = ("name",)
