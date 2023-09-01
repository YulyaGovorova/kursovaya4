from src.vacancy_class import Vacancy


def sort_vacancies(filtered_vacancies):
    return sorted(filtered_vacancies)

def filter_vacancies(hh_vacancies, superjob_vacancies, filter_words):
    filtered_vacancies = []
    for vacancy in hh_vacancies + superjob_vacancies:
        description = vacancy["description"]
        if all(word in description.lower() for word in filter_words):
            filtered_vacancies.append(Vacancy(
                name=vacancy.get("name", vacancy.get("profession")),
                salary=vacancy.get("salary", vacancy.get("payment_from")),
                link=vacancy.get("url", vacancy.get("link")),
                description=description
            ))
    return filtered_vacancies

def print_vacancies(vacancies):
    for vacancy in vacancies:
        print(vacancy)