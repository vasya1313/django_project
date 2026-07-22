from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        #Разрешает чтение всем, а запись - только аутентифицированным пользователям.
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated


    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS or obj.author == request.user
