from rest_framework import serializers

from .models import Task
from api.serializers import UserPublicSerializer

class TaskSerializer(serializers.ModelSerializer):
    author = UserPublicSerializer(read_only=True)
    class Meta:
        model = Task
        fields = [
            'pk',
            'title',
            'description',
            'created',
            'author'
        ]