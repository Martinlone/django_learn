# -*- coding: utf-8 -*-
# @Time : 2020/8/24 11:54
# @Author : yangzishuang
# @Site : 
# @File : urls.py
# @Software: PyCharm
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index_view),
    url(r'^show/$',views.show_view),
    url(r'^login/$',views.login_view)

]