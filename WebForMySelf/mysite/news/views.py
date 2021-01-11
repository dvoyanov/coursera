from django.shortcuts import render
from django.http import HttpResponse

def index(requests):
    #print(dir(requests))
    return HttpResponse('Hello world!')

def test(requests):
    return HttpResponse('<h1>Тестова страница</h1>')