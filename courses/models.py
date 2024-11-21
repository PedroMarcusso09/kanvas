from uuid import uuid4
from django.db import models


class CourseStatus(models.TextChoices): 
    DEFAULT = 'not started', 'Not Started'
    IN_PROGRESS = 'in progress', 'In Progress'
    FINISHED = 'finished', 'Finished'


class Course(models.Model):

    id = models.UUIDField(
        primary_key=True, default=uuid4, editable=False, unique=True
    )    
    name = models.CharField(max_length=100, unique=True)
    status = models.CharField(
        max_length=11, choices=CourseStatus.choices,
        default=CourseStatus.DEFAULT
    )
    start_date = models.DateField()
    end_date = models.DateField()
    instructor = models.ForeignKey(
        'accounts.Account', on_delete=models.CASCADE, 
        related_name='courses', null=True
    )
