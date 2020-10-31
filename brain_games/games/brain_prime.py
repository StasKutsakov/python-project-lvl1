import prompt
from random import randint


def is_prime_number():
    user_name = prompt.string('May I have your name? ')
    print('Hello, {u}!'.format(u=user_name))
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 0
    while i < 3:
        random_number = randint(-10, 50)
        j = random_number - 1
        user_answer = prompt.string('Quastion: {r}\nYour answer: '.format(r=random_number))
        if random_number > 1:
            while random_number % j != 0:
                j = j - 1
        if j == 1:
            right_answer = 'yes'
        if random_number <= 1 or j != 1:
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
