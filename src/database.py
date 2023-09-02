import json
import os
from abc import abstractmethod, ABC

from src.vacancy_class import Vacancy


class VacancySaver(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy):
        pass

    @abstractmethod
    def get_vacancies_by_salary(self, salary: str) -> list[Vacancy]:
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy):
        pass


class JSONSaver(VacancySaver):
    def __init__(self, filename):
        self.filename = filename

    def add_vacancy(self, vacancies: list[Vacancy]):
        if not self.filename.endswith('.json'):
            self.filename = self.filename + '.json'

        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as file:
                json.dump([], file, indent=4, ensure_ascii=False)

        with open(self.filename, 'r', encoding='utf-8') as file:
            data = json.load(file)

        for vacancy in vacancies:
            data.append(vars(vacancy))

        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def get_vacancies_by_salary(self, salary: str) -> list[Vacancy]:
        with open(self.filename, 'r') as file:
            data = json.load(file)

        vacancies = []
        for vacancy_data in data:
            vacancy = Vacancy(**vacancy_data)
            if vacancy.salary == salary:
                vacancies.append(vacancy)

        return vacancies

    def delete_vacancy(self, vacancy: Vacancy):
        with open(self.filename, 'r') as file:
            data = json.load(file)

        for vacancy_data in data:
            if (
                    vacancy_data['name'] == vacancy.name
                    and vacancy_data['salary'] == vacancy.salary
                    and vacancy_data['link'] == vacancy.link
            ):
                data.remove(vacancy_data)
                break

        with open(self.filename, 'w') as file:
            json.dump(data, file)
