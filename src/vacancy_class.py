import json
import os
from abc import ABC, abstractmethod
from typing import List

import requests

from setting import SJ_API_KEY


class API(ABC):
    @abstractmethod
    def get_vacancies(self, query: str) -> List[dict]:
        pass

class Vacancy:
    def __init__(self, name, salary, link):
        self.name = name
        self.salary = salary
        self.link = link

    def __eq__(self, other):
        if isinstance(other, Vacancy):
            return self.salary == other.salary
        return False

    def __lt__(self, other):
        if isinstance(other, Vacancy):
            return self.salary < other.salary
        return False

    def __gt__(self, other):
        if isinstance(other, Vacancy):
            return self.salary > other.salary
        return False

    def __repr__(self):
        return f"Vacancy(name='{self.name}', salary='{self.salary}', link='{self.link}')"