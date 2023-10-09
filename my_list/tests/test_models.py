from django.test import TestCase

from my_list.models import Task, Tag


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
