from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone

from board.models import Question, Answer
from board.forms import QuestionForm, AnswerForm

def index(request):
    question_list = Question.objects.all()
    return render(request, 'board/question_list.html', {'question_list':question_list})
    #return HttpResponse("pyweb 사이트 입니다.")

def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'board/detail.html', {'question':question})

def question_create(request):
    if request.method =="POST":
        form = QuestionForm(request.POST)   #자료 전달
        if form.is_valid():
            question = form.save(commit=False)  #임시저장
            question.create_date = timezone.now()
            question.save() #실제 저장
            return redirect('board:index')  #이동할 경로(app_name) 저장
    else:
        form = QuestionForm()
    return render(request, 'board/question_form.html', {'form':form})

def answer_create(request, question_id):
    question = Question.objects.get(id=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question  #외래키 질문 저장
            answer.save()
            return redirect('board:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question':question, 'form':form}
    return render(request, 'board/detail.html', context)