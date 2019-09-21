# -*- coding: utf-8 -*-
import re
from django.utils.timezone import now
from datetime import timedelta
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.hashers import make_password
from .models import VerifyCode



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
        },
        style={'input_type': 'password'}
    )
    code = serializers.CharField(min_length=4,max_length=4,required=True,write_only=True,
                                 label='验证码',help_text='验证码',
         error_messages={
            'blank':'验证码不能为空',
            'required':'请输入验证码',
            'min_length':'验证码至少是4位',
            'max_length':'验证码至多为4位'
        }
     )

    def validate_code(self, code):
        verify_code = VerifyCode.objects.filter(mobile=self.initial_data['username']).order_by('-add_time')
        if verify_code:
            last_code = verify_code[0]
            two_minutes_ago = now() - timedelta(minutes=2)
            if last_code.add_time < two_minutes_ago:
                raise serializers.ValidationError('验证码已过期')
            if last_code.code != code:
                raise serializers.ValidationError('验证码输入错误')
        else:
            raise serializers.ValidationError('验证码错误')

    def validate_password(self,value):
        salt_pwd = make_password(value)
        return salt_pwd

    def validate(self, attrs):
        del attrs['code']
        return attrs

    class Meta:
        model = User
        fields = ['username','password','email','code']


class VerifyCodeSerializer(serializers.Serializer):
    '''
        验证码
    '''
    mobile = serializers.CharField(min_length=11,max_length=11,required=True,
                                   help_text='手机号码',label='手机号码')

    def validate_mobile(self,mobile):
        '''
        :param mobile: 手机号
        :return:
        '''

        #正则验证手机号
        regexp = "^(13[0-9]|14[1|4|5|6|7|8]|15[0|1|2|3|5|6|7|8|9]|166|17[0|1|3|5|6|7|8]|18[0-9]|19[8|9])\d{8}$"
        if not re.match(regexp,mobile):
            raise serializers.ValidationError('手机号码不正确')

        #验证发送频率
        one_minute_ago = now() - timedelta(days=0,minutes=1,seconds=0)
        if VerifyCode.objects.filter(mobile=mobile,add_time__gt=one_minute_ago):
            raise serializers.ValidationError('距离上次发送未超过60S')

        return mobile

