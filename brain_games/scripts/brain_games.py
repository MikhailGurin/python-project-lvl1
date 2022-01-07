#!/usr/bin/env python
"""Основной скрипт."""

from brain_games.cli import welcome_user


def main():
    """Основная функция."""
    print('Welcome to the Brain Games!')  # noqa: WPS421
    welcome_user()


if __name__ == '__main__':
    main()
