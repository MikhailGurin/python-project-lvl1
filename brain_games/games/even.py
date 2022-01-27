"""Игра проверка на чётность."""
from random import randint

from brain_games.cli import process_game


def get_conditions():
    number = randint(1, 100)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return number, correct_answer


def start():
    header = 'Answer "yes" if the number is even, otherwise answer "no".'
    process_game(header, get_conditions)
