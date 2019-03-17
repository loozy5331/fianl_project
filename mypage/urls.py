from django.urls import path
from mypage import views

app_name='mypage'

urlpatterns = [
    path('', views.show_main, name='main'),
    #path('create/', views.MyPageCreateView.as_view(), name='create'), # 개인 신상 정보
    path('create/<str:user_name>', views.createView, name='create'), # 개인 신상 정보
    path('update/<int:pk>', views.QuestionUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.QuestionDeleteView.as_view(), name='delete'), # 개인이 선택한 질문들을 저장
    
]