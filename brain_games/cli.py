"""Команды для проекта."""

import prompt


def welcome_user():
    """Приветствуем пользователя."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))  # noqa: WPS421
    return name
