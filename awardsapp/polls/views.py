from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello world!')


def detail(request, question_id):
    return HttpResponse(f'Question number {question_id}')


def results(request, question_id):
    return HttpResponse(f'Question results {question_id}')


def vote(request, question_id):
    return HttpResponse(f'Vote for {question_id}')
