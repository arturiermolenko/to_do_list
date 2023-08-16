from datetime import datetime

from django.test import TestCase

from my_list.forms import TaskForm
from my_list.models import Tag


class FormsTests(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(
            name="test tag"
        )

    def test_task_creation_form(self):
        tags_set = Tag.objects.all()
        form_data = {
            "content": "Test content111",
            "deadline": datetime.now(),
            "is_done": True,
            "tags": tags_set
        }

        form = TaskForm(data=form_data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.data,
                         form_data)
