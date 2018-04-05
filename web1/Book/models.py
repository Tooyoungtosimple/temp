#coding=UTF-8
from django.db import models
from User.models import User
from django.utils.timezone import now
import time
# Create your models here.
DEPARTMENT_CHOICE=(
    (1,'电子信息工程系'),
    (2,'计算机科学与技术系'),
    (3,'通信工程系'),
    (4,'管理系'),
    (5,'信息安全系'),
    (6,'其他'),
)

class Book(models.Model):
    title=models.CharField(max_length=30)
    publisher=models.CharField(max_length=30)
    author=models.CharField(max_length=20)
    department = models.CharField(max_length=30, choices=DEPARTMENT_CHOICE, default=DEPARTMENT_CHOICE[5])
    img=models.ImageField(upload_to='img',blank=True)

    def __str__(self):
        return self.title

class Indent(models.Model):
    orderdate=models.DateField(default=now())
    subdate=models.DateField(default=now())
    #price=models.IntegerField()
    seller=models.ForeignKey(User)
    buyer=models.IntegerField(default=0)
    book=models.ManyToManyField(Book)

    def __str__(self):
        return self.seller.phonenum#"id:"+str(self.id)+"\n发布日期:"+time.strftime(self.orderdate)+"\n下单日期:"+time.strftime(self.subdate)


