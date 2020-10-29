#!/usr/bin/env python

import prompt
from random import randint
from brain_games.scripts.brain_games import greet


def even_number():
    user_name = prompt.string('May I have your name? ')
    print('Hello, {u}!'.format(u=user_name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        random_number = randint(1, 100)
        user_answer = prompt.string('Quastion: {r}\nYour answer: '.format(r=random_number))
        if random_number % 2 == 0:
            right_answer = 'yes'
        if random_number % 2 != 0:
            right_answer = 'no'
        if right_answer == user_answer:
            print('Correct!')
            i = i + 1
        if right_answer == user_answer and i == 3:
            print('Congratulations, {u}!'.format(u=user_name))
            i = i + 1
        if right_answer != user_answer:
            print('\'{a}\' is wrong answer ;(. Correct answer was \'{b}\'.\nLet\'s try again, {u}!'.format(a=user_answer, b=right_answer, u=user_name))
            i = i + 4


def main():
    greet()
    even_number()


if __name__ == '__main__':
    main()
