from django.shortcuts import render
from .models import Task
from django.shortcuts import get_object_or_404
from .forms import TaskForm
from django.views.generic import CreateView, DeleteView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

def base_demo(request):
    return render(request, 'tasks/base.html')

def tasks_home(request):
    return render(request, 'tasks/home.html')

def tasks_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks_list.html', {"tasks": tasks})

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, "tasks/task_detail.html", {"task": task})

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/add_task.html"
    success_url = reverse_lazy("tasks_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskDeleteView(DeleteView, LoginRequiredMixin):
    model = Task
    template_name = "tasks/confirm_delete.html"
    success_url = reverse_lazy("tasks_list")
    context_object_name = "task"


class TaskNewView(ListView):
    model = Task
    template_name = 'tasks/tasks_list.html'
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.filter(status="new").order_by("-id")


class TaskInProgressView(ListView):
    model = Task
    template_name = 'tasks/tasks_list.html'
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.filter(status="in_progress").order_by("-id")


class TaskCompletedView(ListView):
    model = Task
    template_name = 'tasks/tasks_list.html'
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.filter(status="completed").order_by("-id")