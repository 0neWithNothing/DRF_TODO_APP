from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Task
from api.serializers import UserPublicSerializer

User = get_user_model()


class TaskSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    completed = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Task
        fields = [
            'pk',
            'title',
            'description',
            'created',
            'completed',
            'author'
        ]
