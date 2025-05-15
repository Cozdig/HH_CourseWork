from src.utils import Utils
from src.vacancies import Vacancies
from src.vacancy_options import Vacancy_options


class UserInputHandlerVacancy:
    """Класс для взаимодействия с пользователем."""
    def ask_for_show(self):
        while True:
            tof = input("Хотите ли вы посмотреть свои вакансии? (да/нет)\n").lower().strip()
            if tof not in ("да", "нет"):
                print("Нет такого ответа. Введите 'да' или 'нет'.")
                continue
            elif tof == "да":
                return True
            elif tof == "нет":
                return False

    def ask_for_add(self):
        while True:
            tof = input("Хотите ли вы добавить вакансию? (да/нет)\n").lower().strip()
            if tof not in ("да", "нет"):
                print("Нет такого ответа. Введите 'да' или 'нет'.")
                continue
            elif tof == "да":
                return True
            elif tof == "нет":
                return False

    def ask_for_add_vacancy(self):
        name = input("Введите название вакансии:\n")
        place = input("Введите место работы:\n")
        while True:
            try:
                from_sal = int(input("Введите зарплату от: (Число)\n"))
                break
            except ValueError:
                print("Ошибка! Нужно ввести целое число.")

        while True:
            try:
                to_sal = int(input("Введите зарплату до: (Число)\n"))
                break
            except ValueError:
                print("Ошибка! Нужно ввести целое число.")

        currency = input("Введите валюту зарплаты:\n")
        res = input("Введите описание работы:\n")
        return name,place,from_sal,to_sal,currency,res

    def ask_for_del(self):
        while True:
            tof = input("Хотите ли вы удалить свою вакансию? (да/нет)\n").lower().strip()
            if tof not in ("да", "нет"):
                print("Нет такого ответа. Введите 'да' или 'нет'.")
                continue
            elif tof == "да":
                return True
            elif tof == "нет":
                return False

    def ask_for_correct_id(self):
        while True:
            try:
                vac = Vacancy_options()
                Utils.print_vacancy(vac.get_vacancies())
                id_ = str(input("Напишите id вакансии:\n"))
                return id_
            except TypeError:
                print("Ошибка! Вы ввели не число")
                continue


class UserVacancy:
    def __init__(self, name, place, from_sal, to_sal, currency, res):
        self.__name = name
        self.__place = place
        self.__from_sal = from_sal
        self.__to_sal = to_sal
        self.__currency = currency
        self.__res = res
    def to_dict(self):
        return {
            'name': self.__name,
            'area': {'name': self.__place},
            'salary': {'from': self.__from_sal, 'to': self.__to_sal, 'currency': self.__currency},
            'snippet': {'responsibility': self.__res}
        }

def create_vacancy():
    user_input = UserInputHandlerVacancy()
    if user_input.ask_for_add():
        words = user_input.ask_for_add_vacancy()
        name, place, from_sal, to_sal, currency, description = words
        create = UserVacancy(name, place, from_sal, to_sal, currency, description)
        new_vac = Vacancies(
            name=create.to_dict()['name'],
            name_place=create.to_dict()['area']['name'],
            salary_from=create.to_dict()['salary']['from'],
            salary_to=create.to_dict()['salary']['to'],
            currency=create.to_dict()['salary']['currency'],
            description=create.to_dict()['snippet']['responsibility']
        )
        return new_vac

def show_vacancy():
    user_input = UserInputHandlerVacancy()
    if user_input.ask_for_show():
        vac = Vacancy_options()
        return vac.get_vacancies()

def del_vacancy():
    user_input = UserInputHandlerVacancy()
    if user_input.ask_for_del():
        id_ = user_input.ask_for_correct_id()
        vac = Vacancy_options()
        vac.del_vacancy(id_)

def add_vacancy():
    vac = Vacancy_options()
    add_vac = vac.add_vacancy(create_vacancy())
    return add_vac