import json
import os

import requests

from setting import SJ_API_KEY
from src.Vacancy_class import SuperJobAPI



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

    def __repr__(self):
        return f"Vacancy(name='{self.name}', salary='{self.salary}', link='{self.link}')"



def get_hh_vacancies():
    url = "https://api.hh.ru/vacancies"
    response = requests.get(url)
    vacancies = response.json()['items']

    hh_vacancies = []
    for vacancy in vacancies:
        name = vacancy['name']
        salary = vacancy['salary']
        link = vacancy['alternate_url']
        hh_vacancies.append(Vacancy(name, salary, link))

    return hh_vacancies


def get_superjob_vacancies(keyword, headers):
    url = "https://api.superjob.ru/2.0/vacancies/"
    headers = {'X-Api-App-Id': SJ_API_KEY}
    params = {
        "town": 4,
        "catalogues": 48,
        "keywords": keyword,
        "count": 100
    }
    response = requests.get(url, headers=headers, params=params)
    vacancies = response.json()['objects']

    superjob_vacancies = []
    for vacancy in vacancies:
        name = vacancy['profession']
        salary = vacancy['payment_from']
        link = vacancy['link']
        superjob_vacancies.append(Vacancy(name, salary, link))

    return superjob_vacancies


def sort_vacancies(filtered_vacancies):
    sorted_vacancies = sorted(filtered_vacancies, key=lambda x: x["salary"], reverse=True)
    return sorted_vacancies

def filter_vacancies(hh_vacancies, superjob_vacancies, filter_words):
    filtered_vacancies = []
    for vacancy in hh_vacancies + superjob_vacancies:
        description = vacancy["description"]
        if all(word in description.lower() for word in filter_words):
            filtered_vacancies.append(vacancy)
    return filtered_vacancies

def print_vacancies(vacancies):
    for vacancy in vacancies:
        title = vacancy["name"] if "name" in vacancy else vacancy["profession"]
        url = vacancy["url"] if "url" in vacancy else vacancy["link"]
        salary = vacancy["salary"] if "salary" in vacancy else vacancy["payment_from"]
        description = vacancy["description"]
        vacancy_obj = Vacancy(title, url, salary, description)
        print(vacancy_obj)


class JSONSaver:
    def __init__(self, filename):
        self.filename = filename

    def add_vacancy(self, vacancy):
        with open(self.filename, "r") as file:
            data = json.load(file)

        data.append(vacancy.__dict__)

        with open(self.filename, "w") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def get_vacancies(self, keyword):
        with open(self.filename, "r") as file:
            data = json.load(file)

        filtered_vacancies = [vacancy for vacancy in data if keyword.lower() in vacancy["description"].lower()]

        return filtered_vacancies

    def delete_vacancies(self):
        with open(self.filename, "w") as file:
            json.dump([], file)

def user_interaction():
    SJ_API_KEY = os.getenv("SJ_API_KEY")
    superjob_api = SuperJobAPI(SJ_API_KEY)
    json_saver = JSONSaver("vacancies.json")

    while True:
        print("1. Получить вакансии с HH.ru")
        print("2. Получить вакансии с SuperJob")
        print("3. Сохранить вакансии в файл")
        print("4. Получить вакансии из файла по ключевому слову")
        print("5. Удалить вакансии из файла")
        print("6. Выход")

        choice = input("Введите ваш выбор: ")

        if choice == "1":
            query = input("ВВедите поисковый запрос: ")
            vacancies = get_hh_vacancies(query)
            for vacancy in vacancies:
                title = vacancy["name"]
                url = vacancy["url"]
                salary = vacancy["salary"]
                description = vacancy["description"]
                vacancy_obj = Vacancy(title, url, salary, description)
                print(vacancy_obj)
                json_saver.add_vacancy(vacancy_obj)

        elif choice == "2":
            query = input("ВВедите поисковый запрос: ")
            vacancies = superjob_api.get_vacancies(query)
            for vacancy in vacancies:
                title = vacancy["profession"]
                url = vacancy["link"]
                salary = vacancy["payment_from"]
                description = vacancy["description"]
                vacancy_obj = Vacancy(title, url, salary, description)
                print(vacancy_obj)
                json_saver.add_vacancy(vacancy_obj)

        elif choice == "3":
            query = input("ВВедите поисковый запрос: ")
            hh_vacancies = get_hh_vacancies(query)
            superjob_vacancies = superjob_api.get_vacancies(query)
            filter_words = input("Enter filter words (comma-separated): ").split(",")
            filtered_vacancies = filtered_vacancies(hh_vacancies, superjob_vacancies, filter_words)
            sorted_vacancies = sort_vacancies(filtered_vacancies)
            for vacancy in sorted_vacancies:
                title = vacancy["name"] if "name" in vacancy else vacancy["profession"]
                url = vacancy["url"] if "url" in vacancy else vacancy["link"]
                salary = vacancy["salary"] if "salary" in vacancy else vacancy["payment_from"]
                description = vacancy["description"]
                vacancy_obj = Vacancy(title, url, salary, description)
                print(vacancy_obj)
                json_saver.add_vacancy(vacancy_obj)

        elif choice == "4":
            keyword = input("ВВедите ключевое слово: ")
            vacancies = json_saver.get_vacancies(keyword)
            for vacancy in vacancies:
                print(vacancy)

        elif choice == "5":
            json_saver.delete_vacancies()
            print("Вакансии удалены.")

        elif choice == "6":
            break

        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")



# if __name__ == "__main__":
#     main()