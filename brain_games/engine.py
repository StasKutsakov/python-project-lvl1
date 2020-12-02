import prompt


template1 = 'Hello, {}!'
template2 = 'Question: {}\nYour answer: '
template3 = 'Congratulations, {}!'
template4 = ('\'{}\' is wrong answer ;(. Correct answer was \'{}\'.'
            '\nLet\'s try again, {}!')


def engine(rule, game):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(template1.format(user_name))
    print(rule)
    for i in range(3):
        question, right_answer = game()
        user_answer = prompt.string(template2.format(question))
        if str(right_answer) == user_answer:
            print('Correct!')
            i = i + 1
        if str(right_answer) == user_answer and i == 3:
            print(template3.format(user_name))
            i = i + 1
        if str(right_answer) != user_answer:
            print(template4.format(user_answer, right_answer, user_name))
            break
