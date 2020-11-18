from random import randint, choices


def game():
    rule = 'Find the greatest common divisor of given numbers.'
    x = randint(1, 5)
    y = randint(1, 5)
    list = (1, 2, 3, 5, 7, 11, 13)
    min_comm_divisor = choices(list, k=1)
    multiplier_first = randint(1, 5)
    multiplier_second = randint(1, 5)
    number_first = x * multiplier_first * min_comm_divisor[0]
    number_second = y * multiplier_second * min_comm_divisor[0]
    quastion = str(number_first) + '  ' + str(number_second)
    if number_first >= number_second:
        t = number_second
        right_answer = t
        while number_first % t != number_second % t or number_first % t != 0 or number_second % t != 0:
            t = t - 1
            right_answer = t
    elif number_first < number_second:
        t = number_first
        right_answer = t
        while number_first % t != number_second % t or number_first % t != 0 or number_second % t != 0:
            t = t - 1
            right_answer = t
    return (rule, quastion, right_answer)
