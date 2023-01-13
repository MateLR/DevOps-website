from django.contrib import admin
from .models import VacanciesNumberAnalyze, VacanciesSalaryAnalyze, SkillsAnalyze, AreaSalaryAnalyze, AreaNumberAnalyze

admin.site.register(VacanciesNumberAnalyze)
admin.site.register(VacanciesSalaryAnalyze)
admin.site.register(SkillsAnalyze)
admin.site.register(AreaSalaryAnalyze)
admin.site.register(AreaNumberAnalyze)
# Register your models here.
