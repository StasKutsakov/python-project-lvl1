from random import randint


rule = 'What number is missing in the progression?'
number_min = 1
number_max = 10
n = 9


def condition():
    x = randint(number_min, number_max)
    step = randint(number_min, number_max)
    index = randint(0, n)
    progression = [str(i * step) for i in range(x, x + n + 1)]
    return (index, progression[index], progression)


def game():
    index, right_answer, progression = condition()
    progression[index] = '..'
    question = " ".join(progression)
    return (question, right_answer)
