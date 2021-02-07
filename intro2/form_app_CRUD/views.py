from django.shortcuts import render

# Create your views here.


def register(request):
    return render(
        request,
        'form_app_CRUD/register.html',
    )
