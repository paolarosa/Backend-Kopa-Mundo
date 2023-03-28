from teams.exceptions import NegativeTitlesError
from teams.exceptions import InvalidYearCupError
from teams.exceptions import ImpossibleTitlesError
from datetime import datetime

""" data = {
    "name": "França",
    "titles": 300,
    "top_scorer": "Zidane",
    "fifa_code": "FRA",
    "first_cup": "2000-10-18",
} """

def data_processing(dict):
    first_cup_played = datetime.strptime(dict["first_cup"],"%Y-%m-%d")
    
    if dict["titles"] < 0:
        raise NegativeTitlesError("titles cannot be negative")

    count_first = first_cup_played.year - 1930
    if count_first % 4 != 0:
        raise InvalidYearCupError("there was no world cup this year")
    datetime_atual = datetime.now()
    count_total_cups = (datetime_atual.year - first_cup_played.year) // 4
    if dict["titles"] > count_total_cups:
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")
    return dict

