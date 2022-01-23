#!/usr/bin/env python
"""Игра проверка на чётность."""
import prompt
from random import randint

from brain_games.scripts import brain_games


def main():
    """Основная функция."""
    name = brain_games.main()
    message = 'Answer "yes" if the number is even, otherwise answer "no".'
    print(message)  # noqa: WPS421
    correct_answers = 0
    while True:
        number = randint(1, 100)
        correct_answer = 'yes' if number % 2 == 0 else 'no'
        print('Question: {0}'.format(number))
        answer = prompt.string('Your answer: ')
        if answer != correct_answer:
            correct_answers = 0
            template = "'{0}' is wrong answer ;(. Correct answer was '{1}'."
            print(template.format(answer, correct_answer))
            print("Let's try again, {0}!".format(name))
        else:
            correct_answers += 1
            print('Correct!')

            if correct_answers == 3:
                print('Congratulations, {0}!'.format(name))
                break


if __name__ == '__main__':
    main()
