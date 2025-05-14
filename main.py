from src.additional_functions import Main_funcs, main_top
from src.utils import Utils
from src.vacancy_options import Vacancy_options
from src.class_api import HH

api = HH()
api.load_vacancies('Россия')
api_json = api.vacancies
Utils.print_vacancy(api_json)
Utils.print_vacancy(Main_funcs.just_search(api_json))
Utils.print_vacancy(main_top(api_json))

