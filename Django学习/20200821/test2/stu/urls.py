# -*- coding: utf-8 -*-
# @Time : 2020/8/23 15:08
# @Author : yangzishuang
# @Site : 
# @File : urls.py
# @Software: PyCharm

# 这是子路由
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index_view),
    url(r'^login/',views.login_view)
]