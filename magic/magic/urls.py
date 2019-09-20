# -*- coding: utf-8 -*-

from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.models import User
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token
from django.views.generic.base import RedirectView
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.documentation import include_docs_urls

from user.views import UsersViewSet,VerifyCodeViewSet


from user.views import UsersViewSet
from goods.views import GoodsViewSet


router = routers.DefaultRouter()

#用户注册
router.register(r'users', UsersViewSet,base_name='users')


#验证码
router.register(r'code', VerifyCodeViewSet,base_name='code')



router.register(r'goods', GoodsViewSet,base_name='goods')



urlpatterns = [
    #Django后台
    path('admin/', admin.site.urls),

    #浏览器图标
    path('favicon.ico', RedirectView.as_view(url='static/favicon.ico')),

    #rest登录
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    #签发token
    path('login/', obtain_jwt_token),
    #刷新token
    path('refresh/', refresh_jwt_token),

    #API路由
    path('', include(router.urls)),

    #富文本
    path('ueditor/',include('DjangoUeditor.urls')),

    #DRF文档
    path('docs/',include_docs_urls(title='DRF接口文档'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)