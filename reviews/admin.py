from django.contrib import admin
from .models import Review
from modeltranslation.admin import TranslationAdmin


@admin.register(Review)
class ReviewAdmin(TranslationAdmin):
    """Отзывы"""

    pass
