from django.urls import path
from .import views
from contents.views import ContentCreate, ContentRetrieveUpdateDestroy

app_name = "courses"

urlpatterns = [
    path(
        '',
        views.CourseListCreateView.as_view(),
        name='list-create-course'
    ),
    path(
        '<uuid:course_id>/',
        views.CourseRetrieveUpdateDestroy.as_view(),
        name='retrieve-update-destroy-course'
    ),
    path(
        '<uuid:course_id>/students/',
        views.StudentCourseListView.as_view(),
        name='manage-students'
    ),
    path(
        '<uuid:course_id>/contents/',
        ContentCreate.as_view(),
        name='add-content'
    ),
    path(
        '<uuid:course_id>/contents/<uuid:content_id>/',
        ContentRetrieveUpdateDestroy.as_view(),
        name='manage-content'
    ),
]