from random import randint


def game():
    rule = 'Answer "yes" if the number is even, otherwise answer "no".'
    quastion = randint(1, 100)
    if quastion % 2 == 0:
        right_answer = 'yes'
    if quastion % 2 != 0:
        right_answer = 'no'
    return (rule, quastion, right_answer)
