from django.urls import path
from mypage import views

app_name='mypage'

urlpatterns = [
    path('', views.main, name='main'),
    path('mypage/', views.show_mypage, name='mypage'),
    path('mypage/<int:mypage_id>', views.show_mypage, name='mypage'),

]