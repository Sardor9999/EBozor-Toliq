from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from .forms import TaskForm, TaskUpdateForm
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator

class TaskListView(LoginRequiredMixin, ListView):
    login_url = 'users/login'
    template_name = 'task/list.html'
    context_object_name = 'tasks'
    paginate_by = 3

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user).order_by('-id')


class TaskCreateView(LoginRequiredMixin, ListView):
    login_url = 'users/login'
    template_name = 'task/crate.html'
    form_class = TaskForm

    def get(self, request):
        form = TaskForm
        return render(request, 'task/create.html', {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.save()
            return redirect('tasks-list')
        return HttpResponse("New task is not valied")

class TaskUpdateView(LoginRequiredMixin, View):
    login_url = '/users/login/'

    def get(self, request,pk):
        task = get_object_or_404(Task, pk=pk)
        form = TaskUpdateForm(instance=task)
        return render(request, "task/update.html", {"form": form, "task": task})

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        form = TaskUpdateForm(instance=task, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks-list')
        return HttpResponse('Task data is not valid')

class TaskDeleteView(LoginRequiredMixin, View):
    login_url = '/users/login/'
    def get(self, request,pk):
        task = get_object_or_404(Task, pk=pk)
        return render(request, "task/delete.html", {"task": task})

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect('tasks-list')


# Create your views here.
