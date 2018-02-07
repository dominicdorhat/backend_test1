# rest_api/permissions.py 

from rest_framework.permissions import BasePermission
from .models import Servant

class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Servant):
            return obj.master == request.user
        return obj.master == request.user