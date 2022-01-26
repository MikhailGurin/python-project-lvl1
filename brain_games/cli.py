"""Команды для проекта."""

import prompt


def welcome_user():
    """Приветствуем пользователя."""
    print('Welcome to the Brain Games!')  # noqa: WPS421
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))  # noqa: WPS421
    return name


def print_message(message: str):
    print(message)  # noqa: WPS421


def process_game(header, conditions):
    name = welcome_user()
    print_message(header)
    correct_answers = 0
    while True:
        question, correct_answer = conditions()
        print_message('Question: {0}'.format(question))
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
