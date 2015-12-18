from django.shortcuts import render
import datetime


def main(request):
    now = datetime.datetime.now()
    context = {'message':'Django 很棒', 'now':now ,'text':'我們提供許多相關知識歡迎瀏覽'}
    return render(request,'main/main.html',context)
