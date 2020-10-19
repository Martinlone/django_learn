# coding=utf-8
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# 页码， num    每页显示记录数 size


class Movie(models.Model):
    mid = models.AutoField(primary_key=True)
    mname = models.CharField(unique=True, max_length=100)
    mdesc = models.TextField(blank=True, null=True)
    mimg = models.CharField(max_length=120)
    mlink = models.CharField(max_length=200)
    # python 2
    # def __unicode__(self):
    #     return u'Movie:%s,%s'%(self.mid,self.mname)

    # python 3
    def __str__(self):
        return u'Movie:%s,%s' % (self.mid, self.mname)

    class Meta:
        managed = False
        db_table = 'movie'
