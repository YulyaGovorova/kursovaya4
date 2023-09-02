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
            if other.salary is None:
                # e.g., 10 < None
                return False
            if self.salary is None:
                # e.g., None < 10
                return True
        return False

    def __gt__(self, other):
        if isinstance(other, Vacancy):
            if other.salary is None:
                # e.g., 10 < None
                return True
            if self.salary is None:
                # e.g., None < 10
                return False
        return False

    def __repr__(self):
        return f"Vacancy(name='{self.name}', salary='{self.salary}', link='{self.link}')"
