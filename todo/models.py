from django.db import models
from django.utils import timezone

class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return self.content

    class Meta:
        ordering = ['is_done', '-created_at']

    def save(self, *args, **kwargs):
        if self.deadline:
            self.deadline = timezone.make_aware(self.deadline)
        super().save(*args, **kwargs)
