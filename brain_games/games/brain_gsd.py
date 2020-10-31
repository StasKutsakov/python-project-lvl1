import prompt
from random import randint, choices


def find_divisor():
    user_name = prompt.string('May I have your name? ')
    print('Hello, {u}!'.format(u=user_name))
    print('Find the greatest common divisor of given numbers.')
    i = 0
    while i < 3:
        x = randint(1, 5)
        y = randint(1, 5)
        list = (1, 2, 3, 5, 7, 11, 13)
        min_comm_divisor = choices(list, k=1)
        multiplier_1 = randint(1, 5)
        multiplier_2 = randint(1, 5)
        random_number_first = x * multiplier_1 * min_comm_divisor[0]
        random_number_second = y * multiplier_2 * min_comm_divisor[0]
        if random_number_first > random_number_second:
            t = random_number_second
            right_answer = t
            while random_number_first % t != random_number_second % t or random_number_first % t != 0 or random_number_second % t != 0:
                t = t - 1
                right_answer = t
        elif random_number_first < random_number_second:
            t = random_number_first
            right_answer = t
            while random_number_first % t != random_number_second % t or random_number_first % t != 0 or random_number_second % t != 0:
                t = t - 1
                right_answer = t
        quastion = str(random_number_first) + '  ' + str(random_number_second)
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
