import requests

from abc import ABC, abstractmethod


class Parser(ABC):

    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def load_vacancies(self, keyword):
        pass


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать
    """

    def __init__(self):
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'page': 0, 'per_page': 20}
        self.__vacancies = []
        super().__init__()

    def load_vacancies(self, keyword):
        self.__params['text'] = keyword
        response = requests.get(self.__url, headers=self.__headers, params=self.__params)
        vacancies = response.json()['items']
        for vac in vacancies:
            self.__vacancies.append(vac)

    @property
    def vacancies(self):
        return self.__vacancies