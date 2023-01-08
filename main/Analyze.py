import pandas as pd
from jinja2 import Environment, FileSystemLoader


# name,key_skills,salary_from,salary_to,salary_currency,area_name,published_at
class DataSet(object):
    """Класс, который преобразует csv файл в базу данных информации о вакансиях, и анализирует эту информацию
    Attributes:
        file_path (str)
        salary_by_years (dict): Словарь с зарплатами по годам
        number_by_years (dict): Словарь с количеством вакансий по годам
        salary_by_years_job (dict): Словарь с зарплатами по годам, по выбранной профессии
        number_by_years_job (dict): Словарь с количеством вакансий по годам, по выбранной профессии
        salary_by_area (dict): Словарь с зарплатами по регионам
        share_number_by_area (dict): Словарь с количеством зарплат по регионам
    """

    def __init__(self):
        """Инициализирует объект DataSet, преобразует файл с вакансиями в список вакансий
        Args:
            file_path: Имя файла
        """
        self.file_path = "vacancies/vacancies_salary_in_rub.csv"
        self.job_name = "Devops-инженер"
        self.job_names = ["devops", "development operations"]
        self.salary_by_years = dict()
        self.number_by_years = dict()
        self.salary_by_years_job = dict()
        self.number_by_years_job = dict()
        self.salary_by_area = dict()
        self.share_number_by_area = dict()
        self.analyze()

    def analyze(self):
        df = pd.read_csv(self.file_path)
        df = df[df["salary"].notnull()]
        df["salary"] = df["salary"].apply(lambda x: int(x))
        df["published_at"] = df["published_at"].apply(lambda d: int(d[:4]))
        years = df["published_at"].unique()
        df_vacancy = df["name"].str.contains('|'.join(self.job_names))

        for year in years:
            filter_by_year = df["published_at"] == year
            self.salary_by_years[year] = int(df[filter_by_year]["salary"].mean())
            self.number_by_years[year] = len(df[filter_by_year])
            self.salary_by_years_job[year] = int(
                df[df_vacancy & filter_by_year]["salary"].mean() if df[df_vacancy & filter_by_year][
                    "salary"].any() else 0)
            self.number_by_years_job[year] = len(df[df_vacancy & filter_by_year])

        count = len(df)
        df["count"] = df.groupby("area_name")["area_name"].transform("count")
        df_norm = df[df["count"] > 0.01 * count]
        df_area = df_norm.groupby("area_name", as_index=False)["salary"].mean().sort_values(by="salary",
                                                                                            ascending=False)
        df_area["salary"] = df_area["salary"].apply(lambda x: int(x))
        df_area10 = df_area.head(10)
        self.salary_by_area = dict(zip(df_area10["area_name"], df_area10["salary"]))

        self.share_number_by_area = {k: round(v / count, 6) for k, v in
                                     dict(df["area_name"].value_counts().head(10)).items()}


class Report:
    def __init__(self):
        self.dataset = DataSet()

    def analyze_to_rows_html(self):
        """Преобразовывает словари с анализом из базы данных в строки для html файла, который генерирует таблицу для pdf файла
        """
        headers1 = ["Год", "Средняя зарплата", "Количество вакансий",
                    f"Средняя зарплата - {self.dataset.job_name}",
                    f"Количество вакансий - {self.dataset.job_name}"]
        rows1 = []
        for year in self.dataset.salary_by_years.keys():
            rows1.append(
                [year, self.dataset.salary_by_years[year], self.dataset.number_by_years[year],
                 self.dataset.salary_by_years_job[year],
                 self.dataset.number_by_years_job[year]])
        headers2 = ["Город", "Уровень зарплат", "", "Город", "Доля вакансий"]
        salary_items = [(k, v) for k, v in self.dataset.salary_by_area.items()]
        share_number_items = [(k, v) for k, v in self.dataset.share_number_by_area.items()]
        rows2 = []
        for i in range(10):
            rows2.append([salary_items[i][0], salary_items[i][1], "",
                          share_number_items[i][0],
                          f'{round(share_number_items[i][1] * 100, 3)}%'])
        return headers1, headers2, rows1, rows2

    def generate_html(self):
        env = Environment(loader=FileSystemLoader('.'))
        template = env.get_template("templates/analyze/demand_template.html")
        tables = self.analyze_to_rows_html()
        # str_template = template.render(
        #     {'name': self.dataset.job_name, 'headers1': tables[0], 'headers2': tables[1], 'rows1': tables[2],
        #      'rows2': tables[3]}).dump('templates/main/demand2.html')
        template.stream(name=self.dataset.job_name, headers1=tables[0], headers2=tables[1], rows1=tables[2],
                        rows2=tables[3]).dump(
            'templates/main/demand2.html')
        # with open("templates/main/demand2.html", "w") as file:
        #     file.write(str_template)


Report().generate_html()
