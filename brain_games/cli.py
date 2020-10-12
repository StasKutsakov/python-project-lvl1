def welcome_user(quastion):
    name = ''
    while name == '':
        print('May I have your name? ', end='')
        name = input()
    print('Hello, {}!'.format(name))

welcome_user('May I have your name?')
