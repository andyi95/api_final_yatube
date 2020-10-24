from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Чтобы не использовать скобки или, что ещё хуже, бэкслэши - удлиним
        # строку - Django CodeStyle одобряе ;)
        return request.method in permissions.SAFE_METHODS or obj.author == request.user
