# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
<<<<<<< HEAD

class VerifyCode(models.Model):
    '''
    短信验证码
    '''
    code = models.CharField(max_length=20,verbose_name='验证码',help_text='验证码')
    mobile = models.CharField(max_length=11,verbose_name='电话',help_text='电话')
    add_time = models.DateTimeField(auto_now_add=True,verbose_name='添加时间')

    class Meta:
        verbose_name_plural = verbose_name = '短信验证码'

    def __str__(self):
        return self.code

class Testinfo(models.Model):
    text = models.CharField(max_length=100,verbose_name='测试数据',blank=True, default='')

    class Meta:
        verbose_name = '测试信息'
        verbose_name_plural = '测试信息'

