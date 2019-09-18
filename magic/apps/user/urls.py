from django.urls import path,include
from rest_framework import routers
from .views import RegisterViewSet,IndexViewSet


router = routers.DefaultRouter()
router.register(r'registers', RegisterViewSet)
router.register(r'test', IndexViewSet)

urlpatterns = [
    path('', include(router.urls)),
]