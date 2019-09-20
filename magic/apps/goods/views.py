# -*- coding: utf-8 -*-
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .permissions import IsAdminOrReadOnly,IsOwner
from rest_framework import viewsets,mixins,status
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
    authentication_classes = (JSONWebTokenAuthentication,)
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
    authentication_classes = (JSONWebTokenAuthentication,)
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
    permission_classes = (IsOwner,)

    queryset = Order.objects.all().order_by("id")
    serializer_class = OrderSerializer