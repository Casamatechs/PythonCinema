import random as rand
from typing import List

from film import Film
from seat import Seat
from spectator import Spectator


class Cinema:

    def __init__(self, film: Film, rows: int, cols: int):
        self.__film = film
        self.__allocated_seats = 0
        self.__allocated_spectators = []
        self.__max_seats = int(rows * cols)
        self.__room = [[Seat(row + 1, col + 1) for col in range(cols)] for row in range(rows)]

    def allocate_spectators(self, spectator_list: List[Spectator]):
        num_rows = len(self.__room)
        num_cols = len(self.__room[0])

        for spectator in spectator_list:
            if spectator.can_buy_film_ticket(self.__film):
                allocated = False

                while not allocated:
                    row = rand.randint(0, num_rows-1)
                    col = rand.randint(0, num_cols-1)
                    allocated = self.__allocate_spectator(spectator, self.__room[row][col])

    def __allocate_spectator(self, spectator: Spectator, seat: Seat):
        result = False

        if seat.check_availability():
            seat.occupy_seat(spectator)
            self.__allocated_spectators.append(spectator)
            self.__allocated_seats = self.__allocated_seats + 1
            result = True

        return result

    def get_allocated_spectators(self):
        return self.__allocated_spectators

    def show_seats(self):
        num_cols = len(self.__room[0] * 10)
        num_spaces = int((num_cols - len("SCREEN") - 2) / 2)

        print("#" * num_cols + "\n#" + " " * num_spaces + "SCREEN" + " " * num_spaces + "#\n" + "#" * num_cols)
        print("\n\n\n")
        print('\n'.join([''.join([f' {seat.__str__()} ' for seat in row]) for row in self.__room]))
        return None

    def get_seats(self):
        list_seats = []

        for row in self.__room:
            list_seats = list_seats + row

        return list_seats
