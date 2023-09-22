from django.urls import path, include
# from rest_framework import routers

from . import views

# router = routers.DefaultRouter()
# router.register(r'tasks', views.TaskViewSet, basename='Task')

urlpatterns = [
    # path('v2/', include(router.urls)),
    path('', views.TaskListCreateAPIView.as_view()),
    path('completed/', views.TaskListCompletedAPIView.as_view()),
    path('<int:pk>/', views.TaskDetailAPIView.as_view()),
    path('<int:pk>/complete/', views.TaskCompleteAPIView.as_view()),
    path('<int:pk>/update/', views.TaskUpdateAPIView.as_view()),
    path('<int:pk>/delete/', views.TaskDestroyAPIView.as_view()),
]