from django.urls import path

from . import views

urlpatterns = [
    path('', views.TaskListCreateAPIView.as_view(), name='task-list'),
    path('<int:pk>/', views.TaskDetailAPIView.as_view(), name='task-detail'),
    path('<int:pk>/update/', views.TaskUpdateAPIView.as_view(), name='task-update'),
    path('<int:pk>/delete/', views.TaskDestroyAPIView.as_view(), name='task-delete'),
]