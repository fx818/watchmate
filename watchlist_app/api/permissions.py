# Here we will make our custom permissions
from rest_framework import permissions

class AdminOrReadOnly(permissions.IsAdminUser):
    # Define the type of permission for object or overall
    def has_permission(self, request, view):
        # admin_permission = super().has_permission(request, view)
        # or
        admin_permission = bool(request.user and request.user.is_staff)
        # return request.method == "GET" or admin_permission
        
        # We can also use
        if request.method in permissions.SAFE_METHODS:
            return True # GET Response
        else:
            return bool(request.user and request.user.is_staff)
        

# Only the user who have created the review can edit it, other can only see it
class ReviewUserOrReadOnly(permissions.BasePermission):
    # We will use has_object_permission as we r checking a perticular detail
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # Safe method is GET
            return True
        else:
            # Unsafe methods are put, post, delete etc
            return obj.review_user == request.user