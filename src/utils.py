import json

def read_json(file_path):
    """Функция принимает на вход путь до JSON файла и возвращает список словарей."""
    try:
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
        return data
    except Exception as e:
        return []