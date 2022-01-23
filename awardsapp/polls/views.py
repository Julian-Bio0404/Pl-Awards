"""Polls views."""

# Django
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Models
from polls.models import Question


def index(request):
    questions = Question.objects.all()
    return render(request, 'polls/index.html', {'questions': questions})


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    return HttpResponse(f'Question results {question_id}')


def vote(request, question_id):
    return HttpResponse(f'Vote for {question_id}')
