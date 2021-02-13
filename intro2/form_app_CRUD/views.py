from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect
from form_app_CRUD.models import Task
from django.shortcuts import Http404
from django.views.decorators.http import require_http_methods


# Create your views here.


def register(request):
    return render(
        request,
        'form_app_CRUD/register.html',
    )


def task_list(request):

    if request.method == "POST":
        task = request.POST.get('task')

        if task:
            Task.objects.create(name=task)

        return redirect("form_app_CRUD:task_list")

    tasks = Task.objects.all()  # queryset

    return render(
        request,
        'form_app_CRUD/task_list.html',
        context={"tasks": tasks}
    )


def update(request, task_id):

    if request.method == "GET":
        # try:
        #     task = Task.objects.get(pk=task_id)
        # except ObjectDoesNotExist:
        #     raise Http404

        task = get_object_or_404(Task, id=task_id)

        return render(
            request,
            'form_app_CRUD/update.html',
            context={
                'task': task
            }
        )
    if request.method == "POST":
        updated_task = request.POST.get('task')

        if updated_task:
            task = Task.objects.get(pk=task_id)
            task.name = updated_task
            task.save()

        tasks = Task.objects.all()

        # return render(
        #     request,
        #     'form_app_CRUD/task_list.html',
        #     context={"tasks": tasks}
        # )
        return redirect("form_app_CRUD:task_list")


@require_http_methods(["POST"])
def delete(request, task_id):

    task = get_object_or_404(Task, id=task_id)
    task.delete()

    # return render(
    #     request,
    #     'form_app_CRUD/delete.html',
    # )
    return redirect("form_app_CRUD:task_list")
