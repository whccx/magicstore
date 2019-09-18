from rest_framework import viewsets,mixins,status
from .serializers import RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
# Create your views here.


class UsersViewSet(mixins.CreateModelMixin,viewsets.GenericViewSet):
    '''
    create:
        创建用户
    '''
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

