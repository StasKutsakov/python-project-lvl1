from random import randint


def game():
    rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    quastion = randint(-10, 50)
    j = quastion - 1
    if quastion > 1:
        while quastion % j != 0:
            j = j - 1
    if j == 1:
        right_answer = 'yes'
    if quastion <= 1 or j != 1:
        right_answer = 'no'
    return (rule, quastion, right_answer)
