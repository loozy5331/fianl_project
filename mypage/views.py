from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from .models import Question, MyPage

def show_main(request):
    return render(request, 'mypage/main.html')

def createView(request, user_name):
    myPage = MyPage.objects.get(user_name=user_name)
    return render(request, 'mypage/mypage_create.html', {'myPage':myPage})

def addQuestionView(request, user_name):
    question = Question(myPage=MyPage.objects.get(user_name=user_name),
                        question_title="hello world!",
                        question_text="content",
                        question_text_num=2000)
    print(request.POST['question_id'])
    question.save()
    return redirect('/')



