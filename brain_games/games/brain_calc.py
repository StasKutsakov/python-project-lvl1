from random import randint, choice


rule = 'What is the result of the expression?'
number_min = 0
number_max = 10
list = [' + ', ' - ', ' * ']


def condition():
    x = randint(number_min, number_max)
    y = randint(number_min, number_max)
    sign = choice(list)
    return (sign, x, y)


def game():
    sign, x, y = condition()
    question = ('{}{}{}'.format(x, sign, y))
    if sign == ' + ':
        right_answer = x + y
    if sign == ' - ':
        right_answer = x - y
    if sign == ' * ':
        right_answer = x * y
    return (question, right_answer)
