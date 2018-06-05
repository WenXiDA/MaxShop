from _datetime import datetime


from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    '''
    用户
    '''
    GENDER =[
        (1,)
    ]
    name = models.CharField(null=True, blank =True, max_length=30, verbose_name="姓名")
    gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", u"女")), verbose_name="性别")
    mobile = models.CharField(max_length=11, verbose_name="电话")
    birthday = models.DateField(null=True, blank=True, verbose_name="出生日期")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="邮箱")
    add_time = models.DateTimeField(default=timezone.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class VerifyCode(models.Model):
    '''
    短信验证码
    '''
    code = models.CharField(max_length=10, verbose_name="验证码")
    mobile = models.CharField(max_length=11, verbose_name="电话")
    add_time = models.DateTimeField(default=timezone.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '短信验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code

#
# from DjangoUeditor.models import UEditorField
# class Blog(models.Model):
# 	Content=UEditorField(u'内容	',width=600, height=300, toolbars="full", imagePath="", filePath="", upload_settings={"imageMaxSize":1204000},
#              settings={},command=None,blank=True)