from django.contrib import admin
from .models import Work, WorkImage
from modeltranslation.admin import TranslationAdmin


@admin.register(Work)
class WorkAdmin(TranslationAdmin):
    """Работы"""

    pass


admin.site.register(WorkImage)
