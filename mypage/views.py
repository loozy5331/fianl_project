from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from .models import Question, MyPage, Question_List

def show_main(request):
    return render(request, 'mypage/main.html')

def createView(request, user_name):
    myPage = MyPage.objects.get(user_name=user_name)
    context = dict()
    context['question_list'] = Question_List.objects.all()
    questions = myPage.question_set.all()
    context['questions'] = [ question.question_list_id for question in questions]
    if request.method == "GET":
        if myPage.user_name != "0":
            # 기존에 있던 정보 불러오기
            context['myPage'] = myPage
            return render(request, 'mypage/mypage_create.html', context)
        else:
            return render(request, 'mypage/mypage_create.html', context)
    else:
        # Post로 form 정보 전송
        form_info = request.POST
        myPage.name = form_info['name']
        myPage.age = int(form_info['age'])

        myPage.high_school_name = form_info['high_school_name']
        myPage.high_adm_date = form_info['high_adm_date']
        myPage.hight_grad_date = form_info['hight_grad_date']

        myPage.univ_name = form_info['univ_name']
        myPage.major_name = form_info['major_name']
        myPage.sub_major_name = form_info['sub_major_name']
        #myPage.univ_adm_date = form_info['univ_adm_date']
        #myPage.univ_grad_date = form_info['univ_grad_date']
        myPage.save()

    return render(request, 'mypage/mypage_create.html', context)

def addQuestionView(request, user_name):
    question = Question(myPage=MyPage.objects.get(user_name=user_name),
                        question_list_id = request.POST['question_list_id'],
                        question_title=Question_List.objects.get(id=request.POST['question_list_id']),
                        question_text_num=request.POST['question_num'])
    question.save()
    return redirect('/')



