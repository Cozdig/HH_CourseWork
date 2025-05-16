import json
import os
from unittest.mock import patch

import pytest

from src.vacancies import Vacancies
from src.vacancy_options import JsonAbstract, Vacancy_options


@pytest.fixture
def sample_vacancy():
    return Vacancies(
        name="Python Developer",
        name_place="Remote",
        salary_from=100000,
        salary_to=150000,
        currency="RUB",
        description="Разработка на Python",
    )


@pytest.fixture
def vacancy_options(tmp_path):
    test_file = tmp_path / "vacancies.json"
    test_file.write_text(json.dumps([]))
    return Vacancy_options(path_file=str(test_file))


def test_abstract_methods():
    with pytest.raises(TypeError):
        JsonAbstract()


def test_add_vacancy_success(vacancy_options, sample_vacancy):
    with patch("builtins.print") as mock_print:
        vacancy_options.add_vacancy(sample_vacancy)
        mock_print.assert_called_with("Вакансия создана")

    vacancies = vacancy_options.get_vacancies()
    assert len(vacancies) == 1
    assert vacancies[0]["name"] == "Python Developer"
    assert vacancies[0]["area"]["name"] == "Remote"


def test_add_existing_vacancy(vacancy_options, sample_vacancy):
    vacancy_options.add_vacancy(sample_vacancy)
    with patch("builtins.print") as mock_print:
        vacancy_options.add_vacancy(sample_vacancy)
        mock_print.assert_called_with("Такая вакансия уже существует")

    assert len(vacancy_options.get_vacancies()) == 2


def test_add_invalid_vacancy(vacancy_options):
    with patch("builtins.print") as mock_print:
        result = vacancy_options.add_vacancy("invalid")
        mock_print.assert_called_with("Ожидается объект класса Vacancies")
        assert result is None


def test_get_vacancies(vacancy_options, sample_vacancy):
    assert vacancy_options.get_vacancies() == [
        {
            "area": {
                "name": "Remote",
            },
            "id": "1",
            "name": "Python Developer",
            "salary": {
                "currency": "RUB",
                "from": 100000,
                "to": 150000,
            },
            "snippet": {
                "responsibility": "Разработка на Python",
            },
        },
        {
            "area": {
                "name": "Remote",
            },
            "id": "2",
            "name": "Python Developer",
            "salary": {
                "currency": "RUB",
                "from": 100000,
                "to": 150000,
            },
            "snippet": {
                "responsibility": "Разработка на Python",
            },
        },
    ]
    vacancy_options.add_vacancy(sample_vacancy)
    assert len(vacancy_options.get_vacancies()) == 3


def test_del_vacancy_success(vacancy_options, sample_vacancy):
    vacancy_options.add_vacancy(sample_vacancy)
    vacancy_id = Vacancies.user_vacancies_id[0]

    with patch("builtins.print") as mock_print:
        vacancy_options.del_vacancy(vacancy_id)
        mock_print.assert_called_with("Вакансия удалена")

    assert vacancy_id not in Vacancies.user_vacancies_id
    assert len(vacancy_options.get_vacancies()) == 3


def test_del_nonexistent_vacancy(vacancy_options):
    with patch("builtins.print") as mock_print:
        vacancy_options.del_vacancy("999")
        mock_print.assert_called_with("Вы не можете удалять не свои вакансии")


def test_file_operations(tmp_path, sample_vacancy):
    test_file = tmp_path / "test_vacancies.json"
    vo = Vacancy_options(path_file=str(test_file))

    vo.add_vacancy(sample_vacancy)
    assert os.path.exists(str(test_file))

    with open(str(test_file), "r") as f:
        data = json.load(f)
        assert len(data) == 1
        assert data[0]["name"] == "Python Developer"

    vo.del_vacancy(Vacancies.user_vacancies_id[0])
    with open(str(test_file), "r") as f:
        data = json.load(f)
        assert len(data) == 1
