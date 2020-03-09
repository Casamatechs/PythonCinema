from spectator import Spectator


class Seat:

    __row: int
    __column: str
    __available: bool
    __spectator: Spectator

    def __init__(self, row: int, col: str):
        self.__row = row
        self.__column = col
        self.__spectator = None
        self.__available = True

    def getRow(self):
        return self.__row

    def getColumn(self):
        return self.__column

    def isAvailable(self):
        return self.__available

    def getSpectator(self):
        return self.__spectator

    def setSpectator(self, spectator: Spectator) -> None:
        self.__spectator = spectator
        self.__available = False

    def removeSpectator(self):
        self.__spectator = None
        self.__available = True

    def printSeat(self):
        if self.__spectator is None:
            return '[ {}, {}]'.format(self.__row, self.__column)
        else:
            return '[*S ,*{}]'.format(self.__spectator.getId())
