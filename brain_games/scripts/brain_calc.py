#!/usr/bin/env python

import prompt
from random import randint, choices
from brain_games.scripts.brain_games import greet


def calculate_numbers():
    user_name = prompt.string('May I have your name? ')
    print('Hello, {u}!'.format(u=user_name))
    print('What is the result of the expression?')
    template_user_answer = 'Quastion: {r}\nYour answer: '
    template_win = 'Congratulations, {u}!'
    template_exit = '\'{a}\' is wrong answer ;(. Correct answer was \'{b}\'.\nLet\'s try again, {u}!'
    i = 0
    while i < 3:
        random_number_first = randint(1, 100)
        random_number_second = randint(1, 100)
        sum_of_random_numbers = random_number_first + random_number_second
        diff_of_random_numbers = random_number_first - random_number_second
        mult_of_random_numbers = random_number_first * random_number_second
        list = [sum_of_random_numbers, diff_of_random_numbers, mult_of_random_numbers]
        random_operation = (choices(list, k=1))[0]
        if str(random_operation) == str(sum_of_random_numbers):
            user_answer = prompt.string(template_user_answer.format(r=str(random_number_first) + ' + ' + str(random_number_second)))
        if str(random_operation) == str(diff_of_random_numbers):
            user_answer = prompt.string(template_user_answer.format(r=str(random_number_first) + ' - ' + str(random_number_second)))
        if str(random_operation) == str(mult_of_random_numbers):
            user_answer = prompt.string(template_user_answer.format(r=str(random_number_first) + ' * ' + str(random_number_second)))
        if user_answer == str(random_operation):
            print('Correct!')
            i = i + 1
        if user_answer == str(random_operation) and i == 3:
            print(template_win.format(u=user_name))
            i = i + 1
        if user_answer != str(random_operation):
            print(template_exit.format(a=user_answer, b=str(random_operation), u=user_name))
            i = i + 4


def main():
    greet()
    calculate_numbers()


if __name__ == '__main__':
    main()
