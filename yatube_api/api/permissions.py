from rest_framework import permissions

# Очень интересно что в теории об этом ничего не говорятся
class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)
