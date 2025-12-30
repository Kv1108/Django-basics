
from django.shortcuts import render
from todo.models import Task

def home(request):
    task = Task.objects.filter(is_completed=False).order_by('updated_at')
    context = {
        'task': task,
    }
    return render(request, 'home.html', context)