import datetime

from django.http import HttpRequest
from django.test import TestCase
from django.urls import reverse

from my_list.models import Task, Tag
from my_list.views import ToggleView

TASK_LIST_URL = reverse("my_list:task-list")
TAG_LIST_URL = reverse("my_list:tag-list")


class ToggleTests(TestCase):
    def test_toggle_view(self):
        flag = True
        self.task = Task.objects.create(
            content="test content",
            is_done=flag
        )
        request = HttpRequest()
        request.method = "POST"
        response = ToggleView.post(request, pk=self.task.id)
        self.task.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            self.task.is_done,
            not flag
        )


class TaskEndpointTests(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(
            name="test tag"
        )

    def test_retrieve_tasks_list(self):
        for index in range(10):
            Task.objects.create(
                content=f"test content {index}",
                is_done=True,
            )
        response = self.client.get(TASK_LIST_URL)
        tasks = Task.objects.all()

        self.assertEqual(
            list(response.context["task_list"]),
            list(tasks)
        )
        self.assertTemplateUsed(response, "my_list/task_list.html")

    def test_create_task_view(self):
        form_data = {
            "content": "Test content111",
            "deadline": datetime.datetime.now(),
            "is_done": True,
            "tags": [self.tag.id]
        }

        response = self.client.post(reverse("my_list:task-create"), form_data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 1)

    def test_update_task_view(self):
        task = Task.objects.create(
            content=f"test content",
            is_done=True,
        )
        form_data = {
            "content": "Test content111",
            "deadline": datetime.datetime.now(),
            "is_done": False,
            "tags": [self.tag.id]
        }
        response = self.client.post(reverse("my_list:task-update", args=[task.pk]), form_data)

        self.assertEqual(response.status_code, 302)

    def test_delete_task(self):
        self.task = Task.objects.create(
            content="test content",
            is_done=True,
        )

        self.client.post(reverse("my_list:task-delete", args=[self.task.pk]))

        self.assertEqual(Task.objects.count(), 0)


class TagEndpointTests(TestCase):

    def test_retrieve_tag_list(self):
        for index in range(10):
            Tag.objects.create(
                name=f"tag {index}",
            )
        response = self.client.get(TAG_LIST_URL)
        tags = Tag.objects.all()

        self.assertEqual(
            list(response.context["tag_list"]),
            list(tags)
        )
        self.assertTemplateUsed(response, "my_list/tag_list.html")

    def test_create_task_view(self):
        form_data = {
            "name": "new tag"
        }

        response = self.client.post(reverse("my_list:tag-create"), form_data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Tag.objects.count(), 1)

    def test_update_task_view(self):
        tag = Tag.objects.create(
            name="new test tag"
        )
        form_data = {
            "name": "very new tag"
        }
        response = self.client.post(reverse("my_list:tag-update", args=[tag.pk]), form_data)

        self.assertEqual(response.status_code, 302)

    def test_delete_task(self):
        self.tag = Tag.objects.create(
            name="tag for delete"
        )

        self.client.post(reverse("my_list:tag-delete", args=[self.tag.pk]))

        self.assertEqual(Tag.objects.count(), 0)
