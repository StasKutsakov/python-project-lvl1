import prompt
from random import randint


def find_progression():
    user_name = prompt.string('May I have your name? ')
    print('Hello, {u}!'.format(u=user_name))
    print('What number is missing in the progression?')
    i = 0
    while i < 3:
        number = randint(1, 10)
        step = randint(1, 10)
        list = [number]
        j = 1
        while j < 10:
            list.append(number + step * j)
            j = j + 1
        index = randint(0, 9)
        right_answer = list[index]
        list[index] = '  '
        k = 0
        quastion = ''
        while k < len(list):
            quastion = quastion + str(list[k]) + ' '
            k = k + 1
        user_answer = prompt.string('Quastion: {r}\nYour answer: '.format(r=quastion))
        if user_answer == str(right_answer):
            print('Correct!')
            i = i + 1
        if user_answer == str(right_answer) and i == 3:
            print('Congratulations, {u}!'.format(u=user_name))
            i = i + 1
        if user_answer != str(right_answer):
            print('\'{a}\' is wrong answer ;(. Correct answer was \'{b}\'.\nLet\'s try again, {u}!'.format(a=user_answer, b=right_answer, u=user_name))
            i = i + 4
