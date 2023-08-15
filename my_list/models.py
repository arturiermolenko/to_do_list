from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField(max_length=500)
    date_time = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    is_done = models.BooleanField()
    tags = models.ManyToManyField(Tag, related_name="tasks")

    def __str__(self):
        return self.content
