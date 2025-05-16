from src.additional_functions import main_search_desc, main_search_name, main_top
from src.class_api import HH
from src.create_user_vacancy import add_vacancy, del_vacancy, show_vacancy
from src.utils import Utils


def main():
    api = HH()
    if not api.load_vacancies("Россия"):
        print("Не удалось загрузить вакансии. Проверьте подключение к интернету.")
        return
    answer = {
        1: lambda: Utils.print_vacancy(main_search_name(api.vacancies)),
        2: lambda: Utils.print_vacancy(main_search_desc(api.vacancies)),
        3: lambda: Utils.print_vacancy(main_top(api.vacancies)),
        4: lambda: add_vacancy(),
        5: lambda: Utils.print_vacancy(show_vacancy()),
        6: lambda: del_vacancy(),
        7: exit,
    }

    while True:
        try:
            user_input = int(
                input(
                    """Выберите действие:
1. Поиск вакансий по названию работы.
2. Поиск вакансий по описанию.
3. Составить топ вакансий по зарплате.
4. Добавить вакансию.
5. Посмотреть свои вакансии.
6. Удалить свою вакансию.
7. Выйти из программы
Ваш выбор: """
                )
            )
            if user_input in answer:
                answer[user_input]()
            else:
                print("Некорректный ввод. Пожалуйста, выберите число от 1 до 7")

        except ValueError:
            print("Пожалуйста, введите число от 1 до 7")
        except Exception as e:
            print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
