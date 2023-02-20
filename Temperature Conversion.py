while True:
    print('Which system are you converting to? Type in either Fahrenheit or Celsius.')
    gentemp = input()
    if gentemp == 'Fahrenheit':
        print('What temperature is it in Celsius?')
        ftemp = float(input())
        ctemp = float((ftemp * 9 / 5) + 32)
        print('In Fahrenheit, your temperature is '+str(ctemp)+' degrees.')
        print('')
    elif gentemp == 'Celsius':
        print('What temperature is it in Fahrenheit?')
        ctemp = float(input())
        ftemp = float((ctemp - 32) * 5 / 9)
        print('In Celsius, your temperature is '+str(ftemp)+' degrees.')
        print('')
    else:
        print('I don\'t understand. Can you try that again?')
    print('Would you like to convert another temperature?')
    ask = input()
    if ask == 'Yes':
        pass
    elif ask == 'No':
        print('Very well. /Script end.')
        break
    else:
        print('I don\'t understand. Answer with a Yes or No.')







#Written Saturday, January 25th, 2014.
#Modified Sunday, January 26th, 2014.
