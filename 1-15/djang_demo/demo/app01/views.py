from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def helloworld(request):
  return HttpResponse('hello world')

def article_year(request,year):
  return HttpResponse(f'{year}年所有文章')

def article_month(request,year,month):
  return HttpResponse(f'{year}年{month}月所有文章')

def article_flag(request,year,month,flag):
  return HttpResponse(f'{year}年{month}月{flag}所有文章')

def get_current_datetime(request):
  today = datetime.today() #获取今天日期
  format_today = today.strftime("%Y-%m-%d")
  html = f"<h1>今天是{format_today}</h1>"
  return HttpResponse(format_today)