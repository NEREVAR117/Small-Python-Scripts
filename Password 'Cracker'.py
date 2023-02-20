password = 650
start_number = 0
while True:
    user_input = input('Type HACK to hack the system: ')
    if user_input == 'HACK':
        while True:
            start_number = start_number + 1
            print(start_number)
            if start_number == password:
                print('Success! The password was:',str(start_number)+'!')
                break
            else:
                pass
        break
    else:
        print('Incorrect. Please type the right command.')
