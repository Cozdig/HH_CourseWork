from io import StringIO
from unittest.mock import patch


from src.additional_functions import (
    SearchDescription,
    SearchName,
    TopVacanciesCalculator,
    UserInputHandler,
    main_search_desc,
    main_search_name,
    main_top,
)

TEST_VACANCIES = [
    {
        "name": "Python Developer",
        "snippet": {"responsibility": "Разработка на Python и Django"},
        "salary": {"from": 100000, "to": 150000},
    },
    {
        "name": "Java Developer",
        "snippet": {"responsibility": "Разработка на Java и Spring"},
        "salary": {"from": 120000, "to": 180000},
    },
    {
        "name": "DevOps Engineer",
        "snippet": {"responsibility": "Настройка CI/CD pipelines"},
        "salary": {"from": 150000, "to": 200000},
    },
    {
        "name": "Intern Python Developer",
        "snippet": {"responsibility": "Помощь в разработке на Python"},
        "salary": {"from": 30000, "to": 50000},
    },
    {"name": "Project Manager", "snippet": {"responsibility": "Управление проектами"}, "salary": None},
]


class TestUserInputHandler:
    @patch("builtins.input", side_effect=["да"])
    def test_ask_for_conf_name_positive(self, mock_input):
        handler = UserInputHandler()
        assert handler.ask_for_conf_name() is True

    @patch("builtins.input", side_effect=["нет"])
    def test_ask_for_conf_name_negative(self, mock_input):
        handler = UserInputHandler()
        assert handler.ask_for_conf_name() is False

    @patch("builtins.input", side_effect=["foo", "да"])
    def test_ask_for_conf_name_invalid_then_valid(self, mock_input):
        handler = UserInputHandler()
        with patch("sys.stdout", new=StringIO()) as fake_out:
            result = handler.ask_for_conf_name()
            assert "Нет такого ответа" in fake_out.getvalue()
        assert result is True

    @patch("builtins.input", side_effect=["0", "21", "5"])
    def test_ask_for_top_size_invalid_then_valid(self, mock_input):
        handler = UserInputHandler()
        with patch("sys.stdout", new=StringIO()) as fake_out:
            result = handler.ask_for_top_size()
            assert "Введите число от 1 до 20" in fake_out.getvalue()
        assert result == 5


class TestSearchDescription:
    def test_search_desc_found(self):
        search = SearchDescription(TEST_VACANCIES)
        result = search.search_desc("Python")
        assert len(result) == 2
        assert all("Python" in v["snippet"]["responsibility"] for v in result)

    def test_search_desc_not_found(self):
        search = SearchDescription(TEST_VACANCIES)
        result = search.search_desc("Ruby")
        assert len(result) == 0

    def test_search_desc_case_insensitive(self):
        search = SearchDescription(TEST_VACANCIES)
        result = search.search_desc("python")
        assert len(result) == 2


class TestSearchName:
    def test_search_name_found(self):
        search = SearchName(TEST_VACANCIES)
        result = search.search_name("Python")
        assert len(result) == 2
        assert all("Python" in v["name"] for v in result)

    def test_search_name_not_found(self):
        search = SearchName(TEST_VACANCIES)
        result = search.search_name("Ruby")
        assert len(result) == 0

    def test_search_name_case_insensitive(self):
        search = SearchName(TEST_VACANCIES)
        result = search.search_name("python")
        assert len(result) == 2


class TestTopVacanciesCalculator:
    def test_calculate_top(self):
        calculator = TopVacanciesCalculator(TEST_VACANCIES)
        result = calculator.calculate_top(2)
        assert len(result) == 2
        assert result[0]["name"] == "DevOps Engineer"
        assert result[1]["name"] == "Java Developer"

    def test_calculate_top_with_invalid_salaries(self):
        calculator = TopVacanciesCalculator(TEST_VACANCIES)
        result = calculator.calculate_top(10)
        assert len(result) == 4


class TestMainFunctions:
    @patch("builtins.input", side_effect=["нет"])
    def test_main_top_declined(self, mock_input):
        result = main_top(TEST_VACANCIES)
        assert result is None

    @patch("builtins.input", side_effect=["да", "2"])
    def test_main_top_accepted(self, mock_input):
        result = main_top(TEST_VACANCIES)
        assert len(result) == 2
        assert result[0]["salary"]["from"] >= result[1]["salary"]["from"]

    @patch("builtins.input", side_effect=["да", "Python"])
    def test_main_search_desc(self, mock_input):
        result = main_search_desc(TEST_VACANCIES)
        assert len(result) == 2

    @patch("builtins.input", side_effect=["нет"])
    def test_main_search_desc_declined(self, mock_input):
        result = main_search_desc(TEST_VACANCIES)
        assert result is None

    @patch("builtins.input", side_effect=["да", "Developer"])
    def test_main_search_name(self, mock_input):
        result = main_search_name(TEST_VACANCIES)
        assert len(result) == 3

    @patch("builtins.input", side_effect=["нет"])
    def test_main_search_name_declined(self, mock_input):
        result = main_search_name(TEST_VACANCIES)
        assert result is None


def test_top_with_empty_list():
    calculator = TopVacanciesCalculator([])
    result = calculator.calculate_top(5)
    assert len(result) == 0
