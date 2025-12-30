
from django.shortcuts import render
from todo.models import Task

def home(request):
    task = Task.objects.filter(is_completed=True)
    context = {
        'task': task,
    }
    return render(request, 'home.html', context)