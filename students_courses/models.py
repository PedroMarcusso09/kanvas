from uuid import uuid4
from django.db import models


class StudentCourseStatus(models.TextChoices):
    DEFAULT = 'pending', 'Pending'
    ACCEPTED = 'accepted', 'Accepted'


class StudentCourse(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid4, editable=False, unique=True
    )
    status = models.CharField(  
        max_length=50, choices=StudentCourseStatus.choices,
        default=StudentCourseStatus.DEFAULT
    )
    course = models.ForeignKey(
        'courses.Course', on_delete=models.CASCADE,
        related_name='students_courses'
    )
    student = models.ForeignKey(
        'accounts.Account', on_delete=models.CASCADE,     
        related_name='students_courses'
    )
