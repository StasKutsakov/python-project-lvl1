from random import randint


rule = 'Answer "yes" if the number is even, otherwise answer "no".'
number_min = 0
number_max = 100


def condition():
    x = randint(number_min, number_max)
    return x


def game():
    question = condition()
    if question % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return (question, right_answer)
