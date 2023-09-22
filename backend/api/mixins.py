from rest_framework import permissions

from todo.models import Task


class TaskQuerySetMixin():
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user.id)