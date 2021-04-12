from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User


class IsSystemAdmin(BasePermission):
    def has_permission(self, request, view):
        # if User.objects.filter(id=request.user.id, groups__name='Admin'):
        #     return True
        # return False
        return User.objects.filter(id=request.user.id, groups__name='Admin').exists()
