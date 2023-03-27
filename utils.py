from exceptions import NegativeTitlesError
from exceptions import InvalidYearCupError
from exceptions import ImpossibleTitlesError
from datetime import datetime

data = {
    "name": "França",
    "titles": 300,
    "top_scorer": "Zidane",
    "fifa_code": "FRA",
    "first_cup": "2000-10-18",
}


def data_processing(dict: dict):
    if dict["titles"] < 0:
        raise NegativeTitlesError("titles cannot be negative")
    # first_cup = datetime(1930)
    count_first = 2022 - 1930
    if count_first % 4 != 0:
        return InvalidYearCupError("there was no world cup this year")
    count_total_cups = count_first
    if dict["titles"] > count_total_cups:
        return ImpossibleTitlesError(
            "impossible to have more titles than disputed cups"
        )
    return dict


function_data = data_processing(data)
print(function_data)
print("oi")
