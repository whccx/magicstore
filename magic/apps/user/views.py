# -*- coding: utf-8 -*-

from rest_framework import viewsets,mixins,status
from .serializers import RegisterSerializer,IndexSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from .models import Testinfo


# Create your views here.


class UsersViewSet(mixins.CreateModelMixin,viewsets.GenericViewSet):
    '''
    create:
        创建用户
    '''
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class IndexViewSet(mixins.ListModelMixin,mixins.CreateModelMixin,viewsets.GenericViewSet):
    queryset = Testinfo.objects.all()
    serializer_class = IndexSerializer