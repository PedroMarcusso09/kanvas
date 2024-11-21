from rest_framework import permissions


class isAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated

        return request.user.is_superuser


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        is_instructor = request.user == obj.course.instructor
     
        is_student = request.user in obj.course.students.all()
     
        return request.user.is_authenticated and (
            is_instructor or request.user.is_superuser or is_student
        )


class IsAdminUser(permissions.BasePermission):

    def has_permission(self, request, view):

        return request.user.is_superuser


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_superuser


class IsStudentOrAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        if request.user.is_authenticated:
            return obj.students.filter(student=request.user).exists()
        return False

    
class IsAdminOrOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        return (request.user.is_authenticated
                and obj == request.user
                and request.method == permissions.SAFE_METHODS
                or request.user.is_superuser)

