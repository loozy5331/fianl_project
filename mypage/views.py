from django.shortcuts import render
from .models import Question, MyPage

def main(request):
    mypages = MyPage.objects.all()
    context = {'mypages': mypages}
    return render(request, 'mypage/main.html', context)