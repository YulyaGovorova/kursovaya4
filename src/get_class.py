from abc import abstractmethod, ABC
from typing import List

import requests

from setting import SJ_API_KEY
from src.vacancy_class import Vacancy


class API(ABC):
    @abstractmethod
    def get_vacancies(self, query: str) -> List[dict]:
        pass


class HHAPI(API):
    def __init__(self, keyword, page=0):
        self.url = "https://api.hh.ru/vacancies"
        self.params = {
            "text": keyword,
            "page": page,
            "per_page": 100,
            "search_field": "name",
        }

    def get_request(self):
        response = requests.get(self.url, params=self.params)
        return response.json()['items']

    def get_vacancies(self, query: str) -> List[dict]:
        return self.get_request()

    def get_hh_vacancies(self):
        vacancies = self.get_request()

        hh_vacancies = []
        for vacancy in vacancies:
            name = vacancy['name']
            salary = vacancy["salary"]["from"] if vacancy["salary"] else None
            link = vacancy['alternate_url']
            hh_vacancies.append(Vacancy(name, salary, link))

        return hh_vacancies


class SJAPI(API):
    def __init__(self, keyword):
        self.url = "https://api.superjob.ru/2.0/vacancies/"
        self.headers = {'X-Api-App-Id': SJ_API_KEY}
        self.params = {
            "town": 4,
            "catalogues": 48,
            "keywords": keyword,
            "count": 100
        }

    def get_request(self):
        response = requests.get(self.url, headers=self.headers, params=self.params)
        return response.json()['objects']

    def get_vacancies(self, query: str) -> List[dict]:
        return self.get_request()

    def get_superjob_vacancies(self):
        vacancies = self.get_request()

        sj_vacancies = []
        for vacancy in vacancies:
            name = vacancy['profession']
            salary = vacancy['payment_from']
            link = vacancy['link']
            sj_vacancies.append(Vacancy(name, salary, link))

        return sj_vacancies
