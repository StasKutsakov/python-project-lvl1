from random import randint


def game():
    rule = 'What number is missing in the progression?'
    number = randint(1, 10)
    step = randint(1, 10)
    list = [number]
    j = 1
    while j < 10:
        list.append(number + step * j)
        j = j + 1
    index = randint(0, 9)
    right_answer = list[index]
    list[index] = '  '
    k = 0
    quastion = ''
    while k < len(list):
        quastion = quastion + str(list[k]) + ' '
        k = k + 1
    return (rule, quastion, right_answer)
