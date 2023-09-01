from src.get_class import HHAPI, SJAPI
from src.utils import JSONSaver


def sort_vacancies(filtered_vacancies):
    return sorted(filtered_vacancies)


def filtere_vacancies(hh_vacancies, superjob_vacancies, filter_words):
    filtered_vacancies = []
    for vacancy in hh_vacancies + superjob_vacancies:
        if all(word in vacancy.name.lower() for word in filter_words):
            filtered_vacancies.append(vacancy)
    return filtered_vacancies


def print_vacancies(vacancies):
    for vacancy in vacancies:
        print(vacancy)





def interact_with_user():
    print("Добро пожаловать в поиск вакансий!")

    platforms = input("Пожалуйста, введите платформы, с которых вы хотите получить вакансий(HH, SJ): ")
    platforms = platforms.split()

    keyword = input("Введите ваш поисковый запрос: ")

    hh_vacancies = []
    superjob_vacancies = []

    if "HH" in platforms:
        hh_api = HHAPI(keyword)
        hh_vacancies = hh_api.get_hh_vacancies()

    if "SJ" in platforms:
        sj_api = SJAPI(keyword)
        superjob_vacancies = sj_api.get_superjob_vacancies()

    filter_words = input("Введите фильтрующие слова разделенные пробелами: ")
    filter_words = filter_words.split()

    filtered_vacancies = filtere_vacancies(hh_vacancies, superjob_vacancies, filter_words)

    sorted_vacancies = sort_vacancies(filtered_vacancies)

    print("Топ 10 вакансий:")
    print_vacancies(sorted_vacancies[:10])

    save_option = input("Сохранить вакансии в файл? (да/нет): ")
    if save_option.lower() == "да":
        filename = input("Введите имя файла для сохранения вакансий: ")
        vacancy_saver = JSONSaver(filename)
        for vacancy in sorted_vacancies:
            vacancy_saver.add_vacancy(vacancy)

interact_with_user()