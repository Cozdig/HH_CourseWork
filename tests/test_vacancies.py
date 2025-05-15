import pytest

from src.vacancies import Vacancies


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
def sample_vacancy_no_salary():
    return Vacancies(
        name="Intern", name_place="Office", salary_from=0, salary_to=0, currency="USD", description="Стажировка"
    )


def test_vacancy_initialization(sample_vacancy):
    assert sample_vacancy.name == "Python Developer"
    assert sample_vacancy.name_place == "Remote"
    assert sample_vacancy.salary_from == 100000
    assert sample_vacancy.salary_to == 150000
    assert sample_vacancy.currency == "RUB"
    assert sample_vacancy.description == "Разработка на Python"
    assert sample_vacancy.choose_id == "-1"


def test_no_salary_handling(capsys, sample_vacancy_no_salary):
    assert sample_vacancy_no_salary.salary_from == 0
    assert sample_vacancy_no_salary.salary_to == 0
    captured = capsys.readouterr()
    assert "Зарплата не указана" in captured.out


def test_property_setters(sample_vacancy):
    sample_vacancy.name = "Senior Python Developer"
    assert sample_vacancy.name == "Senior Python Developer"

    sample_vacancy.description = "Senior разработка"
    assert sample_vacancy.description == "Senior разработка"

    sample_vacancy.choose_id = "123"
    assert sample_vacancy.choose_id == "123"

    sample_vacancy.salary_from = 120000
    assert sample_vacancy.salary_from == 120000

    sample_vacancy.salary_to = 180000
    assert sample_vacancy.salary_to == 180000

    sample_vacancy.currency = "USD"
    assert sample_vacancy.currency == "USD"


def test_comparison_operators():
    vacancy1 = Vacancies("Dev1", "Loc1", 50000, 70000, "RUB", "Desc1")
    vacancy2 = Vacancies("Dev2", "Loc2", 70000, 90000, "RUB", "Desc2")
    vacancy3 = Vacancies("Dev3", "Loc3", 50000, 80000, "RUB", "Desc3")

    assert vacancy1 < vacancy2
    assert vacancy1 <= vacancy2
    assert vacancy1 <= vacancy3
    assert vacancy2 > vacancy1
    assert vacancy2 >= vacancy1
    assert vacancy1 == vacancy3
    assert vacancy1 != vacancy2


def test_slots():
    vacancy = Vacancies("Test", "Test", 1000, 2000, "EUR", "Test")
    with pytest.raises(AttributeError):
        vacancy.non_existent_attr = "value"
