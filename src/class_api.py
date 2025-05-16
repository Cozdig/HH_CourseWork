from abc import ABC, abstractmethod

import requests


class Parser(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __connect(self):
        pass

    @abstractmethod
    def load_vacancies(self, keyword):
        pass


class HH(Parser):
    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 50}
        self.__vacancies = []
        super().__init__()

    def _Parser__connect(self):
        try:
            response = requests.get(self.__url)
            return response.status_code == 200
        except requests.exceptions.RequestException:
            return False

    def load_vacancies(self, keyword):
        if not self._Parser__connect():
            print(f'Сервер не доступен. Ошибка: {requests.get(self.__url).status_code}')
            return False

        self.__params["text"] = keyword
        try:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            response.raise_for_status()
            vacancies = response.json().get("items", [])
            self.__vacancies.extend(vacancies)
            return True
        except (requests.exceptions.RequestException, ValueError) as e:
            print(f"Ошибка при загрузке вакансий: {e}")
            self.__vacancies = []
            return False

    @property
    def vacancies(self):
        return self.__vacancies.copy()

