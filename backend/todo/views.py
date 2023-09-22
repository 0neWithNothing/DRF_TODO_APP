from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework import permissions
from django.contrib.auth import get_user_model
from django.utils import timezone
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from rest_framework.decorators import api_view
from drf_spectacular.utils import extend_schema

from .models import Task
from .serializers import TaskSerializer
from api.mixins import TaskQuerySetMixin


# class TaskViewSet(viewsets.ModelViewSet):
#     serializer_class = TaskSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         return Task.objects.filter(author=self.request.user.id, completed__isnull=True)


# CRUD TODO

class TaskListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user.id, completed__isnull=True)


class TaskListCompletedAPIView(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user.id, completed__isnull=False)


class TaskDetailAPIView(TaskQuerySetMixin, generics.RetrieveAPIView):
    serializer_class = TaskSerializer


class TaskUpdateAPIView(TaskQuerySetMixin, generics.RetrieveUpdateAPIView):
    serializer_class = TaskSerializer


class TaskDestroyAPIView(TaskQuerySetMixin, generics.RetrieveDestroyAPIView):
    serializer_class = TaskSerializer


class TaskCompleteAPIView(TaskQuerySetMixin, APIView):
    def get_object(self, pk):
        return self.get_queryset().get(pk=pk)
    
    def patch(self, request, pk):
        task = self.get_object(pk)
        if task.completed:
            task.completed = None
        else:
            task.completed = timezone.now()

        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=200, data=serializer.data)
        return Response(status=400, data="wrong parameters")
