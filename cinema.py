from typing import List

from film import Film
from seat import Seat
from spectator import Spectator


class Cinema:

    __seats: List[Seat]
    __film: Film

    def allocateSpectators(self, spectatorList: List[Spectator]):
        return None

    def getAllocatedSpectators(self):
        return None

    def showSeats(self):
        return None

    def getSeats(self):
        return None
