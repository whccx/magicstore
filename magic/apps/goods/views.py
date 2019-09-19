# -*- coding: utf-8 -*-
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets,mixins,status
from .serializers import GoodsSerializer,AdminGoodsSerializer
from goods.models import GoodsBase

# 商品信息
class GoodsViewSet(viewsets.ReadOnlyModelViewSet,viewsets.GenericViewSet):
    queryset = GoodsBase.objects.all()
    serializer_class = GoodsSerializer

# 后台商品
class AdminGoodsViewSet(viewsets.ModelViewSet,viewsets.GenericViewSet):
    # 认证
    #authentication_classes = (JSONWebTokenAuthentication,)
    # 权限
    #permission_classes = (IsAuthenticated,)

    queryset = GoodsBase.objects.all()
    serializer_class = AdminGoodsSerializer
