while True:
    print('Please enter the correct password:')
    while True:
        password = 'foliage'
        user = input()
        if user == 'foliage':
            print('Welcome!')
            break
        else:
            print('Incorrect. Try again.')
    while True:
        rest = input()
        if rest == 'restart':
            print('Restarting...')
            break
        else:
            print('Error. Unrecognized command.')
