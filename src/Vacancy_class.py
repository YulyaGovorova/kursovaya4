import json
import os
from abc import ABC, abstractmethod
from typing import List

import requests

from setting import SJ_API_KEY


class Vacancy(ABC):
    def __init__(self, name, salary, link):
        self.name = name
        self.salary = salary
        self.link = link

    @abstractmethod
    def get_vacancies(self, query: str) -> List[dict]:
        hh_api = HHAPI()
        vacancies = hh_api.get_vacancies(query)


class HHAPI(Vacancy):
    def __init__(self, keyword, page=0):
        # Подключение к API платформы hh.ru
        self.url = "https://api.hh.ru/vacancies"
        self.params = {
            "text": keyword,
            "page": page,
            "per_page": 100,
            "search_field": "name",
        }

    def get_request(self):
        return requests.get(self.url, params=self.params).json()



class SuperJobAPI(Vacancy):
    def __init__(self, keyword, name=None, salary=None, link=None, page=0):
        super().__init__(name, salary, link)
        self.url = "https://api.superjob.ru/2.0/vacancies/"
        self.params = {
            "keyword": keyword,
            "page": page,
            "count": 100
        }

    def get_requests(self):
        headers = {"X-Api-App-Id": SJ_API_KEY}
        return requests.get(self.url, headers=headers, params=self.params).json()

#
# if __name__ == "__main__":
#     x = HHAPI('python')
#     y = x.get_requests()
#     print(y)
#
#     with open("hh.json", "w", encoding="utf-8") as f:
#         json.dump(y, f, ensure_ascii=False, indent=4)

#
#
# # if __name__ == "__main__":
#     x = SuperJobAPI('python')
#     y = x.get_requests()
#     print(y)
#
#
#     with open("sj.json", "w", encoding="utf-8") as f:
#         json.dump(y, f, ensure_ascii=False, indent=4)