from django.urls import path
from mypage import views

urlpatterns = [
    path('', views.main, name='main'),

]