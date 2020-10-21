#!/usr/bin/env python

import prompt
from random import randint
from brain_games.scripts.brain_games import greet


def even_number():
    name = prompt.string('May I have your name? ')
    print('Hello, {a}!'.format(a=name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    y = 'yes'
    n = 'no'
    template = '\'{b}\' is wrong answer ;(. Correct answer was \'{c}\'.\nLet\'s try again, {a}!'
    i = 0
    while i < 3:
        c = randint(0, 100)
        answer = prompt.string('Quastion: ' + str(c) + '\n' + 'Your answer: ')
        if (c % 2 == 0 and answer == y) or (c % 2 != 0 and answer == n):
            print('Correct!')
            i = i + 1
        if (c % 2 == 0 and answer == y and i == 3) or (c % 2 != 0 and answer == n and i == 3):
            print('Congratulations, {a}!'.format(a=name))
        if c % 2 == 0 and answer == n:
            print(template.format(b=n, c=y, a=name))
            i = i + 4
        if c % 2 != 0 and answer == y:
            print(template.format(b=y, c=n, a=name))
            i = i + 4


def main():
    greet()
    even_number()


if __name__ == '__main__':
    main()
