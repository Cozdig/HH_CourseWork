import json
from abc import ABC, abstractmethod

from src.utils import Utils
from src.vacancies import Vacancies


class JsonAbstract(ABC):

    @abstractmethod
    def add_vacancy(self, user_vacancy):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def del_vacancy(self, id_):
        pass


class Vacancy_options(JsonAbstract):

    def __init__(self, path_file="data/vacancies.json"):
        self.__path_file = path_file
        self._data = Utils.read_json(self.__path_file)

    def add_vacancy(self, user_vacancy):
        if not user_vacancy:
            return None
        elif not isinstance(user_vacancy, Vacancies):
            print("Ожидается объект класса Vacancies")
            return None


        new_vacancy_dict = {
            "name": user_vacancy.name,
            "area": {"name": user_vacancy._name_place},
            "salary": {
                "from": user_vacancy.salary_from,
                "to": user_vacancy.salary_to,
                "currency": user_vacancy.currency
            },
            "snippet": {"responsibility": user_vacancy.description}
        }

        for existing_vacancy in self._data:
            if (existing_vacancy["name"] == new_vacancy_dict["name"] and
                    existing_vacancy["area"]["name"] == new_vacancy_dict["area"]["name"] and
                    existing_vacancy.get("salary", {}).get("from") == new_vacancy_dict["salary"]["from"] and
                    existing_vacancy.get("salary", {}).get("to") == new_vacancy_dict["salary"]["to"] and
                    existing_vacancy.get("salary", {}).get("currency") == new_vacancy_dict["salary"]["currency"] and
                    existing_vacancy.get("snippet", {}).get("responsibility") == new_vacancy_dict["snippet"][
                        "responsibility"]):
                print("Такая вакансия уже существует")
                return None

        list_id = [int(i.get("id", "0")) for i in self._data + Vacancies.user_vacancies]
        new_id = str(max(list_id) + 1) if list_id else "1"

        vacancy_dict = {
            "id": new_id,
            **new_vacancy_dict
        }


        self._data.append(vacancy_dict)
        Vacancies.user_vacancies.append(vacancy_dict)
        Vacancies.user_vacancies_id.append(new_id)

        Utils.write_json(self.__path_file, self._data)
        print("Вакансия создана")

    def get_vacancies(self):
        return Vacancies.user_vacancies

    def del_vacancy(self, id_):
        id_ = str(id_)
        if id_ in Vacancies.user_vacancies_id:

            self._data = [v for v in self._data if v.get("id") != id_]
            Utils.write_json(self.__path_file, self._data)

            Vacancies.user_vacancies = [v for v in Vacancies.user_vacancies if v.get("id") != id_]

            Vacancies.user_vacancies_id.remove(id_)
            print("Вакансия удалена")
        else:
            print("Вы не можете удалять не свои вакансии")
