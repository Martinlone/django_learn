from django.db import models

# Create your models here.

class Student(models.Model):
    # 主键不设会有自动递增的一个id
    # CharField代表字符串
    sname = models.CharField(max_length=30, unique=True)
    spwd = models.CharField(max_length=30)

    # 方便后台进django网站查看数据库类时，记录显示的是名字 而不是object
    def __str__(self):
        return u'Student:%s'%self.sname

    # 内部类可以用来生成表名
    class Meta:
        db_table = "t_stu"  # db_table是固定字段 代表表名，如果不写，默认是应用名_模型类名

