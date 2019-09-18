# -*- coding: utf-8 -*-

from django.contrib import admin
from django.urls import path,include

from django.contrib.auth.models import User
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/',include('user.urls')),
    path('api-token-auth/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
]
