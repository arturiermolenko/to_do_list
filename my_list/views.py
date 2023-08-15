from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render

from my_list.forms import TaskForm, TagForm
from my_list.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("my_list:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("my_list:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("my_list:task-list")


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("my_list:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("my_list:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("my_list:tag-list")
