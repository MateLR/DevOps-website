from django.shortcuts import render
from django.http import HttpResponse
from .processing import Processing
from .models import VacanciesNumberAnalyze, VacanciesSalaryAnalyze, SkillsAnalyze, AreaNumberAnalyze, AreaSalaryAnalyze, \
    Vacancy


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


def last(request):
    date = '2022-12-19'
    Vacancy.objects.all().delete()
    rows = Processing(date).to_rows()
    for row in rows:
        Vacancy(name=row[0], description=row[1], skills=row[2], employer=row[3], salary=row[4], area=row[5],
                date=row[6]).save()
    vacancies = Vacancy.objects.all()
    return render(request, 'main/last.html', {'vacancies': vacancies})
