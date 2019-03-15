from django.views.generic.edit import CreateView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from .models import Question, MyPage

def main(request):
    return render(request, 'mypage/main.html')


def show_mypage(request):
    #mypage = get_object_or_404(MyPage, pk=page_id)
    mypage = MyPage.objects.all()
    context = {'mypage': mypage}
    return render(request, 'mypage/mypage.html', context)

class MyPageCreateView(CreateView):
    model = MyPage
    fields = ['name', 'age', 'high_school_name', 'high_adm_date', 'high_grad_date',
        'univ_name', 'major_name', 'sub_major_name', 'univ_adm_date', 'univ_grad_date']
    success_url = reverse_lazy('mypage:main')
    template_name_suffix = '_create'