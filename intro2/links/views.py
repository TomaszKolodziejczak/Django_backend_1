from django.shortcuts import render

# Create your views here.


def first(request):
    return render(
        request,
        'links/first.html',
    )


def second(requests):
    return render(
        requests,
        'links/second.html',
    )


def third(request, x):
    return render(
        request,
        'links/third.html',
        context={"text": x}
    )
