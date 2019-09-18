# -*- coding: utf-8 -*-

from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.models import User
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from user.views import UsersViewSet

router = routers.DefaultRouter()


#用户注册
router.register(r'users', UsersViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_jwt_token),
    path('', include(router.urls)),
]
