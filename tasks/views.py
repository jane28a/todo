from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.decorators import login_required

from tasks.models import Task

@login_required
def index(request):
    user = request.user
    context = {
        'tasks': user.task_set.all()
    }
    return render(request, 'tasks/list.html', context=context)

def details(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        raise Http404('Task does not exist')
    return render(request, 'tasks/details.html', context={'task': task})