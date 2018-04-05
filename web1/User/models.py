#_*_coding:utf-8_*_

from django.db import models
#from Book.models import Indent
# Create your models here.

DEPARTMENT_CHOICE=(
    (1,'电子信息工程系'),
    (2,'计算机科学与技术系'),
    (3,'通信工程系'),
    (4,'管理系'),
    (5,'信息安全系'),
    (6,'其他'),
)
class User(models.Model):
    id=models.AutoField(primary_key=True,unique=True)
    phonenum=models.CharField(max_length=12,unique=True,blank=False)
    passwords=models.CharField(max_length=30,blank=False)
    nickname=models.CharField(max_length=30,blank=False)
    sex=models.CharField(max_length=2,default="空")
    email=models.EmailField(null=True)
    department=models.CharField(max_length=30,choices=DEPARTMENT_CHOICE,default=DEPARTMENT_CHOICE[5])
    portrait=models.ImageField(null=True)
    checkcode=models.IntegerField(default=0)

    def __str__(self):
        return self.phonenum
    def __unicode__(self):
        return self.phonenum