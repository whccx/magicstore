# -*- coding: utf-8 -*-

from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.hashers import make_password
from .models import Testinfo

class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True,
        allow_blank=False,
        label="用户名",
        max_length=16,
        min_length=6,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message='用户名已经存在',
            )
        ],
        error_messages={
            "blank": "用户名不允许为空",
            "required": "请输入用户名",
            "max_length": "用户名长度最长为16位",
            "min_length": "用户名长度至少为6位"
        }
    )
    password = serializers.CharField(
        required=True,
        write_only=True,
        label='密码',
        max_length=16,
        min_length=6,
        error_messages={
            "blank": "密码不允许为空",
            "required": "请输入密码",
            "max_length": "用户名长度最长为16位",
            "min_length": "用户名长度至少为6位"
        }
    )

    class Meta:
        model = User
        fields = ['username','password','email']

    def validate_password(self,value):
        salt_pwd = make_password(value)
        return salt_pwd


class IndexSerializer(serializers.ModelSerializer):
    text = serializers.CharField(
        required=True,
        write_only=True,
        label='用户信息'
    )
    class Meta:
        model = Testinfo
        fields = ['text']