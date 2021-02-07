from django.shortcuts import render
from form_app2.models import Task
# Create your views here.


def register(request):

    return render(
        request,
        'form_app2/register.html'
    )


def task_list(request):

    task = request.POST.get('task')

    if task:
        Task.objects.create(name=task)

    tasks = Task.objects.all()

    return render(
        request,
        'form_app2/task_list.html',
        context={
            "tasks": tasks,
        }
    )
