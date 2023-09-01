import pytest

from src.get_class import SJAPI, HHAPI
from src.main import sort_vacancies
from src.utils import JSONSaver
from src.vacancy_class import Vacancy


@pytest.fixture
def hh_api():
    return HHAPI("Python")

@pytest.fixture
def sj_api():
    return SJAPI("Python")

@pytest.fixture
def json_saver():
    return JSONSaver("vacancies.json")

def test_get_hh_vacancies(hh_api):
    vacancies = hh_api.get_hh_vacancies()
    assert isinstance(vacancies, list)
    assert all(isinstance(vacancy, Vacancy) for vacancy in vacancies)

def test_get_superjob_vacancies(sj_api):
    vacancies = sj_api.get_superjob_vacancies()
    assert isinstance(vacancies, list)
    assert all(isinstance(vacancy, Vacancy) for vacancy in vacancies)

def test_add_vacancy(json_saver):
    vacancy = Vacancy("Test", "50000", "test.com")
    json_saver.add_vacancy(vacancy)
    vacancies = json_saver.get_vacancies_by_salary("50000")
    assert vacancy in vacancies

def test_delete_vacancy(json_saver):
    vacancy = Vacancy("Test", "50000", "test.com")
    json_saver.add_vacancy(vacancy)
    json_saver.delete_vacancy(vacancy)
    vacancies = json_saver.get_vacancies_by_salary("50000")
    assert vacancy not in vacancies

def test_sort_vacancies():
    vacancy1 = Vacancy("Test1", "50000", "test1.com")
    vacancy2 = Vacancy("Test2", "60000", "test2.com")
    vacancy3 = Vacancy("Test3", "40000", "test3.com")
    filtered_vacancies = [vacancy1, vacancy2, vacancy3]
    sorted_vacancies = sort_vacancies(filtered_vacancies)
    assert sorted_vacancies == [vacancy3, vacancy1, vacancy2]