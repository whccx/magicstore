# -*- coding: utf-8 -*-
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets,mixins,status

from .permissions import IsAdminOrReadOnly,IsOwner
from .serializers import GoodsSerializer,TypeSerializer,OrderSerializer
from goods.models import GoodsBase,Type,Order

# 商品信息
class GoodsViewSet(viewsets.ModelViewSet,viewsets.GenericViewSet):
    '''
        list:
            商品列表
        action:
            编辑商品
    '''

    # 认证
    #authentication_classes = (JSONWebTokenAuthentication,)
    # 权限
    permission_classes = (IsAdminOrReadOnly,)

    queryset = GoodsBase.objects.all().order_by("id")
    serializer_class = GoodsSerializer


# 分类信息
class TypeViewSet(viewsets.ModelViewSet,viewsets.GenericViewSet):
    '''
        list:
            分类列表
        action:
            编辑分类
    '''

    # 认证
    #authentication_classes = (JSONWebTokenAuthentication,)
    # 权限
    permission_classes = (IsAdminOrReadOnly,)

    queryset = Type.objects.all().order_by("id")
    serializer_class = TypeSerializer


# 订单信息
class OrderViewSet(viewsets.ModelViewSet,viewsets.GenericViewSet):
    '''
        list:
            订单列表
        action:
            编辑订单
    '''

    # 认证
    #authentication_classes = (JSONWebTokenAuthentication,)
    # 权限
    permission_classes = (IsOwner,IsAuthenticated,)

    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderSerializer

    def list(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            #不能查看别人的订单
            queryset = Order.objects.filter(buy_phone__username=request.user.username).order_by('id')
        else:
            queryset = Order.objects.all().order_by('id')

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({'msg':'管理员不可以创建商品订单'}, status=status.HTTP_403_FORBIDDEN)

