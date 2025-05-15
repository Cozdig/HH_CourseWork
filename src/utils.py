import json


class Utils:
    @staticmethod
    def read_json(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data if isinstance(data, list) else [data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    @staticmethod
    def write_json(file_path, data):
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"Ошибка при записи в файл: {e}")
            return False

    @staticmethod
    def print_vacancy(vacancy):
        if not vacancy:
            pass
        else:
            for items in vacancy:
                print("=================================================================")
                print(f"|| id = {items.get('id', 'нет')}")
                print(f"|| название: {items.get('name', 'нет')}")
                print(f"|| место работы: {items.get('area', {}).get('name', 'не указана')}")

                salary = items.get("salary")
                if salary is None:
                    print("|| зарплата не указана")
                else:
                    salary_from = salary.get("from", "не указана")
                    salary_to = salary.get("to", "не указана")
                    currency = salary.get("currency", "валюта не указана")

                    if salary_to is None or salary_to == salary_from:
                        print(f"|| зарплата {salary_from} {currency}")
                    elif salary_from is None:
                        print(f"|| зарплата до {salary_to} {currency}")
                    else:
                        print(f"|| зарплата от {salary_from} до {salary_to} {currency}")

                responsibility = items.get("snippet", {}).get("responsibility") or "нет"
                print(f"|| описание: {responsibility}")
                print("=================================================================")
