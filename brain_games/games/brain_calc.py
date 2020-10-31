import prompt
from random import randint, choices


def calculate_number():
    user_name = prompt.string('May I have your name? ')
    print('Hello, {u}!'.format(u=user_name))
    print('What is the result of the expression?')
    i = 0
    while i < 3:
        random_number_first = randint(0, 10)
        random_number_second = randint(0, 10)
        list = [' + ', ' - ', ' * ']
        random_sign = (choices(list, k=1))
        quastion = str(random_number_first) + random_sign[0] + str(random_number_second)
        user_answer = prompt.string('Quastion: {r}\nYour answer: '.format(r=quastion))
        if random_sign[0] == ' + ':
            right_answer = random_number_first + random_number_second
        if random_sign[0] == ' - ':
            right_answer = random_number_first - random_number_second
        if random_sign[0] == ' * ':
            right_answer = random_number_first * random_number_second
        if user_answer == str(right_answer):
            print('Correct!')
            i = i + 1
        if user_answer == str(right_answer) and i == 3:
            print('Congratulations, {u}!'.format(u=user_name))
            i = i + 1
        if user_answer != str(right_answer):
            print('\'{a}\' is wrong answer ;(. Correct answer was \'{b}\'.\nLet\'s try again, {u}!'.format(a=user_answer, b=right_answer, u=user_name))
            i = i + 4
