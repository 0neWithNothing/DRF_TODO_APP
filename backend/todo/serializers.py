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


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'], password=validated_data['password'])
        return user