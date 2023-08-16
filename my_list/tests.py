from django.http import HttpRequest
from django.test import TestCase

from my_list.models import Task, Tag
from my_list.views import ToggleView


class ModelStrTests(TestCase):
    def test_task_str(self):
        self.task = Task.objects.create(
            content="test content",
            is_done=True
        )
        self.assertEqual(
            str(self.task),
            self.task.content
        )

    def test_tag_str(self):
        self.tag = Tag.objects.create(
            name="test tag"
        )
        self.assertEqual(
            str(self.tag),
            self.tag.name
        )


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
