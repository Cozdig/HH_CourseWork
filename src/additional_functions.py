import re

class UserInputHandler:
    """Класс для взаимодействия с пользователем."""
    def ask_for_conf_name(self):
        while True:
            tof = input("Хотите ли вы провести поиск вакансий? (да/нет)\n").lower().strip()
            if tof not in ("да", "нет"):
                print("Нет такого ответа. Введите 'да' или 'нет'.")
                continue
            elif tof == "да":
                return True
            elif tof == "нет":
                return False

    def ask_name_word(self):
        search = input("Введите ваш поисковой запрос: (укажите название работы)\n")
        return search


    def ask_for_conf_desc(self):
        while True:
            answer = input("Хотите ли вы искать вакансии по описанию? (да/нет)\n").strip().lower()
            if answer == "да":
                return True
            elif answer == "нет":
                return False
            else:
                print("Нет такого ответа. Введите 'да' или 'нет'.")

    def ask_key_word(self):
        while True:
            key_word = str(input("Введите ключевое слово в описании:\n"))
            if not key_word:
                print("Вы не ввели слово")
                continue
            else:
                return key_word

    def ask_for_confirmation(self):
        """Запрашивает подтверждение на формирование топа вакансий."""
        while True:
            answer = input("Хотите ли вы составить топ вакансий? (да/нет)\n").strip().lower()
            if answer == "да":
                return True
            elif answer == "нет":
                return False
            else:
                print("Нет такого ответа. Введите 'да' или 'нет'.")

    def ask_for_top_size(self):
        """Запрашивает желаемое количество вакансий в топе."""
        while True:
            try:
                size = int(input("Топ из скольких вакансий по зарплате вы хотите составить?\n"))
                if size < 1 or size > 20:
                    print("Введите число от 1 до 20.")
                else:
                    return size
            except ValueError:
                print("Некорректный ввод. Введите целое число.")

class SearchDescription:
    def __init__(self, ob):
        self.__vacancies = ob

    def search_desc(self, key_word):
        pattern = re.compile(key_word, re.IGNORECASE)
        vacancies = [vac for vac in self.__vacancies if pattern.search(vac.get("snippet", {}).get("responsibility") or "нет")]
        return vacancies


class TopVacanciesCalculator:
    """Класс для расчёта и формирования топа вакансий."""

    def __init__(self, vacancies_data):
        self.vacancies_data = vacancies_data

    def calculate_top(self, top_size):
        """Формирует топ вакансий по размеру top_size."""
        valid_vacancies = [
            (v["salary"]["from"], v)
            for v in self.vacancies_data
            if v.get("salary") and isinstance(v["salary"].get("from"), (int, float))
        ]
        sorted_vacancies = sorted(valid_vacancies, key=lambda x: x[0], reverse=True)
        top_vacancies = sorted_vacancies[:top_size]
        return [vacancy for _, vacancy in top_vacancies]

class SearchName:
    def __init__(self, ob):
        self.__vacancies = ob

    def search_name(self, search):
        pattern = re.compile(search, re.IGNORECASE)
        vacancies = [vac for vac in self.__vacancies if pattern.search(vac.get("name", ""))]
        if not vacancies:
            print("Такая(-ие) вакансия(-ии) не найдена(-ы).")
            return []
        else:
            return vacancies

def main_top(ob):
    user_input_handler = UserInputHandler()
    if user_input_handler.ask_for_confirmation():
        top_size = user_input_handler.ask_for_top_size()
        calculator = TopVacanciesCalculator(ob)
        result = calculator.calculate_top(top_size)
        return result

def main_search_desc(ob):
    user_input_handler = UserInputHandler()
    if user_input_handler.ask_for_conf_desc():
        key_word = user_input_handler.ask_key_word()
        search = SearchDescription(ob)
        result = search.search_desc(key_word)
        return result

def main_search_name(ob):
    user_input_handler = UserInputHandler()
    if user_input_handler.ask_for_conf_name():
        name_word = user_input_handler.ask_name_word()
        search = SearchName(ob)
        result = search.search_name(name_word)
        return result


