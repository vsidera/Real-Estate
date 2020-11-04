from rest_framework.permissions import BasePermission

class IsCompanyAdmin(BasePermission):
    
    message = "You must be a company admin to acess this page"

    def has_permission(self, request, view):
        """ check if the object has permission """

        user = request.user

        if user is not None and user.is_authenticated:
            return user.role == 'CA'

class IsNormalUser(BasePermission):
    message = "You must be a user to acess this page"

    def has_permission(self, request, view):
        """ check if the object has permission """

        user = request.user

        if user is not None and user.is_authenticated:
            return user.role == 'NU'