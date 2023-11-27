from datetime import datetime

from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic

from todo.forms import TaskForm, TagForm
from todo.models import Task, Tag


def home_page(request: HttpRequest) -> HttpResponse:
    return render(request, "todo/home-page.html")


class TaskListView(generic.ListView):
    model = Task
    template_name = "todo/task_list.html"

    def get_queryset(self):
        return Task.objects.all().order_by('is_done', 'created_at')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_date'] = datetime.now()
        return context


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "todo/task_delete_confirm.html"
    success_url = reverse_lazy("todo:task-list")


class TagListView(generic.ListView):
    model = Tag
    template_name = "todo/tag_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "todo/tag_delete_confirm.html"
    success_url = reverse_lazy("todo:tag-list")


class TaskDoneView(generic.View):
    @staticmethod
    def post(request, pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=pk)
        if task.is_done:
            task.is_done = False
        else:
            task.is_done = True
        task.save()
        return HttpResponseRedirect(reverse("todo:task-list"))
