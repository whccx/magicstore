from rest_framework import permissions

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')

class IsAdminOrReadOnly(permissions.BasePermission):

    message = "只有管理员才可以操作数据。"

    def has_permission(self, request, view):

        return bool(
            request.method in SAFE_METHODS or
            request.user and request.user.is_superuser
        )