import requests
from datetime import datetime
import re


class Processing:
    def __init__(self, date):
        self.date = date
        self.url = f'https://api.hh.ru/vacancies?clusters=true&enable_snippets=true&st=searchVacancyObj&only_with_salary=true&specialization=1&per_page=10&date_from={date}&date_to={date}&text=devops'
        self.vacancies = []
        self.parse_vacs()

    def to_rows(self):
        return [vac.to_row() for vac in self.vacancies]

    def parse_vacs(self):
        vacs = requests.get(self.url).json()
        new_vacs = []
        for vac in vacs['items']:
            new_vacs.append((vac['id'], vac['published_at']))
        new_vacs.sort(key=lambda tup: tup[1])
        for vac in new_vacs:
            inf = requests.get(f'https://api.hh.ru/vacancies/{vac[0]}').json()
            self.vacancies.append(VacancyObj(inf))


currency = {"AZN": "Манаты",
            "BYR": "Белорусские рубли",
            "EUR": "Евро",
            "GEL": "Грузинский лари",
            "KGS": "Киргизский сом",
            "KZT": "Тенге",
            "RUR": "Рубли",
            "UAH": "Гривны",
            "USD": "Доллары",
            "UZS": "Узбекский сум"}


class VacancyObj:
    def __init__(self, inf: dict):
        self.name = inf['name']
        self.description = self.change_string(inf['description'])
        self.skills = ', '.join(inf['key_skills'][0].values())
        self.employer = inf['employer']['name']
        self.salary = self.salary_to_string(inf['salary'])
        self.area = inf['area']['name']
        self.published_at = datetime.strptime(inf['published_at'], '%Y-%m-%dT%H:%M:%S%z')

    def to_row(self):
        return [self.name, self.description, self.skills, self.employer, self.salary, self.area, self.published_at]

    def salary_to_string(self, salary):
        salary_from = f'от {self.numbers_space(salary["from"])} ' if salary["from"] is not None else ''
        salary_to = f'до {self.numbers_space(salary["to"])}' if salary["to"] is not None else ''
        salary_gross = 'С вычетом налогов' if salary["gross"] else 'Без вычета налогов'
        return f'{salary_from}{salary_to} ({currency[salary["currency"]]}) ({salary_gross})'

    @staticmethod
    def numbers_space(x):
        x = str(x)
        return ' '.join([x[i:i + 3] for i in range(0, len(x), 3)])

    @staticmethod
    def change_string(s):
        s = re.sub("<[^>]*>", "", s).strip()
        if len(s) > 100:
            s = s[:100] + '...'
        return s
