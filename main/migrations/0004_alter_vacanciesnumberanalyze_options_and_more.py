# Generated by Django 4.1.5 on 2023-01-13 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_vacanciesnumberanalyze_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vacanciesnumberanalyze',
            options={'verbose_name': 'Статистика за год', 'verbose_name_plural': 'Динамика количества вакансий по годам'},
        ),
        migrations.AddField(
            model_name='vacanciesnumberanalyze',
            name='number_by_job',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество вакансий для Devops'),
            preserve_default=False,
        ),
    ]
