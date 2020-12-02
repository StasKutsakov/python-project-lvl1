from random import randint


rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'
number_min = -10
number_max = 50


def condition():
    x = randint(number_min, number_max)
    return (x)


def game():
    question = condition()
    j = question - 1
    if question > 1:
        while question % j != 0:
            j = j - 1
    if j == 1:
        right_answer = 'yes'
    if question <= 1 or j != 1:
        right_answer = 'no'
    return (question, right_answer)
