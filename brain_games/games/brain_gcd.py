from random import randint, choice


rule = 'Find the greatest common divisor of given numbers.'
number_min = 1
number_max = 5
list = (1, 2, 3, 5, 7, 11, 13)


def condition():
    number_1 = randint(number_min, number_max)
    number_2 = randint(number_min, number_max)
    multiplier_1 = randint(number_min, number_max)
    multiplier_2 = randint(number_min, number_max)
    min_comm_divisor = choice(list)
    x = number_1 * multiplier_1 * int(min_comm_divisor)
    y = number_2 * multiplier_2 * int(min_comm_divisor)
    return (x, y)


def game():
    x, y = condition()
    question = ('{} {}'.format(x, y))
    if x >= y:
        t = y
    else:
        t = x
    right_answer = t
    while (x % t != y % t or x % t != 0 or y % t != 0):
        t = t - 1
        right_answer = t
    return (question, right_answer)
