"""Game CLI."""

import prompt


def welcome_user():
    """User greeting output."""
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(user_name))
