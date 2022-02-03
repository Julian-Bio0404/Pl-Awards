"""Polls admin models."""

# Django
from re import search
from django.contrib import admin

# Models
from .models import Choice, Question


class ChoiceInline(admin.StackedInline):
    """Choice Inline admin."""

    model = Choice
    extra = 3


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """Question model admin."""

    fields = ['text', 'date']
    inlines = [ChoiceInline]
    list_display = ['text', 'date', 'published_recently']
    list_filter = ['date']
    search_fields = ['text']
