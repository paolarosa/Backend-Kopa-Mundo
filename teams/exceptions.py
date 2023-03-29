class NegativeTitlesError(Exception):
    def __init__(self, message):
        self.message = message


class InvalidYearCupError(Exception):
    def __init__(self, message):
        self.message = message
        # raise "there was no world cup this year"


class ImpossibleTitlesError(Exception):
    def __init__(self, message):
        self.message = message

#class ImpossibleFirstCup(Exception)