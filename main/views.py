from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')


def stat(request):
    return render(request, 'main/demand2.html')
