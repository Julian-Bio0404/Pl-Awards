"""Polls Tests."""

# Utilities
import datetime
from urllib import response

# Django
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

# Models
from polls.models import Question


class QuestionModelTests(TestCase):
    """Question model Test."""

    def test_was_published_recently_with_future_question(self):
        """Check that a future date of the question is False in published_recently."""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(text='Who is the best Course Director?', date=time)
        self.assertIs(future_question.published_recently(), False)


def create_question(text, days):
    """
    Create a question with the given text, and published the
    given number of days offset to now (negative for questions
    published in the past, positive for questions that have
    yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(text=text, date=time)


class QuestionIndexViewTests(TestCase):
    """Question view test."""

    def test_no_question(self):
        """If no question exist, an message is displayed."""
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No polls are available')
        self.assertQuerysetEqual(response.context['questions'], [])

    def test_future_question(self):
        """
        Check that question with date in the future aren't
        displayed on the index page.
        """
        create_question('Future question', days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, 'No polls are available.')
        self.assertQuerysetEqual(response.context['questions'], [])

    def test_past_question(self):
        """
        Question with a date in the past are displayed
        on the index page.
        """
        question = create_question('Past question', days=-10)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['questions'], [question])

    def test_future_question_and_past_question(self):
        """
        Even if both past and future question exist,
        only past questions are displayed.
        """
        past_question = create_question(text='Past question', days=-30)
        future_question = create_question(text='Future question', days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['questions'], [past_question])


class DetailViewTests(TestCase):
    """Detail Question View test."""

    def test_future_question(self):
        """
        The detail view of a question with a date in the
        future return a 404 not found.
        """
        future_question = create_question(text='Future question', days=30)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        The detail view of a question with a date in the past
        display the question's text.
        """
        past_question = create_question(text='Future question', days=-30)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, past_question.text)
