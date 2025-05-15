class Vacancies:
    user_vacancies = []
    user_vacancies_id = []

    __slots__ = ["_id", "_name", "_name_place", "_salary_from", "_salary_to", "_currency", "_description"]

    def __init__(self, name, name_place, salary_from, salary_to, currency, description):
        self._id = "-1"
        self._name = name
        self._name_place = name_place
        if salary_from <= 0:
            print("Зарплата не указана")
            self._salary_from = 0
        else:
            self._salary_from = salary_from
        if salary_to <= 0:
            print("Зарплата не указана")
            self._salary_to = 0
        else:
            self._salary_to = salary_to
        self._currency = currency
        self._description = description

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def name_place(self):
        return self._name_place

    @name_place.setter
    def name_place(self, new_name_place):
        self._name_place = new_name_place

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

    @property
    def salary_from(self):
        return self._salary_from

    @salary_from.setter
    def salary_from(self, new_salary_from):
        self._salary_from = new_salary_from

    @property
    def salary_to(self):
        return self._salary_to

    @salary_to.setter
    def salary_to(self, new_salary_to):
        self._salary_to = new_salary_to

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, new_currency):
        self._currency = new_currency

    def __lt__(self, other):
        if not isinstance(other, Vacancies):
            return NotImplemented
        return self._salary_from < other._salary_from

    def __le__(self, other):
        if not isinstance(other, Vacancies):
            return NotImplemented
        return self._salary_from <= other._salary_from

    def __eq__(self, other):
        if not isinstance(other, Vacancies):
            return NotImplemented
        return self._salary_from == other._salary_from

    def __gt__(self, other):
        if not isinstance(other, Vacancies):
            return NotImplemented
        return self._salary_from > other._salary_from

    def __ge__(self, other):
        if not isinstance(other, Vacancies):
            return NotImplemented
        return self._salary_from >= other._salary_from
