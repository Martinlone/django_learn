from django.shortcuts import render

from .models import *
import math


# Create your views here.
def page(num, size=20):
    num = int(num)
    # 判断是否越界
    # 求出总的记录数
    totalRecords = Movie.objects.count()
    # 总页数
    # totalPages = totalRecords // size if totalRecords % size == 0 else totalRecords // size + 1
    # math.ceil()代表向上取整
    totalPages = int(math.ceil(totalRecords / size))
    if num < 1:
        num = 1
    if num > totalPages:
        num = totalPages
    # 计算每页显示的记录

    movies = Movie.objects.all()[((num - 1) * size):(num * size)]

    return movies, num


# 原生的请求方式
def index_view(request):
    num = request.GET.get('num', 1)
    # 处理分页请求
    page(num)
    movies, n = page(num)

    # 上一页页码
    pre_page_num = n - 1
    next_page_num = n + 1
    return render(request, 'index01.html',
                  {'movies': movies, 'pre_page_num': pre_page_num, 'next_page_num': next_page_num})


from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# 利用django自带的分页技术
def index2_view(request):
    # 查询所有数据
    movies = Movie.objects.all()

    # 创建分页器对象
    pager = Paginator(movies, 20)

    # 获取当前页码数
    n = int(request.GET.get("num", 1))

    # 获取当前页得数据
    try:
        perpage_data = pager.page(n)
    except PageNotAnInteger:
        # 返回第一页的数据
        perpage_data = pager.page(1)
    except EmptyPage:
        # 返回最后一页的数据
        perpage_data = pager.page(pager.num_pages)

    # 每页开始页码,为了解决，页码点最后一个以后，页码变成中间
    begin = (n - int(math.ceil(10.0 / 2)))

    if begin < 1:
        begin = 1

    # 每页结束页码
    end = begin + 9
    if end > pager.num_pages:
        end = pager.num_pages
    # 可能一共就没有10页 或者刚好
    if end <= 10:
        begin = 1
    else:
        begin = end - 9
    pagelist = range(begin, end + 1)

    return render(request, 'index01.html', {'pager': pager, 'perpage_data': perpage_data, 'pagelist': pagelist})


from movie.models import Movie


# 定义一个从类操作语句获得sql语句的函数
def showsql():
    from django.db import connection
    # 打印最近一个执行的类操作数据库的sql语句
    print(connection.queries[-1]['sql'])
