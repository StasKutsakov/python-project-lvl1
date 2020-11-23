import prompt


def engine(game):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {u}!'.format(u=user_name))
    print(game()[0])
    i = 0
    while i < 3:
        conditions = game()
        question = conditions[1]
        right_answer = conditions[2]
        user_answer = prompt.string('Question: {q}\nYour answer: '.format(q=question))
        if str(right_answer) == str(user_answer):
            print('Correct!')
            i = i + 1
        if str(right_answer) == str(user_answer) and i == 3:
            print('Congratulations, {u}!'.format(u=user_name))
            i = i + 1
        if str(right_answer) != str(user_answer):
            print('\'{a}\' is wrong answer ;(. Correct answer was \'{b}\'.\nLet\'s try again, {u}!'.format(a=user_answer, b=right_answer, u=user_name))
            i = i + 4
