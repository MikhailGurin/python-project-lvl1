"""Игра Простое ли число?"""
from random import randint
from math import sqrt

from cli import process_game


def is_prime(number):
    prime_flag = 0
    if number > 1:
        for i in range(2, int(sqrt(number)) + 1):
            if number % i == 0:
                prime_flag = 1
                break
        return prime_flag == 0
    else:
        return False


def get_conditions():
    number = randint(1, 100)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return number, correct_answer


def start():
    header = 'Answer "yes" if given number is prime. Otherwise answer "no"'
    process_game(header, get_conditions)
