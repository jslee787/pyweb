from django.http import HttpResponse
from django.shortcuts import render
from board.models import Question


def index(request):
    question_list = Question.objects.all()
    return render(request, 'board/question_list.html', {'question_list':question_list})
    #return HttpResponse("pyweb 사이트 입니다.")

def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'board/detail.html', {'question':question})
