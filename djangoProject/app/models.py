from django.db import models

# Create your models here.

class UserInfo(models.Model):
    name = models.CharField(verbose_name='姓名',max_length=32, null=True, blank=True)
    password = models.CharField(verbose_name='密码',max_length=64, null=True, blank=True)
    age = models.IntegerField()

class Department(models.Model):
    title = models.CharField(verbose_name='名称',max_length=16)

# #新建数据 insert into app_department(title) values('销售部')
# Department.objects.create(title='销售部')
# UserInfo.objects.create(name='111',password='123',age=19,aaa='aaa',bbb='bbb')

class Role(models.Model):
    caption = models.CharField(max_length=16)


""""
create table app_userinfo(
    id bigint auto_increment primary key,
    name varchar(32),
    password varchar(64),
    age int
)
"""