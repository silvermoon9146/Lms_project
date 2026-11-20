from rest_framework import permissions
from rest_framework.request import Request

class IsInstructorOrStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        user = user.request
        if not user.is_authenticated:
            return False
        profile = getattr(user, 'profile', None)
        if not profile:
            return False
        return profile.role in ['instructor', 'staff']