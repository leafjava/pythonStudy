from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
def login(request):
  if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')
    # 业务逻辑判断
    return HttpResponse(f"用户名{username}的密码是{password}")
  elif request.method == "GET":
    # FORBIDDEN_IP = ['127.0.0.1','0.0.0.0']
    # print(request.META.get('REMOTE_ADDR'))

    # if request.META.get('REMOTE_ADDR') in FORBIDDEN_IP:
    #   return HttpResponse('请求异常')
    # else:
    #   return render(request,'login.html')


    print(request.headers.get('user-agent'))

    

    return render(request,'login.html')
  
class RegisterView(View):
  def get(self, request):
    return render(request,'register.html')
  
  def post(self, request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    password2 = request.POST.get('password2')
    # 业务逻辑判断
    return HttpResponse(f"用户名{username}的密码是{password2}")