from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'is_complited', 'author')
    fields = ('title', 'description', 'priority', 'is_complited', 'author')
    search_fields = ('title', 'description')
    list_filter = ('priority', 'is_complited', 'author', 'created', 'updated')


# Register your models here.
