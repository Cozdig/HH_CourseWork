import json

def read_json(file_path):
    """Функция принимает на вход путь до JSON файла и возвращает список словарей."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except Exception:
        return []

def write_json(file_path, vacancy):
    """Функция принимает на вход путь до JSON файла и записывает новые аргументы."""
    try:
        with open(file_path, "w+", encoding="utf-8") as f:
            json.dump(vacancy, f, ensure_ascii=False, indent=2)
    except Exception:
        return []

