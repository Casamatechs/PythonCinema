
class Spectator:

    __id: int
    __age: int
    __available_money: float

    def __init__(self, id: int, age: int, available_money: float):
        self.__id = id
        self.__age = age
        self.__available_money = available_money

    def getId(self) -> int:
        return self.__id

    def getAge(self) -> int:
        return self.__age

    def getAvailableMoney(self) -> float:
        return self.__available_money
