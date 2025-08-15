from django.shortcuts import render

def base_demo(request):
    return render(request, 'tasks/base.html')

def tasks_home(request):
    return render(request, 'tasks/home.html')

def tasks_list(request):
    return render(request, 'tasks/tasks_list.html')



