"""Polls views."""

# Django
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

# Models
from polls.models import Choice, Question


def index(request):
    questions = Question.objects.all()
    return render(request, 'polls/index.html', {'questions': questions})


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request, 'polls/detail.html',
            {'question': question, 'error_message': 'You did not choose an answer'})
    choice.votes +=1
    choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
