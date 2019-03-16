from django.db import models
from django.contrib.auth.models import User
from django.conf import settings 

#from django.utils import timezone
from django.urls import reverse

class MyPage(models.Model):
    """
    user_name = user의 id

    name = 이름
    age = 나이
    
    high_school_name = 고등학교 이름
    high_adm_date = 고등학교 입학일
    high_grad_date = 고등학교 졸업일
    
    univ_name = 대학교 이름
    major_name = 주전공 이름
    sub_major_name = 복수, 부전공 이름
    univ_adm_date = 대학교 입학일
    univ_grad_date = 대학교 졸업일
    """
    user_name = models.CharField(max_length=30, default='0')

    name = models.CharField(max_length=10)
    age = models.PositiveIntegerField(default=0)
    
    high_school_name = models.CharField(max_length=30, default="")
    high_adm_date = models.DateField()
    high_grad_date = models.DateField()
    
    univ_name = models.CharField(max_length=30, default="")
    major_name = models.CharField(max_length=30, default="")
    sub_major_name = models.CharField(max_length=30, default="")
    univ_adm_date = models.DateField()
    univ_grad_date = models.DateField()

    def __str__(self):
        return "id : {}, name : {}, age : {}".format(self.id, self.name, self.age)

class Question(models.Model):
    """
    myPage = mypage
    question_title = 질문 제목
    question_text = 답변 내용
    #question_text_file = 답변 내용을 저장할 파일
    question_text_num = 답변 길이 제한
    """
    myPage = models.ForeignKey(MyPage, on_delete=models.CASCADE)
    question_title = models.CharField(max_length=200)
    question_text = models.TextField()
    #question_text_file = models.FileField(upload_to="question_log/{}".format(self.id))
    question_text_num = models.PositiveIntegerField(default=2000)

    def __str__(self):
        return self.question_title
    
    def get_absolute_url(self):
        return reverse('mypage:detail', args=[str(self.id)])

class Log(models.Model):
    """
    question = question
    save_date = 저장일
    log_message = 저장 메시지
    log_text = 저장 내용
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    save_date = models.DateTimeField()
    log_message = models.CharField(max_length=20)
    log_text = models.TextField()