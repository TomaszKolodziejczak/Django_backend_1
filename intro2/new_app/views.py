from datetime import datetime
from random import shuffle

from django.shortcuts import HttpResponse, render


# Create your views here.


def helloB(request):
    return render(request, 'new_app/helloB.html')


def bartek(request):
    return HttpResponse('Witaj, Bartek')


def ewa(request):
    return HttpResponse('Witaj, Ewa')


def display_name(request, name, age):
    a_list = [item for item in name]
    shuffle(a_list)
    shuffled_name = ''.join(a_list)
    return HttpResponse(f'Witaj, {shuffled_name.title()}! lat {age}')


def display_name2(request, name):
    my = 'Pozdrawiam!!'
    return render(
              request,
              'new_app/name.html',
              context={
                  'name': name.title(),
                  'add': my
              }
    )


def is_it_newyear(request):
    """jinja conditions"""
    now = datetime.now()
    is_new_year = now.day == 1 and now.month == 1

    return render(
        request,
        'new_app/is_it_newyear.html',
        {'is_new_year': is_new_year,
        }
    )


def fruits(request):
    """Jinja loops"""

    fruits = ['apple', 'banana', 'grapes', 'cherry']
    return render(
        request,
        'new_app/fruits.html',
        {'fruits': fruits}
    )



