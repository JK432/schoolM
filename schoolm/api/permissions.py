from rest_framework import permissions


class TeachersOwnSubject(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user in obj.teachers:
            return True


class TeachersOwnTeacher(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True

# class TeachersOwnMark(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.user in obj.user:
#             return True