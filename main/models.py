from django.db import models


# name,key_skills,salary_from,salary_to,salary_currency,area_name,published_at
class Vacancy(models.Model):
    name = models.TextField('Название')
    description = models.TextField('Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
