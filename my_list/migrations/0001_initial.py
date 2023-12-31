# Generated by Django 4.2.4 on 2023-08-15 06:48

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField(max_length=500)),
                ("date_time", models.DateTimeField(auto_now_add=True)),
                ("deadline", models.DateTimeField(blank=True)),
                ("is_done", models.BooleanField()),
                (
                    "tags",
                    models.ManyToManyField(related_name="tasks", to="my_list.tag"),
                ),
            ],
        ),
    ]
