# -*- coding: utf-8 -*-
# @Time : 2020/8/28 16:53
# @Author : yangzishuang
# @Site : 
# @File : note.py
# @Software: PyCharm

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

## ###  插入
'''
m = Movie(mid=10001, mname="yzs", mdesc="hahah",mimg="https://image.baidu.com",mlink="123456")
m.save()
或者是：
Movie.objects.create(mid=10002, mname="sy", mdesc="hahah",mimg="https://image.baidu.com",mlink="123456")




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
