# -*- coding: utf-8 -*-
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets,mixins,status
from .serializers import GoodsSerializer
from goods.models import GoodsBase

# 商品信息
class GoodsViewSet(viewsets.ModelViewSet,viewsets.GenericViewSet):
    # 认证
    authentication_classes = (JSONWebTokenAuthentication,)
    # 权限
    permission_classes = (IsAuthenticatedOrReadOnly,)

    queryset = GoodsBase.objects.all()
    serializer_class = GoodsSerializer
