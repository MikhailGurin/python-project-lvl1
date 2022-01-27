"""Игра найти НОД."""
from math import gcd
from random import randint

from brain_games.cli import process_game


def get_conditions():
    number_one = randint(1, 100)
    number_two = randint(1, 100)
    question = '{} {}'.format(number_one, number_two)
    return question, str(gcd(number_one, number_two))


def start():
    header = 'Find the greatest common divisor of given numbers.'
    process_game(header, get_conditions)
