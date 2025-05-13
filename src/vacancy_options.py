from abc import ABC, abstractmethod

import json

from src.utils import read_json, write_json
from src.vacancies import Vacancies


class JsonAbstract(ABC):

    @abstractmethod
    def add_vacancy(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def del_vacancy(self, id_):
        pass

class Vacancy_options(JsonAbstract):

    def __init__(self, vacancy, path_file="../data/vacancies.json"):
        self.__path_file = path_file
        self._data = read_json(self.__path_file)
        self._vacancy = vacancy

    def add_vacancy(self):
        if self._vacancy in Vacancies.user_vacancies:
            print("Такая вакансия уже существует")
        else:
            list_id = [int(i.get("id", "0")) for i in self._data]
            new_id = str(max(list_id) + 1)
            self._vacancy.choose_id = new_id
            write_json(self.__path_file, self._vacancy)
            Vacancies.user_vacancies.append(self._vacancy)
            Vacancies.user_vacancies_id.append(new_id)

    def get_vacancies(self):
        return read_json(self.__path_file)

    def del_vacancy(self, id_):
        list_ = [v for v in self._data if v.get("id") != id_]
        with open(self.__path_file, "w", encoding="utf-8") as f:
            json.dump(list_, f, ensure_ascii=False, indent=2)

