from django.shortcuts import render
from .models import Task
from django.shortcuts import get_object_or_404

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
