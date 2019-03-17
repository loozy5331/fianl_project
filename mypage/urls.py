from django.urls import path
from mypage import views

app_name='mypage'

urlpatterns = [
    path('', views.show_main, name='main'),
    #path('create/', views.MyPageCreateView.as_view(), name='create'), # 개인 신상 정보
    path('create/<str:user_name>', views.createView, name='create'), # 개인 신상 정보
    path('create/<str:user_name>/add', views.addQuestionView, name='add'), # 질문 추가
    
]