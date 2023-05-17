from django.urls import path
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView


urlpatterns = [
    path('', TaskListView.as_view(), name="tasks-list"),
    path('create/', TaskCreateView.as_view, name="task-create"),
    path('update/<int:pk>/', TaskUpdateView.as_view(), name="task-update"),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name="task-delete"),
]