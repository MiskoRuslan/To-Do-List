from datetime import datetime, timedelta
from django.utils import timezone
from todo.forms import TaskForm, TagForm
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from todo.models import Task, Tag


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


class TaskFormTest(TestCase):

    def test_task_form_invalid_data(self):
        form_data = {
            'deadline': str(timezone.now()),
            'is_done': False,
        }
        form = TaskForm(data=form_data)
        self.assertFalse(form.is_valid())


class TagFormTest(TestCase):
    def test_tag_form_valid_data(self):
        form_data = {
            'name': 'Test Tag',
        }
        form = TagForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_tag_form_invalid_data(self):
        form_data = {}
        form = TagForm(data=form_data)
        self.assertFalse(form.is_valid())


class AdminPanelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.user.is_staff = True
        self.user.is_superuser = True
        self.user.save()

        self.client = Client()
        self.client.login(username='testuser', password='testpassword')

    def test_task_admin_panel(self):
        task = Task.objects.create(content='Test Task', is_done=False)
        url = reverse('admin:todo_task_change', args=[task.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_tag_admin_panel(self):
        tag = Tag.objects.create(name='Test Tag')
        url = reverse('admin:todo_tag_change', args=[tag.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
