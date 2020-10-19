# -*- coding: utf-8 -*-
# @Time : 2020/8/26 10:41
# @Author : yangzishuang
# @Site : 
# @File : urls.py
# @Software: PyCharm
from django.conf.urls import url
from . import views
print("wwww")
urlpatterns = [
    url(r'^$',views.index_view),
    url(r'^index/$',views.index2_view)
]