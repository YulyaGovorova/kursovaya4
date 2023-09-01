from src.utils import filter_vacancies, sort_vacancies, print_vacancies
from src.get_class import HHAPI, SJAPI


def interactive_mode():
    keyword = input("Введите ключевое слово для поиска вакансий: ")
    filter_words = input("Введите фильтры через запятую: ").split(",")

    hh_api = HHAPI(keyword)
    superjob_api = SJAPI(keyword)

    try:
        hh_vacancies = hh_api.get_vacancies()
    except Exception as e:
        print("Ошибка при получении вакансий с сайта HH:", e)
        hh_vacancies = []

    superjob_vacancies = superjob_api.get_vacancies()

    filtered_vacancies = filter_vacancies(hh_vacancies, superjob_vacancies, filter_words)
    sorted_vacancies = sort_vacancies(filtered_vacancies)
    print_vacancies(sorted_vacancies)

if __name__ == "__main__":
    interactive_mode()