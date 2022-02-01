"""Polls models."""

# Utilities
import datetime

# Django
from django.db import models
from django.utils import timezone


class Question(models.Model):
    """Question model."""

    text = models.CharField(max_length=200)
    date = models.DateTimeField()

    def __str__(self) -> str:
        """Return question text."""
        return self.text
    
    def published_recently(self) -> bool:
        """Check if the pub date is recently."""
        now = timezone.now()
        return now >= self.date >= now - datetime.timedelta(days=1)


class Choice(models.Model):
    """Choice model."""

    question = models.ForeignKey('polls.Question', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    votes = models.BigIntegerField(default=0)

    def __str__(self) -> str:
        """Return choice text."""
        return self.text
