from django.shortcuts import render

from tasks.models import Task


def index(request):
    context = {
        'tasks': Task.objects.all()
    }
    return render(request, 'tasks/tasks.html', context=context)