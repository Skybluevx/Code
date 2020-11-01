from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("你好呀，世界！")


def detail(request, question_id):
    return HttpResponse(f"你正在看第{question_id}个问题")


def result(request, question_id):
    return HttpResponse(f"你正在看第{question_id}个问题的结果")


def vote(request, question_id):
    return HttpResponse(f"你正在给第{question_id}个问题投票")
