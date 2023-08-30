import pytest

from src.main import Vacancy


def test_sort_vacancies():
    vacancies = [
        Vacancy("Вакансия 1", 50000, "https://hh.ru/vacancy/1"),
        Vacancy("Вакансия 2", 60000, "https://hh.ru/vacancy/2"),
        Vacancy("Вакансия 3", 40000, "https://hh.ru/vacancy/3")
    ]
    sorted_vacancies = sort_vacancies(vacancies)
    assert sorted_vacancies[0].name == "Вакансия 2"
    assert sorted_vacancies[0].salary == 60000
    assert sorted_vacancies[0].link == "https://hh.ru/vacancy/2"
    assert sorted_vacancies[1].name == "Вакансия 1"
    assert sorted_vacancies[1].salary == 50000
    assert sorted_vacancies[1].link == "https://hh.ru/vacancy/1"
    assert sorted_vacancies[2].name == "Вакансия 3"
    assert sorted_vacancies[2].salary == 40000
    assert sorted_vacancies[2].link == "https://hh.ru/vacancy/3"


def sort_vacancies(filtered_vacancies):
    sorted_vacancies = sorted(filtered_vacancies, key=lambda x: x["salary"], reverse=True)
    return sorted_vacancies

# Тестовые данные
vacancies = [
    {"title": "Вакансия 1", "salary": 50000},
    {"title": "Вакансия 2", "salary": 60000},
    {"title": "Вакансия 3", "salary": 40000}
]

# Вызов функции и сохранение результата
sorted_vacancies = sort_vacancies(vacancies)

# Вывод отсортированного списка вакансий
for vacancy in sorted_vacancies:
    print(vacancy)


{'title': 'Вакансия 2', 'salary': 60000}
{'title': 'Вакансия 1', 'salary': 50000}
{'title': 'Вакансия 3', 'salary': 40000}

if __name__ == "__main__":
    pytest.main()



