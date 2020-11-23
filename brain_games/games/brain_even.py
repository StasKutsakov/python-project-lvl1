from random import randint


def game():
    rule = 'Answer "yes" if the number is even, otherwise answer "no".'
    question = randint(1, 100)
    if question % 2 == 0:
        right_answer = 'yes'
    if question % 2 != 0:
        right_answer = 'no'
    return (rule, question, right_answer)
