# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Testinfo(models.Model):
    text = models.CharField(max_length=100,verbose_name='测试数据',blank=True, default='')

    class Meta:
        verbose_name = '测试信息'
        verbose_name_plural = '测试信息'