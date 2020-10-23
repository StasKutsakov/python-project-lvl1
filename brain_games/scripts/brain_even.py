#!/usr/bin/env python

import prompt
from random import randint
from brain_games.scripts.brain_games import greet


def even_number():
    user_name = prompt.string('May I have your name? ')
    print('Hello, {u}!'.format(u=user_name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    template_user_answer = 'Quastion: {r}\nYour answer: '
    template_win = 'Congratulations, {u}!'
    template_exit = '\'{a}\' is wrong answer ;(. Correct answer was \'{b}\'.\nLet\'s try again, {u}!'
    i = 0
    while i < 3:
        random_number = randint(1, 100)
        user_answer = prompt.string(template_user_answer.format(r=str(random_number)))
        if (random_number % 2 == 0 and user_answer == 'yes') or (random_number % 2 != 0 and user_answer == 'no'):
            print('Correct!')
            i = i + 1
        if (random_number % 2 == 0 and user_answer == 'yes' and i == 3) or (random_number % 2 != 0 and user_answer == 'no' and i == 3):
            print(template_win.format(u=user_name))
            i = i + 1
        if random_number % 2 == 0 and user_answer == 'no':
            print(template_exit.format(a='no', b='yes', u=user_name))
            i = i + 4
        if random_number % 2 != 0 and user_answer == 'yes':
            print(template_exit.format(a='yes', b='no', u=user_name))
            i = i + 4


def main():
    greet()
    even_number()


if __name__ == '__main__':
    main()
