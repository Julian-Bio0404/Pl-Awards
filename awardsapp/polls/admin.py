"""Polls admin models."""

# Django
from django.contrib import admin

# Models
from .models import Choice, Question


admin.site.register(Question)
