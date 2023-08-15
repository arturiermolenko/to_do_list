from django.urls import path

from my_list.views import (
    TaskListView,
    TaskUpdateView,
    TaskCreateView,
    TaskDeleteView,
    TagListView,
    TagUpdateView,
    TagCreateView,
    TagDeleteView, toggle_is_done
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("<int:pk>/toggle-is_done/", toggle_is_done, name="toggle-is-done")
]

app_name = "my_list"
