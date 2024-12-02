from .models import Content
from rest_framework import serializers


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['id', 'name', 'content', 'video_url', 'course']
        extra_kwargs = {
            'course': {'required': False, 'write_only': True}
        }