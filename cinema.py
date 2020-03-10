from functools import reduce
from typing import List

from film import Film
from seat import Seat
from spectator import Spectator


class Cinema:

    __seats: List[List[Seat]]
    __film: Film

    def __init__(self, nRows: int, nColumns: int, film: Film):
        self.__film = film
        self.__seats = self.__generateSeats(nRows, nColumns)

    def __generateSeats(self, rows: int, cols: int):
        seatsArray: List[str] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                                 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        seats: List[List[Seat]] = []
        for i in range(rows):
            rowSeats: List[Seat] = []
            for j in range(cols):
                rowSeats.append(Seat(i + 1, seatsArray[j]))
            seats.append(rowSeats)
        return seats

    def allocateSpectators(self, spectatorList: List[Spectator]):
        return None

    def getAllocatedSpectators(self):
        return None

    def showSeats(self):
        nCol: int = len(self.__seats[0])
        upDownScreenLine: str = '#'*(8*nCol+1)
        screenLine: str = '#{}SCREEN{}#'.format(' '*int((8*nCol-7)/2), ' '*int((8*nCol-7)/2+1))
        print(upDownScreenLine)
        print(screenLine)
        print(upDownScreenLine)
        print('\n\n')
        for row in self.__seats:
            for seat in row:
                print(' '+seat.printSeat(), end='')
            print()


    def getSeats(self) -> List[List[Seat]]:
        return reduce(list.__add__, self.__seats)
