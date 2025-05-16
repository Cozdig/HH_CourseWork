import json
import os
from tempfile import NamedTemporaryFile

import pytest

from src.utils import Utils

TEST_VACANCY = {
    "id": "1",
    "name": "Python Developer",
    "area": {"name": "Москва"},
    "salary": {"from": 100000, "to": 150000, "currency": "RUR"},
    "snippet": {"responsibility": "Разработка backend на Python"},
}

TEST_VACANCY_NO_SALARY = {
    "id": "2",
    "name": "Intern",
    "area": {"name": "Санкт-Петербург"},
    "snippet": {"responsibility": "Помощь в разработке"},
}


@pytest.fixture
def temp_json_file():
    with NamedTemporaryFile(mode="w+", suffix=".json", delete=False, encoding="utf-8") as f:
        json.dump([TEST_VACANCY], f, ensure_ascii=False, indent=2)
        f.seek(0)
        yield f.name
    os.unlink(f.name)


@pytest.fixture
def empty_temp_json_file():
    with NamedTemporaryFile(mode="w+", suffix=".json", delete=False, encoding="utf-8") as f:
        yield f.name
    os.unlink(f.name)


def test_read_json_valid_file(temp_json_file):
    result = Utils.read_json(temp_json_file)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0]["name"] == "Python Developer"


def test_read_json_nonexistent_file():
    result = Utils.read_json("nonexistent_file.json")
    assert result == []


def test_write_json_success(empty_temp_json_file):
    data = [TEST_VACANCY, TEST_VACANCY_NO_SALARY]
    result = Utils.write_json(empty_temp_json_file, data)
    assert result is True

    with open(empty_temp_json_file, "r", encoding="utf-8") as f:
        content = json.load(f)
    assert len(content) == 2


def test_write_json_failure():
    result = Utils.write_json("/nonexistent/path/file.json", [TEST_VACANCY])
    assert result is False


def test_print_vacancy(capsys):
    vacancies = [TEST_VACANCY]
    Utils.print_vacancy(vacancies)
    captured = capsys.readouterr()
    assert "Python Developer" in captured.out
    assert "100000" in captured.out
    assert "150000" in captured.out
    assert "RUR" in captured.out
    assert "Разработка backend на Python" in captured.out


def test_print_vacancy_no_salary(capsys):
    vacancies = [TEST_VACANCY_NO_SALARY]
    Utils.print_vacancy(vacancies)
    captured = capsys.readouterr()
    assert "Intern" in captured.out
    assert "зарплата не указана" in captured.out
    assert "Помощь в разработке" in captured.out


def test_print_vacancy_empty(capsys):
    Utils.print_vacancy([])
    captured = capsys.readouterr()
    assert captured.out == ""


def test_print_vacancy_none(capsys):
    Utils.print_vacancy(None)
    captured = capsys.readouterr()
    assert captured.out == ""


def test_print_vacancy_partial_salary(capsys):
    partial_salary_vacancy = {
        "id": "3",
        "name": "DevOps",
        "area": {"name": "Новосибирск"},
        "salary": {"from": None, "to": 200000, "currency": "RUR"},
        "snippet": {"responsibility": "Настройка CI/CD"},
    }
    vacancies = [partial_salary_vacancy]
    Utils.print_vacancy(vacancies)
    captured = capsys.readouterr()
    assert "зарплата до 200000 RUR" in captured.out
