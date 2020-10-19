from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from .models import *


def index_view(request):
    # 获取当前的请求方式
    m = request.method
    # 这句话的意思是直接再浏览器中输入url回车后默认是get所以走下面的，进行render
    if m == 'GET':
        return render(request, "register.html")
    else:
        # 获取请求参数
        uname = request.POST.get('uname', '')
        pwd = request.POST.get('pwd', '')

        if uname and pwd:
            # 创建模型对象
            stu = Student(sname=uname, spwd=pwd)
            # 插入数据库
            stu.save()

            return HttpResponse("注册ok")
        else:
            return HttpResponse("注册失败")


def show_view(request):
    # 查询stu数据库所有数据
    stus = Student.objects.all()
    # 后面的字典是为了把查询数据传过去
    return render(request, 'show.html', {'students': stus})


def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')

        if uname and pwd:
            # 对象类得数据库查询语句
            c = Student.objects.filter(sname=uname, spwd=pwd).count()
            if c == 1:
                return HttpResponse('登录成功！')
        return HttpResponse('登录失败！')
