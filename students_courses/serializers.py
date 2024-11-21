from rest_framework import serializers
from .models import StudentCourse


class StudentCourseSerializer(serializers.ModelSerializer):
    student_email = serializers.EmailField(
        source='student.email', read_only=True)
    student_username = serializers.CharField(
        source='student.username', read_only=True)
    student_id = serializers.UUIDField(
        source='student.id', read_only=True)

    class Meta:
        model = StudentCourse
        fields = [
            'id', 'status', 'student_email','student_username', 'student_id'
        ]


