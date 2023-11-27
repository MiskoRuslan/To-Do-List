from django.urls import path

from todo.views import (home_page,
                        TaskListView,
                        TaskCreateView,
                        TaskUpdateView,
                        TaskDeleteView,
                        TagListView,
                        TagCreateView,
                        TagUpdateView,
                        TagDeleteView, TaskDoneView)

urlpatterns = [
    path("", home_page, name="home-page"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/update/<int:pk>/,", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/delete/<int:pk>/,", TaskDeleteView.as_view(), name="task-delete"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/update/<int:pk>/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/delete/<int:pk>/", TagDeleteView.as_view(), name="tag-delete"),
    path('task-done/<int:pk>/', TaskDoneView.as_view(), name='task-done'),
]

app_name = "todo"
