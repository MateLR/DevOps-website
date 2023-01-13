# Generated by Django 4.1.5 on 2023-01-12 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VacanciesNumberAnalyze',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(verbose_name='Год')),
                ('number', models.IntegerField(verbose_name='Количество вакансий')),
                ('number2', models.IntegerField(verbose_name='Количество вакансий')),
            ],
            options={
                'verbose_name': 'Статистика за год',
                'verbose_name_plural': 'Динамика количества вакансий по годам',
            },
        ),
    ]