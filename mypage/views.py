from django.shortcuts import render, get_object_or_404
from .models import Question, MyPage

def main(request):
    return render(request, 'mypage/main.html')


def show_mypage(request):
    #mypage = get_object_or_404(MyPage, pk=page_id)
    mypage = MyPage.objects.all()
    context = {'mypage': mypage}
    return render(request, 'mypage/mypage.html', context)