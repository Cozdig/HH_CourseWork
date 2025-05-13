class Vacancies:
    user_vacancies = []
    user_vacancies_id = []

    __slots__ = ["_name", "_link", "_salary", "_description", "_id"]
    def __init__(self, name, link, salary, description):
        if salary <= 0:
            print("Зарплата не указана")
            self._salary = 0
        else:
            self._salary = salary
        self._id = "-1"
        self._name = name
        self._link = link
        self._description = description
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, new_link):
        self._link = new_link

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        self._salary = new_salary

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, new_description):
        self._description = new_description

    @property
    def choose_id(self):
        return self._id

    @choose_id.setter
    def choose_id(self, new_id):
        self._id = new_id

    def __lt__(self, other):
        if not isinstance(other, Vacancies):
            return NotImplemented
        return self.salary < other.salary

    def __le__(self, other):
        if not isinstance(other, Vacancies):
            return NotImplemented
        return self.salary <= other.salary

    def __eq__(self, other):
        if not isinstance(other, Vacancies):
            return NotImplemented
        return self.salary == other.salary

    def __gt__(self, other):
        if not isinstance(other, Vacancies):
            return NotImplemented
        return self.salary > other.salary

    def __ge__(self, other):
        if not isinstance(other, Vacancies):
            return NotImplemented
        return self.salary >= other.salary