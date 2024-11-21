from django.urls import path
from .import views
from contents.views import ContentCreate, ContentRetrieveUpdateDestroy


urlpatterns = [
    path('courses/', views.CourseListCreateView.as_view()),
    path('courses/<uuid:course_id>/', 
         views.CourseRetrieveUpdateDestroy.as_view()),
    path('courses/<uuid:course_id>/students/',
         views.StudentCourseListView.as_view()),
    path("courses/<uuid:course_id>/students/<uuid:student_id>/",
         views.StudentCourseListView.as_view()),
    path('courses/<uuid:course_id>/contents/',
         ContentCreate.as_view()),
    path('courses/<uuid:course_id>/contents/<uuid:content_id>/',
         ContentRetrieveUpdateDestroy.as_view())
]