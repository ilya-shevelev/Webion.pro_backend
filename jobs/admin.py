from django.contrib import admin
from .models import Job
from modeltranslation.admin import TranslationAdmin


@admin.register(Job)
class JobAdmin(TranslationAdmin):
    """Должности"""

    pass
