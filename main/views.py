from django.shortcuts import render
from django.http import HttpResponse
from .models import VacanciesNumberAnalyze, VacanciesSalaryAnalyze, SkillsAnalyze, AreaNumberAnalyze, AreaSalaryAnalyze


def index(request):
    return render(request, 'main/index.html')


def demand(request):
    number_stat = VacanciesNumberAnalyze.objects.all()
    salary_stat = VacanciesSalaryAnalyze.objects.all()
    return render(request, 'main/demand.html', {'number_stat': number_stat, 'salary_stat': salary_stat})


def geo(request):
    share_number_stat = AreaNumberAnalyze.objects.all()
    salary_stat = AreaSalaryAnalyze.objects.all()
    return render(request, 'main/geo.html', {'salary_stat': salary_stat, 'share_number_stat': share_number_stat})


def skills(request):
    skills_stat = SkillsAnalyze.objects.all()
    return render(request, 'main/skills.html', {'skills_stat': skills_stat})
