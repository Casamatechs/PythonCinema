#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string

from spectator import Spectator


class Seat:
    def __init__(self, row: int, col: int):
        self.__number = row
        self.__letter = self.__get_letter_from_idx(col)
        self.__spectator = None

    def __get_letter_from_idx(self, num):
        num2alphadict = dict(zip(range(1, 27), string.ascii_lowercase))
        outval = ""
        numloops = (num - 1) // 26

        if numloops > 0:
            outval = outval + self.__get_letter_from_idx(numloops)

        remainder = num % 26
        if remainder > 0:
            outval = outval + num2alphadict[remainder]
        else:
            outval = outval + "z"

        return outval.upper()

    def occupy_seat(self, spectator: Spectator):
        self.__spectator = spectator


    def check_availability(self):
        return self.__spectator is None

    def __str__(self) -> str:
        if self.__spectator:
            str_seat = f"[*S ,{self.__spectator.__str__()}]"

        else:
            str_seat = f"[ {self.__number:>2},  {self.__letter:>1}]"

        return str_seat
