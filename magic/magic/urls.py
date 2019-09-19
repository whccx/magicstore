# -*- coding: utf-8 -*-

from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.models import User
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token

from rest_framework_jwt.views import obtain_jwt_token
from user.views import UsersViewSet

router = routers.DefaultRouter()

#用户注册
router.register(r'users', UsersViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('login/', obtain_jwt_token),
    path('refresh/', refresh_jwt_token),

    path('', include(router.urls)),

    path('ueditor/',include('DjangoUeditor.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)