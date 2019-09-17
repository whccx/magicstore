from rest_framework import viewsets,mixins
from .serializers import RegisterSerializer
from django.contrib.auth.models import User
# Create your views here.


class RegisterViewSet(mixins.ListModelMixin,mixins.CreateModelMixin,viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
