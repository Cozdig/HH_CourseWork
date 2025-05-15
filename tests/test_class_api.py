from unittest.mock import patch

import pytest
import requests

from src.class_api import HH


class TestHH:
    @pytest.fixture
    def hh_instance(self):
        return HH()

    @patch("requests.get")
    def test_load_vacancies_api_error(self, mock_get, hh_instance):
        mock_get.side_effect = requests.exceptions.RequestException("API Error")

        hh_instance.load_vacancies("C++")

        assert len(hh_instance.vacancies) == 0

    def test_vacancies_property(self, hh_instance):
        test_vacancies = [{"id": 1}, {"id": 2}]
        hh_instance._HH__vacancies = test_vacancies

        returned_vacancies = hh_instance.vacancies

        assert returned_vacancies == test_vacancies

        hh_instance._HH__vacancies.append({"id": 3})
        assert len(returned_vacancies) == 2
        assert len(hh_instance.vacancies) == 3
