from django.contrib import admin
from .models import Staff
from modeltranslation.admin import TranslationAdmin


@admin.register(Staff)
class StaffAdmin(TranslationAdmin):
    """Персонал"""

    pass
