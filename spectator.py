#!/usr/bin/env python
# -*- coding: utf-8 -*-

from film import Film
from seat import Seat


class Spectator:
    __id: int
    __age: int
    __available_money: float

    def __init__(self, spectator_id: int, age: int, available_money: float):
        self.__spectator_id = spectator_id
        self.__age = age
        self.__available_money = available_money

    def can_buy_film_ticket(self, film: Film):
        return self.__available_money > film.get_ticket_price() and self.__age > film.get_min_allowed_age()

    def __str__(self) -> str:
        if len(str(self.__spectator_id)) == 1:
            str_spectator_id = f"{self.__spectator_id} "
        else:
            str_spectator_id = f"{self.__spectator_id}"

        return str_spectator_id
