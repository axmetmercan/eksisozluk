from django.forms import ValidationError
from rest_framework import permissions as per


class IsAuthenticatedAndBelongsToOrAdmin(per.BasePermission):

    def has_object_permission(self, request, view, obj):

        isAuth = super().has_object_permission(request, view, obj)
        
        isAuth = (isAuth and (obj.created_by == request.user))  
        if isAuth or request.method in per.SAFE_METHODS:
            return True
        return False

class IsAuthenticatedAndBelongsTo(per.BasePermission):

    def has_object_permission(self, request, view, obj):

        isAuth = super().has_object_permission(request, view, obj)
        
        isAuth = (isAuth and (obj.user == request.user))
        if isAuth or request.method in per.SAFE_METHODS:  
            return True
        return False


class TitleCreatePermission(per.BasePermission):

    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:

            stat = request.user.status
            if request.user.is_superuser or request.user.status == 'PR':
                return True
        return False

    

