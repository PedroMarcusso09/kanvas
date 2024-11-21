from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.models import Account
from accounts.permissions import IsAdminOrOwner, IsAdminOrReadOnly, IsAdminUser
from courses.models import Course
from courses.serializers import CourseSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from students_courses.models import StudentCourse
from students_courses.serializers import StudentCourseSerializer
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework import status
from rest_framework.response import Response


class CourseListCreateView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Course.objects.all()
        else:
            return self.request.user.my_courses.all()


class CourseRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrOwner]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_url_kwarg = 'course_id'
    lookup_field = 'id'
    

class StudentCourseListView(RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    serializer_class = StudentCourseSerializer
    lookup_field = "course_id"
    queryset = StudentCourse.objects.all()

    def put(self, request, *args, **kwargs):
        course = get_object_or_404(Course, id=self.kwargs["course_id"])

        students_data = request.data.get("students_courses", [])
        for student_data in students_data:
            email = student_data.get('student_email')
            try:
                student = Account.objects.get(email=email)
            except Account.DoesNotExist:
                return Response(
                    {"detail": f"No active accounts was found: {email}."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            if not StudentCourse.objects.filter(
                    course=course, student=student).exists():
                StudentCourse.objects.create(course=course, student=student)
        
        students = StudentCourse.objects.filter(course=course)
        student_serializer = self.get_serializer(students, many=True)
        
        response_data = {
            "id": str(course.id),
            "name": course.name,
            "students_courses": student_serializer.data
        }
                
        return Response(response_data, status=status.HTTP_200_OK)

