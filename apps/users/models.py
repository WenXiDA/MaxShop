from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    '''
    用户
    '''
    name = models.CharField()
    gender = models.CharField()
    mobile = models.CharField()
    birthday = models.DateTimeField()
    email = models.EmailField()
    add_time = models.DateTimeField()

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class VerifyCode(models.Model):
    '''
    短信验证码
    '''
    code = models.CharField()
    mobile = models.CharField()
    add_time = models.DateTimeField()

    class Meta:
        verbose_name = '短信验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code