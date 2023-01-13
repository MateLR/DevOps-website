from django.db import models


# year,key_skills,salary_from,salary_to,salary_currency,area_year,published_at
class VacanciesNumberAnalyze(models.Model):
    year = models.PositiveIntegerField('Год')
    number = models.PositiveIntegerField('Количество вакансий')
    number_by_job = models.PositiveIntegerField('Количество вакансий для Devops')

    def __str__(self):
        return f'Количество вакансий за {self.year}г.'

    class Meta:
        verbose_name = 'Статистика за год'
        verbose_name_plural = 'Динамика количества вакансий по годам'


class VacanciesSalaryAnalyze(models.Model):
    year = models.PositiveIntegerField('Год')
    salary = models.PositiveIntegerField('Средняя зарплата')
    salary_by_job = models.PositiveIntegerField('Средняя зарплата для Devops')

    def __str__(self):
        return f'Средняя зарплата за {self.year}г.'

    class Meta:
        verbose_name = 'Статистика за год'
        verbose_name_plural = 'Динамика уровня зарплат по годам'
