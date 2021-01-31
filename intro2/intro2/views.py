from django.shortcuts import HttpResponse
from django.shortcuts import render


#Przyjmuje http request i zwraca http response
def hello1(request):
    return HttpResponse("Hello")


def hello2(request):
    return HttpResponse("<!DOCTYPE html1><html><head></head><body><h3>Hello!</h3></body></head></html>")


def hello3(request):
    return render(request, 'templates/Hello.html')


def new(request):
    return render(request, 'templates/new.html')

