# -*- coding: utf-8 -*-
# @Time : 2020/8/28 16:53
# @Author : yangzishuang
# @Site : 
# @File : note.py
# @Software: PyCharm

#### 项目文件说明
'''
@@@@APP包
1.
python manage.py startapp stu  # 创建一个新的应用，完后还得将他添加到settings的APPS中去
2.
admin文件将后台站点和app绑定
在admin.py中添加  admin.site.register(Movie)
3.
apps文件 自动给生成指定当前应用名字
4.
模型类（数据库表）
5.
test专门用来给写测试代码的
6.
urls是子路由
7.
views文件是请求响应函数文件 属于控制层

@@@@项目包
1.
settings文件是配置文件，数据库，debug模式，中间件，app添加
2.
urls根路由
3.
wsgi通用网关

'''
#### manage.py相关操作
'''
1、
python manage.py startapp stu  # 新建一个app
2、
下面再去models写数据库类，并将之添加到setting中
3、
python manage.py makemigrations stu  # 创建迁移文件
4、
然后执行迁移文件python manage.py migrate在数据库中于是就生成了对应的表
5、
在admin文件中添加两行代码实现后台管理
6、
如果mysql没有client则在init文件中加几行，利用pymysql来代替client
7、
创建admin用户python manage.py createsuperuser
8、
settings里面将时区、语言更改一下,admin后台就发生了变化
LANGUAGE_CODE = 'zh-Hans'
TIME_ZONE = 'Asia/Shanghai'
9、
uuid.uuid4().get_hex()获取16进制uuid的具体值
10、
迁移失败的情况下，先删除migrations下面的0001_initial.py文件，在删除数据库中的表django_migrations中的上一次迁移记录，一般是最后一条，然后删除表

'''

'''
get 请求的几种方式
    1、url直接输入
    2、form指定method
    3、js脚本里面输入比如
        <script>
            windows.location.href="/movie/?num=2";
        </script>
    4、标签里面的请求比如
         <a href="/movie/?num={{pre_page_num}}">上一页</a>


from movie.models import Movie
Movie.objects.all()
    想要看它底层的sql语句怎么办呢？
    from django.db import connection
    print (connection.queries)
    # [{'sql': 'SELECT @@SQL_AUTO_IS_NULL', 'time': '0.000'}, {'sql': 'SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED', 'time': '0.001'}, {'sql': 'SELECT `movie`.`mid`, `movie`.`mname`, `movie`.`mdesc`, `movie`.`mimg`, `movie`.`mlink` FROM `movie` LIMIT 21', 'time': '0.013'}]
    print(connection.queries[-1]['sql'])
    # SELECT `movie`.`mid`, `movie`.`mname`, `movie`.`mdesc`, `movie`.`mimg`, `movie`.`mlink` FROM `movie` LIMIT 21

'''

###### 查询
'''
查询单个对象（记录）
Movie.objects.get(mid=147)

过滤
Movie.objects.filter(mname="麻辣学院")

切片
Movie.objects.all()[20:40]

模糊查询(使用魔法下划线)
Movie.objects.filter(mname__endswith="爱情")  # 查询以爱情结尾的
Movie.objects.filter(mname__contains="爱情")  # 查询包含爱情字样的记录
Movie.objects.filter(mname__startswith="爱情")  # 查询以爱情字样开头的记录
Movie.objects.filter(mname__exact="爱情")  # 精确查询和=一样效果
Movie.objects.filter(mname__iendswith="爱情")  # 加了i代表忽略大小写

多条件查询
Movie.objects.filter(mname__iendswith="爱情", mid=147)          # 加了i代表忽略大小写
或者
Movie.objects.filter(mname__endswith="爱情").filter(mid=147)    # 查询以爱情结尾的

部分查询
Movie.objects.values('mid','name').filter(mid=7497)

排除一部份
Movie.objects.filter(mname__endswith="H").exclude(mid=7497)  # 查询以爱情结尾的

排序
Movie.objects.order_by('mid')   # mid前面加了-表示降序    '-mid'

大于小于查询
Movie.objects.filter(mid__gt='147')  # 大于
Movie.objects.filter(mid__lte='147')  # 小于等于   加了e就是等于
Movie.objects.filter(mid__in=(147,149))  # 在某个列表内   mid=147和149的
Movie.objects.filter(mid__range=(147,149))  # 在某个范围内  >= and <=    或者between 147 and 149

'''

#####  插入
'''
m = Movie(mid=10001, mname="yzs", mdesc="hahah",mimg="https://image.baidu.com",mlink="123456")
m.save()
或者是：
Movie.objects.create(mid=10002, mname="sy", mdesc="hahah",mimg="https://image.baidu.com",mlink="123456")

'''

###### 删除
'''
Movie.objects.filter(mid="10002").delete()



'''

# 下面这个算法是解决[1,2,3,4,5]、['a','b','a','c','b']输出[4,7,3]、['a','b','c']

# import re
# from functools import reduce
#
# list1 = [1, 2, 3, 4, 5, 6]
# list2 = ['a', 'b', 'a', 'c', 'd', 'b']
# str2 = ''.join(list2)
# set1 = list(set(list2))
# set1.sort(key=list2.index)
# list_result = []
# for i in set1:
#     index_list = [list1[m.start()] for m in re.finditer(i, str2)]
#     sum = reduce(lambda x, y: x + y, index_list)
#     list_result.append(sum)
# print(set1,list_result)
'''
学生和学生证加了级联，学生证的主键是student，那么用学生表查学生证就是正向查询
Student.objects.first().scard

Scard.objects.first().student
用学生证表查询学生就是逆向查询


'''