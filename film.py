#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Film:

    def __init__(self, title: str, duration: int, min_allowed_age: int, director: str, ticket_price: float):
        self.__title = title
        self.__duration = duration
        self.__min_allowed_age = min_allowed_age
        self.__director = director
        self.__ticket_price = ticket_price

    def get_ticket_price(self):
        return self.__ticket_price

    def get_min_allowed_age(self):
        return self.__min_allowed_age

    def __str__(self) -> str:
        return f"\n\t - Title: {self.__title}" \
               f"\n\t - Director: {self.__director}" \
               f"\n\t - Duration: {self.__duration}" \
               f"\n\t - Minimum Allowed Age: {self.__min_allowed_age}" \
               f"\n\t - Ticket Price: {self.__ticket_price}"
