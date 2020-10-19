from django.db import models
from django.db.models.manager import Manager

class CustomManger(Manager):



# Create your models here.
class Student(models.Model):
    sname = models.CharField(max_length=30)
    isdelete = models.BooleanField(default=False)

# Student.objects.all()执行这句话 我不想返回全表数据，我只想要其返回isdelete字段为True的

