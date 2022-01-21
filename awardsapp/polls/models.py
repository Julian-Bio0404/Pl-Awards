from django.db import models


class Question(models.Model):
    """Question model."""

    text = models.CharField(max_length=200)
    date = models.DateTimeField()


class Choice(models.Model):
    """Choice model."""

    question = models.ForeignKey('polls.Question', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    votes = models.BigIntegerField(default=0)
