
"""The module supplies a function, welcom_user."""

import prompt


def welcome_user():
    """Get a username and say hello."""
    name = prompt.string('May I have your name? ')
    print('Hello, {a}!'.format(a=name))
