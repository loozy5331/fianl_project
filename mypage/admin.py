from django.contrib import admin
from .models import *

class MyPageAdmin(admin.ModelAdmin):
    list_display = ['name', 'univ_name', 'major_name']
    list_filter = ['univ_name', 'major_name']
    search_field = ['text', 'name']



admin.site.register(MyPage, MyPageAdmin)
admin.site.register(Question)
