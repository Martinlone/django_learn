from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


# 只是用来渲染页面的
def index_view(request):
    return render(request,'login.html')

# 处理登录功能
def login_view(request):
    # 接收表单请求数据
    uname = request.GET.get("uname",'')
    pwd = request.GET.get("pwd",'')
    # 判断
    if uname == 'zhangsan'  and pwd == "123":
        return HttpResponse('登陆成功！')

    return HttpResponse('登陆失败！')