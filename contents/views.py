from rest_framework.exceptions import NotFound
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from contents.serializers import ContentSerializer
from courses.models import Course
from .models import Content
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.permissions import IsAdminUser, IsOwnerOrAdmin


class ContentCreate(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_url_kwarg = 'course_id'

    def perform_create(self, serializer):
        course = get_object_or_404(Course, id=self.kwargs["course_id"])
        serializer.save(course=course)


class ContentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrAdmin]
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'content_id'

    def get_object(self):
        course_exists = Course.objects.filter(
            id=self.kwargs["course_id"]).exists()
        if not course_exists:
            raise NotFound(detail="course not found.")      
        try:
            return super().get_object()
        except Http404:
            raise NotFound(detail="content not found.")
