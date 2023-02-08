from django.shortcuts import render
from django.http import Http404

from tasks.models import Task


def index(request):
    return render(request, 'tasks/base.html', context={})
    '''
    context = {
        'tasks': Task.objects.all()
    }
    return render(request, 'tasks/tasks.html', context=context)
    '''

def details(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        raise Http404('Task does not exist')
    return render(request, 'tasks/details.html', context={'task': task})