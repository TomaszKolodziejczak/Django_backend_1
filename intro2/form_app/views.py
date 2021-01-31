from django.shortcuts import render

# Create your views here.
TASKS = []


def register(request):

    return render(
        request,
        'form_app/register.html',
    )


def task_list(request):
    task = request.POST.get('task')
    if task:
        TASKS.append(task)

    return render(
        request,
        'form_app/list.html',
        {"tasks": TASKS},
    )