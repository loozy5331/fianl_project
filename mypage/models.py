from django.db import models
from django.conf import settings 
from django.utils import timezone

class MyPage(models.Model):
    """
    name: UserName
    age: UserAge
    high_school_name : 고등학교 이름
    high_adm_date : 고등학교 입학일
    high_grad_date : 고등학교 졸업일
    
    univ_name : 대학 이름
    major_name : 전공 이름
    sub_major_name : 부전공 이름
    univ_adm_date : 대학 입학일
    univ_grad_date : 대학 졸업일
    """
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    
    high_school_name = models.CharField(max_length=30)
    high_adm_date = models.DateField()
    high_grad_date = models.DateField()
    
    univ_name = models.CharField(max_length=30)
    major_name = models.CharField(max_length=30)
    sub_major_name = models.CharField(max_length=30)
    univ_adm_date = models.DateField()
    univ_grad_date = models.DateField()

    def __str__(self):
        return "id : {}, name : {}, age : {}".format(self.id, self.name, self.age)

class Question(models.Model):
    """
    myPage: 개인이 선택한 페이지
    question_title: 질문
    question_content: 질문에 대한 답변
    """
    myPage = models.ForeignKey(MyPage, on_delete=models.CASCADE)
    question_title = models.CharField(max_length=200)
    question_text = models.TextField()

    def __str__(self):
        return self.question_title
