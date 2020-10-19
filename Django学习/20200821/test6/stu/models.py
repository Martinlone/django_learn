from django.db import models


# Create your models here.


class Clazz(models.Model):
    cno = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=30)

    def __str__(self):
        return u'Clazz:%s' % self.cname


class Course(models.Model):
    course_no = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=30)

    def __str__(self):
        return u'Course:%s' % self.course_name


class Student(models.Model):
    sno = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=30)
    cls = models.ForeignKey(Clazz, on_delete=models.CASCADE)
    cour = models.ManyToManyField(Course)

    def __str__(self):
        return u"Student:%s" % self.sname

# 根据班级名称获取班级对象
def getCls(cname):
    try:
        cls = Clazz.objects.get(cname=cname)
    except Clazz.DoesNotExist:
        cls = Clazz.objects.create(cname=cname)
    return cls

# 根据名称获取课程对象列表
def getCourseList(*coursenames):
    courseList = []
    for cn in coursenames:
        try:
            c = Course.objects.get(course_name=cn)
        except Course.DoesNotExist:
            c = Course.objects.create(course_name=cn)
        courseList.append(c)
    return courseList




def registerStu(sname,cname,*coursenames):
    # 获取班级对象
    cls = getCls(cname)
    # 获取课程对象列表
    courselist = getCourseList(*coursenames)
    # 插入学生表数据
    try:
        stu = Student.objects.get(sname=sname)
    except Student.DoesNotExist:
        stu = Student.objects.create(sname=sname, cls=cls)
    # 插入中间表数据
    stu.cour.add(*courselist)

    return True
