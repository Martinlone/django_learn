# -*- coding: utf-8 -*-
# @Time : 2020/8/21 17:35
# @Author : yangzishuang
# @Site : 
# @File : views.py
# @Software: PyCharm
from django.http import HttpResponse


def index_view(request):
    return HttpResponse("helloworld")