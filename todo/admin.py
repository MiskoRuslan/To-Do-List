from django.contrib import admin

from todo.models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['content', 'created_at', 'deadline', 'is_done']
    list_filter = ['is_done', 'created_at']
    search_fields = ['content']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
