from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from .models import Question, MyPage

def show_main(request):
    return render(request, 'mypage/main.html')

class MyPageCreateView(CreateView):
    model = MyPage
    fields = ['name', 'age', 'high_school_name', 'high_adm_date', 'high_grad_date',
        'univ_name', 'major_name', 'sub_major_name', 'univ_adm_date', 'univ_grad_date']
    template_name_suffix = '_create'

    def form_valid(self, form):
        form.instance.mypage_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('mypage:mypage')
        else:
            return self.render_to_response({'form':form})

class QuestionDeleteView(DeleteView):
    model = Question
    success_url = 'mypage:mypage'
    template_name = 'mypage/delete.html'

class QuestionUpdateView(UpdateView):
    models = Question
    fields = ['question_text', 'question_text_num']
    template_name = 'mypage/update.html'


