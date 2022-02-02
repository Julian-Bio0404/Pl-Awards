"""Polls views."""

# Django
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

# Models
from polls.models import Choice, Question


class IndexView(generic.ListView):
    """Handle the question list."""

    template_name = 'polls/index.html'
    context_object_name = 'questions'

    def get_queryset(self):
        """Return the last five published questions."""
        now = timezone.now()
        return Question.objects.filter(date__lte=now).order_by('-date')[:5]


class DetailView(generic.DetailView):
    """Handle the question detail."""

    model = Question
    template_name = 'polls/detail.html'


class ResultView(generic.DetailView):
    """Handle the question results."""

    model = Question
    template_name = 'polls/results.html'


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
