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

def list(request):
  author = 'andy'
  article_number = 20
  article_list = [
    '第一篇文章:什么是django',
    '第二篇文章:django的mvt模式',
    '第三篇文章:django的视图'
  ]
  info = {
    'name':'andy',
    'age':18,
    'programming_language':['python','java','c']
  }
  content = """
    <span class="text_heoJj" data-text="true">，三人每天横冲直撞，以为可以自在生活，结果都面临人生最大的转折点。陈末相遇了最神秘的</span>
  """
  return render(request,'list.html',{
    'author':author,
    'number':article_number,
    'article_list':article_list,
    'info':info,
    'content':content
  })