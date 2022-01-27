"""Игра калькулятор."""
from random import randint, choice

from cli import process_game


def get_conditions():
    number_one = randint(1, 100)
    number_two = randint(1, 100)
    sign = choice(['+', '*', '-'])
    question = '{} {} {}'.format(number_one, sign, number_two)
    return question, str(eval(question))


def start():
    header = 'What is the result of the expression?'
    process_game(header, get_conditions)
