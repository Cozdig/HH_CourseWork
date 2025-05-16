from unittest.mock import MagicMock, patch

import pytest

from src.create_user_vacancy import (
    UserInputHandlerVacancy,
    UserVacancy,
    add_vacancy,
    create_vacancy,
    del_vacancy,
    show_vacancy,
)
from src.vacancies import Vacancies


class TestUserInputHandlerVacancy:
    @pytest.fixture
    def handler(self):
        return UserInputHandlerVacancy()

    @patch("builtins.input")
    def test_ask_for_add_vacancy(self, mock_input, handler):
        mock_input.side_effect = ["Python Developer", "Moscow", "100000", "150000", "RUR", "Разработка"]
        result = handler.ask_for_add_vacancy()
        assert result == ("Python Developer", "Moscow", 100000, 150000, "RUR", "Разработка")


class TestUserVacancy:
    def test_to_dict(self):
        vacancy = UserVacancy("Python Dev", "Remote", 100000, 150000, "RUR", "Разработка")
        expected = {
            "name": "Python Dev",
            "area": {"name": "Remote"},
            "salary": {"from": 100000, "to": 150000, "currency": "RUR"},
            "snippet": {"responsibility": "Разработка"},
        }
        assert vacancy.to_dict() == expected


class TestVacancyFunctions:
    @patch("src.create_user_vacancy.UserInputHandlerVacancy.ask_for_add")
    @patch("src.create_user_vacancy.UserInputHandlerVacancy.ask_for_add_vacancy")
    def test_create_vacancy(self, mock_ask_details, mock_ask_add):
        mock_ask_add.return_value = True
        mock_ask_details.return_value = ("Dev", "Remote", 100000, 150000, "RUR", "Code")

        result = create_vacancy()
        assert isinstance(result, Vacancies)
        assert result.name == "Dev"

    @patch("src.create_user_vacancy.UserInputHandlerVacancy.ask_for_show")
    @patch("src.vacancy_options.Vacancy_options.get_vacancies")
    def test_show_vacancy(self, mock_get_vacancies, mock_ask_show):
        mock_ask_show.return_value = True
        mock_get_vacancies.return_value = [{"id": "1", "name": "Test"}]
        assert show_vacancy() == [{"id": "1", "name": "Test"}]

    @patch("src.create_user_vacancy.UserInputHandlerVacancy.ask_for_del")
    @patch("src.create_user_vacancy.UserInputHandlerVacancy.ask_for_correct_id")
    @patch("src.vacancy_options.Vacancy_options.del_vacancy")
    def test_del_vacancy(self, mock_del, mock_ask_id, mock_ask_del):
        mock_ask_del.return_value = True
        mock_ask_id.return_value = "123"
        del_vacancy()
        mock_del.assert_called_once_with("123")

    @patch("src.create_user_vacancy.create_vacancy")
    @patch("src.vacancy_options.Vacancy_options.add_vacancy")
    def test_add_vacancy(self, mock_add, mock_create):
        mock_vac = MagicMock()
        mock_create.return_value = mock_vac
        add_vacancy()
        mock_add.assert_called_once_with(mock_vac)
