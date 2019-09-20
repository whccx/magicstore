from rest_framework.permissions import BasePermission

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')

class IsAdminOrReadOnly(BasePermission):

    message = "只有管理员才可以操作数据。"

    def has_permission(self, request, view):

        return bool(
            request.method in SAFE_METHODS or
            request.user and request.user.is_superuser
        )

class IsOwner(BasePermission):

    message = "用户只能查看自己的订单。"

    def has_object_permission(self, request, view, obj):

        return obj.buy_phone == request.user

