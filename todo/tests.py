from django.test import TestCase
from .models import Tag, Task
from datetime import datetime, timedelta


class TaskModelTest(TestCase):

    def setUp(self):
        self.tag1 = Tag.objects.create(name='Tag 1')
        self.tag2 = Tag.objects.create(name='Tag 2')

        self.task1 = Task.objects.create(
            content='Task 1',
            created_at=datetime.now() - timedelta(days=1),
            deadline=datetime.now() + timedelta(days=1),
            is_done=False
        )
        self.task1.tags.add(self.tag1)

        self.task2 = Task.objects.create(
            content='Task 2',
            created_at=datetime.now() - timedelta(days=2),
            deadline=datetime.now() + timedelta(days=2),
            is_done=True
        )
        self.task2.tags.add(self.tag1, self.tag2)

    def test_task_str_method(self):
        self.assertEqual(str(self.task1), 'Task 1')
        self.assertEqual(str(self.task2), 'Task 2')

    def test_task_ordering(self):
        tasks = Task.objects.all()
        self.assertEqual(tasks[0], self.task2)
        self.assertEqual(tasks[1], self.task1)

    def test_tags_associated_with_task(self):
        self.assertEqual(list(self.task1.tags.all()), [self.tag1])
        self.assertEqual(list(self.task2.tags.all()), [self.tag1, self.tag2])
