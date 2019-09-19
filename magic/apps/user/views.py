# -*- coding: utf-8 -*-
from random import choice
from rest_framework import viewsets,mixins
from .serializers import RegisterSerializer,IndexSerializer,VerifyCodeSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from .models import Testinfo,VerifyCode
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from utils.yupian import YuPian
from magic.settings import YP_API,YP_APK
# Create your views here.

class UsersViewSet(mixins.CreateModelMixin,viewsets.GenericViewSet):
    '''
    create:
        创建用户
    '''
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class IndexViewSet(mixins.ListModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    #认证
    #authentication_classes = (JSONWebTokenAuthentication,)
    #权限
    #permission_classes = (IsAuthenticated,)

    queryset = Testinfo.objects.all()
    serializer_class = IndexSerializer

    def destroy(self, request, *args, **kwargs):
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        ids = filter_kwargs[self.lookup_field]
        obj = Testinfo.objects.filter(pk=int(ids))
        if obj:
            obj.delete()
            return Response({'error':'删除成功'},status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'error':'不存在此数据'},status=status.HTTP_404_NOT_FOUND)
    # ==================立即修改数据库===============================================
    # for q in queryset:
    #     if q.id == 1:
    #         q.text = '测试789下'
    #         q.save()


    #=================================================================
    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     serializer = self.get_serializer(queryset, many=True)
    #
    #     set = User.objects.all()
    #     for s in set:
    #         print(s.username)
    #
    #     for q in queryset:
    #         if q.id == 1:
    #             q.text += '测试456下'
    #             q.save()
    #
    #     return Response(serializer.data)


    #==================定义查询结果=====================================
    # def get_queryset(self):
    #     queryset = Testinfo.objects.filter(id=1)
    #
    #     for q in queryset:
    #         if q.id == 1:
    #             q.text += '测试123下'
    #             q.save()
    #
    #     return queryset

class VerifyCodeViewSet(mixins.CreateModelMixin,viewsets.GenericViewSet):
    '''
    create:
        手机验证码
    '''
    serializer_class = VerifyCodeSerializer

    def generte_code(self):
        nums = "0123456789"
        random_str = []
        for _ in range(4):
            random_str.append(choice(nums))
        return ''.join(random_str)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        mobile = serializer.validated_data['mobile']

        #生成四位验证码
        code = self.generte_code()
        yp_init = YuPian(YP_APK,YP_API)
        response_data = yp_init.sms_message(mobile=mobile,code=code)
        print(response_data)
        if response_data['code'] != 0:
            return Response({
                'msg':response_data['msg']
            },status=status.HTTP_400_BAD_REQUEST)
        else:
            VerifyCode.objects.create(code=code,mobile=mobile)
            return Response({
                'mobile':response_data['msg']
            },status=status.HTTP_201_CREATED)


