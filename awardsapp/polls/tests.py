"""Polls Tests."""

# Utilities
import datetime

# Django
from django.test import TestCase
from django.utils import timezone

from polls.models import Question


class QuestionModelTests(TestCase):
    """Question model Test."""

    def test_was_published_recently_with_future_question(self):
        """Check that a future date of the question is False in published_recently."""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(text='Who is the best Course Director?', date=time)
        self.assertIs(future_question.published_recently(), False)
