from random import randint, choices


def game():
    rule = 'What is the result of the expression?'
    number_first = randint(0, 10)
    number_second = randint(0, 10)
    list = [' + ', ' - ', ' * ']
    sign = (choices(list, k=1))
    question = str(number_first) + sign[0] + str(number_second)
    if sign[0] == ' + ':
        right_answer = number_first + number_second
    if sign[0] == ' - ':
        right_answer = number_first - number_second
    if sign[0] == ' * ':
        right_answer = number_first * number_second
    return (rule, question, right_answer)
