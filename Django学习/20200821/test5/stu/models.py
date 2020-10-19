from django.db import models


# Create your models here.
# 帖子的模型类
class Post(models.Model):
    pid = models.AutoField(primary_key=True)  # Autofield是指自动递增
    title = models.CharField(max_length=100, unique=True, null=True)
    content = models.TextField()
    create = models.DateTimeField(auto_now_add=True)  # 加了add是只有第一次插入的时候才会将当前时间添加过来
    modified = models.DateTimeField(auto_now=True)  # 只要修改了当前表中的字段的值，这个值会自动更新
    email = models.EmailField()  # 其实就是一个字符串，默认有一个最大长度254
    isdelete = models.BooleanField(default=False)  # 当用户删除该帖子时候，其实是逻辑删除，对应数据库该字段变True，一段时间后数据库才将该记录删掉
    access_count = models.PositiveIntegerField()  # 访问量只有正
    price = models.DecimalField(max_digits=5, decimal_places=2)  # 小数点后两位,总共5位
    file = models.ImageField(upload_to='upload/images/')

    # 自定义查询后的返回值
    def __str__(self):
        return u"Post:%s,%s" % (self.title, self.access_count)

    # 自定义表名
    class Meta:
        db_table = 't_post'

# 班级主表
class Clazz(models.Model):
    cno = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=30)

# 学生从表
class Student(models.Model):
    sno = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=30)
    cno = models.ForeignKey(Clazz, on_delete=models.CASCADE,related_name='sts')

    def __str__(self):
        return u"Student:%s" % self.sname


class Scard(models.Model):
    # 定义一对一，且级联删除
    student = models.OneToOneField(Student, primary_key=True, on_delete=models.CASCADE)
    major = models.CharField(max_length=30)

    def __str__(self):
        return u"Scard:%s" % self.major


# insertData('B203HTML5班','张杰','谢娜')
