"""Polls views."""

# Django
from django.shortcuts import render
from django.http import HttpResponse

# Models
from polls.models import Question


def index(request):
    questions = Question.objects.all()
    return render(request, 'polls/index.html', {'questions': questions})


def detail(request, question_id):
    return HttpResponse(f'Question number {question_id}')


def results(request, question_id):
    return HttpResponse(f'Question results {question_id}')


def vote(request, question_id):
    return HttpResponse(f'Vote for {question_id}')
