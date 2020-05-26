from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    message = 'You must be the owner of this post.'

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
