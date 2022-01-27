"""Игра Арифметическая прогрессия."""
from random import randint

from brain_games.cli import process_game


def get_conditions():
    step = randint(1, 9)
    progression = [str(i) for i in range(100)[::step]][:10]
    choice = randint(0, 9)
    correct_answer = progression[choice]
    progression[choice] = '..'

    question = ' '.join(progression)
    return question, correct_answer


def start():
    header = 'What number is missing in the progression?'
    process_game(header, get_conditions)
