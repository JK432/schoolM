from rest_framework import permissions


class IsTeachersSubject(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the user is in the 'teachers' ManyToMany field of the subject
        return request.user in obj.teachers.all()
