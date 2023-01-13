from django.shortcuts import render
from django.http import HttpResponse
from .models import VacanciesNumberAnalyze,VacanciesSalaryAnalyze


def index(request):
    return render(request, 'main/index.html')


def demand(request):
    number_stat = VacanciesNumberAnalyze.objects.all()
    salary_stat = VacanciesSalaryAnalyze.objects.all()
    return render(request, 'main/demand.html', {'number_stat': number_stat, 'salary_stat': salary_stat})


def geo(request):
    return render(request, 'main/geo.html')
