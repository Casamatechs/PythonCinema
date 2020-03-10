
class Film:

    __title: str
    __duration: int
    __min_allowed_age: int
    __director: str
    __ticket_price: float

    def __init__(self, title: str, duration: int, min_allowed_age: int, director: str, ticke_price: float):
        self.__title = title
        self.__duration = duration
        self.__min_allowed_age = min_allowed_age
        self.__director = director
        self.__ticket_price = ticke_price

    def getTitle(self) -> str:
        return self.__title

    def getDuration(self) -> int:
        return self.__duration

    def getMinAllowedAge(self) -> int:
        return self.__min_allowed_age

    def getDirector(self) -> str:
        return self.__director

    def getTicketPrice(self) -> float:
        return self.__ticket_price
