from django.db import models
from django.contrib.auth.models import User
class Task(models.Model):
    HIGH = 'high'
    NORMAL = 'normal'
    LOW = 'low'
    TYPES = (
        (HIGH, 'High'),
        (NORMAL, 'Normal'),
        (LOW, 'Low')
    )
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    priority = models.CharField(max_length=20, choices=TYPES, default=NORMAL)
    is_complited = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
# Create your models here.
