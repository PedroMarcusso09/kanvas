from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser
from courses.models import Course


class Account(AbstractUser):
    id = models.UUIDField(
        primary_key=True, default=uuid4, editable=False, unique=True
    )
    email = models.EmailField(max_length=100, unique=True)
    my_courses = models.ManyToManyField(
        Course, through='students_courses.StudentCourse',
        related_name='students'
    )
