from random import randint


def game():
    rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    question = randint(-10, 50)
    j = question - 1
    if question > 1:
        while question % j != 0:
            j = j - 1
    if j == 1:
        right_answer = 'yes'
    if question <= 1 or j != 1:
        right_answer = 'no'
    return (rule, question, right_answer)
