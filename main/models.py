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


class AreaSalaryAnalyze(models.Model):
    area = models.TextField('Название города')
    salary = models.PositiveIntegerField('Средняя зарплата')

    def __str__(self):
        return f'Средняя зарплата в городе {self.area}'

    class Meta:
        verbose_name = 'Статистика'
        verbose_name_plural = 'Динамика уровня зарплат по городам'


class AreaNumberAnalyze(models.Model):
    area = models.TextField('Название города')
    stake = models.DecimalField('Доля', max_digits=5, decimal_places=2)

    def __str__(self):
        return f'Доля всех вакансий в городе {self.area}'

    class Meta:
        verbose_name = 'Статистика'
        verbose_name_plural = 'Динамика количества вакансий по городам'


class SkillsAnalyze(models.Model):
    year = models.PositiveIntegerField('Год')
    skills = models.TextField('Топ-10 навыков')

    def __str__(self):
        return f'Топ навыков за {self.year}г.'

    class Meta:
        verbose_name = 'Статистика за год'
        verbose_name_plural = 'Динамика самых встречаемых навыков по годам'


class Vacancy(models.Model):
    name = models.TextField('Название вакансии')
    description = models.TextField('Описание')
    skills = models.TextField('Навыки')
    employer = models.TextField('Навыки')
    salary = models.TextField('Навыки')
    area = models.TextField('Навыки')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return f'{self.name} - {self.date}'

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
