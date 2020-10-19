from django.contrib import admin

from .models import *

# Register your models here.
# 因为之前再urls里面注册了admin.size.urls,所以这里就可以通过admin对应的那个路由查看所有模型类
# 直接查看所以肯定没有，需要创建一些用户
admin.site.register(Student)
