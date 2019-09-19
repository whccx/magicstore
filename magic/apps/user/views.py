# -*- coding: utf-8 -*-

from rest_framework import viewsets,mixins,status
from .serializers import RegisterSerializer,IndexSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from .models import Testinfo
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
# Create your views here.
from rest_framework import status

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
